## Requirements 
#### pip install pyTelegramBotAPI
#### pip install APScheduler
## How to install 
1. You need to set the bot token in the senderBot.py and run the program.
   
   ![image](https://github.com/TEGTO/TelegramBotSender/assets/90476119/96641fb8-40df-49f3-bd55-b1ade9420a0c)
2. Send */help* or */start* to your bot in Telegram.

### Buttons
If installation correct bot will show you these buttons:

![image](https://github.com/TEGTO/TelegramBotSender/assets/90476119/d7fb91b3-b047-4c41-80ee-4b6f0f63fd30)

**Set Message Content** - button to set content of bot sending message. After clicking, the bot will ask you to send a content, it can be *image, video or text.*

![image](https://github.com/TEGTO/TelegramBotSender/assets/90476119/00ecdf37-97cb-4f1c-8b9a-c938eb340cb6)


**Send Message** - button to send the message immediately. After clicking, the bot will ask you message information type of *"Chat Id||Amount of messages".*

![image](https://github.com/TEGTO/TelegramBotSender/assets/90476119/3220cd84-6436-4f42-b75d-2ee70d8aed5e)

> **Chat Id** - id of the chat you want to the bot to send the message.

> **Amount of messages** - how many messages the bot will send per time.

> ***Example: 1111111||5***

**Send Delayed Message** - button to send the message per 24 hours for a few days. After clicking, the bot will ask you message information type of *"Chat Id||Amount of messages||11:20||Amount of days"*

![image](https://github.com/TEGTO/TelegramBotSender/assets/90476119/07a74882-234a-4925-878a-0484360b7966)


> **11:20** - it's time when the bot will send the message at day. Use the format **hours:minutes** to set the time.

>  **Amount of days** - how many days the bot will send the message, 1 means only one day (include today).

> ***Example: 1111111||5||5:20||10***

> ##### Don't forget the split symbol (default is ||), it's important).

##### Bots in Telegram can't send any messages first, users need to start a conversation with the bot themselves. But, bots can send send messages to a group chat.
