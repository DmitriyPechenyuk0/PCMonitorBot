Telegram Remote Control Bot

This bot lets you control your Windows PC remotely through Telegram:

- Take screenshots of your current screen and get them sent right in the chat
- Lock your computer screen (like pressing Win + L)
- Shut down your PC remotely

---

Why did I create this?

Sometimes you need quick access to your PC or want to perform simple commands without sitting in front of it. This bot lets you do that easily via Telegram from anywhere.

---

How to use

1. Create a bot on Telegram using @BotFather and get your bot token
2. Insert your bot token and your Telegram chat_id in the bot_script.py file
3. Make sure Python is installed and install required libraries:

pip install pyTelegramBotAPI pyautogui

4. Run the bot script:

python main.py

5. Send commands to your bot in Telegram:

Command     - Description
/screenshot - Takes a screenshot of your PC  
/lock       - Locks the screen (Win + L)  
/shutdown   - Shuts down your computer  

Important notes

- Never share your bot token or chat_id with others
- Run the bot on your PC which must be online for it to respond
- The bot only responds to messages from the authorized chat_id for security

---