"""このモジュールの目的や機能を簡潔に説明します。"""

from flask import Flask,request,abort
from linebot import LineBotApi,WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MassageEvent, TextMessage, TextSendMessage

app=Flask(_neme_)