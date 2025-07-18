import telebot, ctypes, pyautogui, os, time, dotenv

dotenv.load_dotenv()

TOKEN = os.getenv('TOKEN')
MY_TELEGRAM = os.getenv('MY_TELEGRAM')

bot = telebot.TeleBot(TOKEN)

def lock_screen():
    ctypes.windll.user32.LockWorkStation()

def shutdown_pc():
    os.system("shutdown /s /t 1")

@bot.message_handler(commands=['start'])
def start(message):
    if message.chat.id != MY_TELEGRAM:
        return

@bot.message_handler(commands=['screenshot'])
def send_screenshot(message):
    if message.chat.id != MY_TELEGRAM:
        return
    screenshot = pyautogui.screenshot()

    filepath = f"screenshot_{int(time.time())}.png"

    screenshot.save(filepath)

    with open(filepath, 'rb') as photo:
        bot.send_photo(message.chat.id, photo)

@bot.message_handler(commands=['lock'])
def lock_command(message):
    if message.chat.id != MY_TELEGRAM:
        return
    bot.send_message(message.chat.id, "Blocked")
    lock_screen()

@bot.message_handler(commands=['shutdown'])
def shutdown_command(message):
    if message.chat.id != MY_TELEGRAM:
        return
    bot.send_message(message.chat.id, "PC was shutdowned")
    shutdown_pc()

from telebot import types
commands = [
    types.BotCommand("/screenshot", "Screenshot"),
    types.BotCommand("/lock", "Win+L"),
    types.BotCommand("/shutdown", "Shutdown"),
]

bot.set_my_commands(commands)

bot.polling()
