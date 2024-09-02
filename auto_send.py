"""
This module handles the automatic sending of LINE messages based on a schedule.
"""

import time
import schedule
from linebot import LineBotApi
from linebot.models import TextSendMessage

#LINE API設定
line_bot_api=LineBotApi()