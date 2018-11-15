import operator

import jieba
from linebot import LineBotApi
from linebot.models import (
    TextSendMessage, TemplateSendMessage, CarouselTemplate, ButtonsTemplate,
    MessageTemplateAction, URITemplateAction, CarouselColumn
)
from django.core.cache import cache
from chatbot import settings

from utils import utils


intent_identifier = utils.QueryProcess()
line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)


def identify_program_intent(sentence):
    segmented_words = jieba.lcut(sentence)
    result = intent_identifier.get_category(segmented_words)
    sorted_result = sorted(result.items(), key=operator.itemgetter(1), reverse=True)

    if len(sorted_result) == 0:
        intent = []
    else:
        intent = int(sorted_result[0][0])

    return intent


def send_text_message(reply_to, message):
        line_bot_api.reply_message(
            reply_to,
            TextSendMessage(text=message)
        )


def send_template_message(reply_to, program):
    line_bot_api.reply_message(
        reply_to,
        TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                thumbnail_image_url='https://upload.wikimedia.org/wikipedia/zh/thumb/8/83/National_Cheng_Kung_University_logo.svg/200px-National_Cheng_Kung_University_logo.svg.png',
                title=program.name,
                text=program.brief_intro,
                actions=[
                    MessageTemplateAction(
                        label='申請資格',
                        text=program.name + '的資格',
                    ),
                    MessageTemplateAction(
                        label='相關時程與期限',
                        text=program.name + '的期限'
                    ),
                    MessageTemplateAction(
                        label='繳交文件',
                        text=program.name + '要繳交的文件'
                    ),
                    URITemplateAction(
                        label='詳細辦法',
                        uri=program.details
                    ),
                ]
            )
        )
    )


def send_carousel_message(reply_to, programs):
    line_bot_api.reply_message(
        reply_to,
        TemplateSendMessage(
            alt_text='Carousel Template',
            template=CarouselTemplate(columns=[

                CarouselColumn(
                    title=program.name,
                    text=program.brief_intro,
                    actions=[
                        MessageTemplateAction(
                            label='查看相關資訊',
                            text=program.name
                        )
                    ]
                ) for program in programs
            ])
        )
    )

