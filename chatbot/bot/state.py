# 這個檔案在實作 Finite State Machine, 利用 State Pattern
# 來實作每一個 State 不同的效果以及 transition。
# 我們利用 redis 這樣的 memory database 去紀錄
#
# 目前在 State 的命名比較不好。


from django.core.cache import cache

from .models import Program, UnableToHandleMsg
from .reply_messages import program_fields_reply
from .condition import conditions_in_sentence
from .helper import send_text_message, send_template_message, send_carousel_message


def set_state(user_id, state):
    cache.set(user_id + '_state', state, timeout=600)


class State:
    def act(self, message, user_id, reply_to):
        pass


class NoneState(State):

    @classmethod
    def act(self, message, user_id, reply_to):

        if '查看業務' in message:
            set_state(user_id, none_state)
            send_carousel_message(reply_to, Program.objects.all())
        else:
            previous_state = get_state(user_id)

            if conditions_in_sentence(message):
                reply_msg = program_fields_reply(previous_state.program, message)
            else:
                # TODO batch creation
                UnableToHandleMsg.objects.create(
                    poster=user_id,
                    msg=message
                )
                reply_msg =  '這個問題，我沒有辦法辨認。請查看使用說明，或是直接詢問承辦人員。'
                set_state(user_id, none_state)

            send_text_message(reply_to, reply_msg)


class ProgramState(State):

    def __init__(self):
        self.program = None

    def act(self, message, user_id, reply_to):
        previous_state = get_state(user_id)
        if isinstance(previous_state, self.__class__):
            if conditions_in_sentence(message):
                reply_msg = program_fields_reply(self.program, message)
                send_text_message(reply_to, reply_msg)
            else:
                # TODO batch creation
                UnableToHandleMsg.objects.create(
                    poster=user_id,
                    msg=message
                )
                reply_msg = '這個問題或許和{}相關，可以利用選單功能查看相關資訊，或是詢問承辦人員。'.format(self.program.name)
                send_text_message(reply_to, reply_msg)
        else:
            # with transition
            if conditions_in_sentence(message):
                reply_msg = program_fields_reply(self.program, message)
                send_text_message(reply_to, reply_msg)
            else:
                send_template_message(reply_to, self.program)

            set_state(user_id, self)


class Program1State(ProgramState):
    # 目前對應到出席國際會議論文補助
    def __init__(self):
        self.program = Program.objects.get(program_id=1)


class Program2State(ProgramState):
    # 雙向研修補助
    def __init__(self):
        self.program = Program.objects.get(program_id=2)


class Program3State(ProgramState):
    # 國際志工補助
    def __init__(self):
        self.program = Program.objects.get(program_id=3)


class Program4State(ProgramState):
    # 學海築夢計畫
    def __init__(self):
        self.program = Program.objects.get(program_id=4)


# TODO code refactoring
# 因為希望節省記憶體，所以在創建物件的時候，希望藉由這種方式只創建一次記憶體
# 但是目前的寫法比較糟糕一些，在相依性的設計上有些混亂，這是需要 refactoring 的地方。
none_state = NoneState()
program_state1 = Program1State()
program_state2 = Program2State()
program_state3 = Program3State()
program_state4 = Program4State()


def get_state(user_id):
    state = cache.get(user_id + '_state')
    if state is None:
        state =  none_state
    return state



