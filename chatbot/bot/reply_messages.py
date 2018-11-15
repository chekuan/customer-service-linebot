from .condition import (
    brief, time, details, requirements,
    qualification, notice
)


general_reply = (
                '國際事務處有負責以下這些業務申請:\n'
                '1. 國際會議補助\n'
                '2. 學生跨國雙向研修獎助學金\n' 
                '3. 海外國際短期志工服務學習補助\n'
                '4. 教育部補助出國研修實習補助 - 學海築夢計畫\n\n'
                '如果不知道怎麼使用下方選單查看使用說明喔！'
                )

def program_fields_reply(program, message):
    if any(cond in message for cond in brief):
        reply_msg = '{}的簡介:\n{}'.format(program.name, program.brief_intro)
    elif any(cond in message for cond in time):
        reply_msg = '{}的申請日期: {}'.format(program.name, program.duration)
    elif any(cond in message for cond in details):
        reply_msg = '{}的詳細資訊:\n{}'.format(program.name, program.details)
    elif any(cond in message for cond in requirements):
        reply_msg = '{}需要遞交的文件\n {}'.format(program.name, program.requirements)
    elif any(cond in message for cond in qualification):
        reply_msg = '{}的申請條件:\n {}'.format(program.name, program.qualification)
    elif any(cond in message for cond in notice):
        reply_msg = '{}的注意事項:\n{}'.format(program.name, program.notice)
    return reply_msg