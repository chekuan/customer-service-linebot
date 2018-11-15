from rest_framework.views import  APIView
from rest_framework.response import Response

from linebot import WebhookParser
from linebot.models import MessageEvent, TextMessage

from chatbot import settings
from .helper import identify_program_intent
from .state import none_state, program_state1, program_state2, program_state3, program_state4

parser = WebhookParser(settings.LINE_CHANNEL_SECRET)



class Webhook(APIView):

    def get(self, request, format=None):
        #  這個 handler 僅供測試 django restful framework 使用
        print(request)

        return Response({
            'text':'hello',
        })

    def post(self, request, format=None):
        # Line message API handler
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        events = parser.parse(request.body.decode('utf-8'), signature)

        for event in events:

            if isinstance(event, MessageEvent):
                if isinstance(event.message, TextMessage):
                    user_id = event.source.user_id
                    message = event.message.text

                    # 判別目前的訊息可能是滿足哪一個 program intent
                    program_intent = identify_program_intent(message)

                    # 將目前的 state 辨別出來，可能是對應到 None Intent State or 特定 Program 的 State
                    # 在 current_state.act() 中會觸發那個 state 的實際效果，並且 state transition 也在
                    # current_state 進行
                    if program_intent == 1:
                        current_state = program_state1
                    elif program_intent == 2:
                        current_state = program_state2
                    elif program_intent == 3:
                        current_state = program_state3
                    elif program_intent == 4:
                        current_state = program_state4
                    else:
                        current_state = none_state

                    current_state.act(message, user_id, event.reply_token)

        return Response()