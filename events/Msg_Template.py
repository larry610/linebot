from line_bot_api import *

def stock_reply_other(stockNumber):
    content_text = "及時股價和K線圖"
    text_message = TextSendMessage(
                                text = content_text , 
                                quick_reply = QuickReply(
                                    items = [
                                        QuickReplyButton(
                                                action = MessageAction(
                                                    label = "即時股價" , 
                                                    text = "#" + stockNumber , 
                                                )   
                                        ) ,
                                        QuickReplyButton (
                                                action = MessageAction(
                                                    label = "K線圖" , 
                                                    text = "@K" + stockNumber
                                                )
                                        ),
                                    ]
                                ))
    return text_message


# 幣別種類Button
def show_Button(user_id):
    flex_message = FlexSendMessage(
            alt_text="指標選股",
            contents={
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "指標選股",
        "weight": "bold",
        "size": "xl",
        "color": "#04B2D9"
      }
    ],
    "backgroundColor": "#CEECF2"
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "上市",
        "size": "xl",
        "color": "#15BFBF",
        "weight": "bold"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "postback",
              "label": "本益比",
              "data": f"action=button_clicked&data=PE&userID={user_id}"
            },
            "gravity": "center",
            "style": "primary",
            "color": "#04C4D9",
            "margin": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "postback",
              "label": "殖利率",
              "data": f"action=button_clicked&data=DY&userID={user_id}"
            },
            "gravity": "center",
            "style": "primary",
            "color": "#04C4D9",
            "margin": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "postback",
              "label": "淨值比",
              "data": f"action=button_clicked&data=PB&userID={user_id}"
            },
            "gravity": "center",
            "style": "primary",
            "color": "#04C4D9",
            "margin": "sm"
          }
        ]
      },
      {
        "type": "separator",
        "margin": "md",
        "color": "#D9D0C7"
      },
      {
        "type": "text",
        "text": "上櫃",
        "color": "#15BFBF",
        "weight": "bold",
        "size": "xl"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "postback",
              "label": "本益比",
              "data": f"action=button_clicked&data=PE2&userID={user_id}"
            },
            "gravity": "center",
            "style": "primary",
            "color": "#04C4D9",
            "margin": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "postback",
              "label": "殖利率",
              "data": f"action=button_clicked&data=DY2&userID={user_id}"
            },
            "gravity": "center",
            "style": "primary",
            "color": "#04C4D9",
            "margin": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "postback",
              "label": "淨值比",
              "data": f"action=button_clicked&data=PB2&userID={user_id}"
            },
            "gravity": "center",
            "style": "primary",
            "color": "#04C4D9",
            "margin": "sm"
          }
        ]
      }
    ],
    "backgroundColor": "#CEECF2"
  },
  "styles": {
    "header": {
      "backgroundColor": "#CEECF2"
    }
  }
}
                    
    )
    return flex_message