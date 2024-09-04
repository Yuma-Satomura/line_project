"""
This module handles the automatic sending of LINE messages based on a schedule.
"""

import time
import schedule
from linebot import LineBotApi
from linebot.models import TextSendMessage

#LINE API設定
line_bot_api = LineBotApi('jqrBbcHm5zvuC4/uGV7vN2Vbqccpqb+CWlk+W26uTJgQO0GcC3Btc0v5tICPdwwnYPpUjzgGuCw+80rtmg2a4BSucJRp7vvdTGDQEoTYQksIUuJFsGCtSyzeYMZtiYCu0n8RMbg4mJMeTzlSW8ek2wdB04t89/1O/w1cDnyilFU=')

user_id=""