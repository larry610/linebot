from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler, exceptions)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *


# Channel access token
line_bot_api = LineBotApi("gnohpWNe3+rTsVP/HGQtBADT7XsAwWPQp13pmXmWIczKi7lvgs4aX6YV4khZVI9JxVIWsc3ynsJ+Opi+Ve1JZOwYpjqU/Ra+Is4QnjOsWLFmADLT9GeVFQl4mhM84wSnyRJQdopMKEwyGtJM+RvM1AdB04t89/1O/w1cDnyilFU=")
# Channel secret
handler = WebhookHandler("ea4b5fdc1e16a04e83f9fb7e6897939f")