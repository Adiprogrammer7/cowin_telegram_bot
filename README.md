# cowin_telegram_bot 
A simple slot notifier for vaccine availability on COWIN platform of India. Here, we used official cowin api to access information about available slots and telegram api to notify
us in realtime via our own telegram bot.   

First we need to create our bot from telegram app. We will use **BotFather** which is an official telegram bot to create and manage bots. Refer this small article for "How to Create a New Bot for Telegram": ```https://sendpulse.com/knowledge-base/chatbot/create-telegram-chatbot```

Once, you get your token for bot, copy that token and you are good to move on. Now search for your bot in the search menu of app with the name given by you for your bot. Then start
your bot and enter ```/my_id```

![image](https://user-images.githubusercontent.com/30752980/122887010-148b6b80-d35e-11eb-9123-71b64405ef5f.png)

Now, visit ```https://api.telegram.org/bot<bot_token>/getUpdates``` in your browser where ```<bot_token>``` should be token that we copied earlier for our telegram bot. Now, look
for 'chat id' and copy that id too. ( refer https://stackoverflow.com/questions/32423837/telegram-bot-how-to-get-a-group-chat-id/38388851#38388851)

Once we get our token and chat id we are good to go. Replace 'telegram_key' and 'telegram_chat_id' variables in ``bot.py`` with token and chat id respectively. For the first time, you will need to set location, run ```set_location.py```. Corresponding district id will be stored in ```location.txt```. Now you can let ```bot.py``` run in background and whenever conditions are met, you will be notified on telegram app(consider modifying the conditions in if/else statements to customize based on your preference)

![2](https://user-images.githubusercontent.com/30752980/122889657-9aa8b180-d360-11eb-827a-de5692d09454.jpg)


**NOTE: Requests made from countries outside India are forbidden by Cowin api.**
