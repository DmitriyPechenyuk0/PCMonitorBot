import telebot, ctypes, pyautogui, os, time, dotenv, subprocess
from telebot import types
    
dotenv.load_dotenv()

TOKEN = str(os.getenv('TOKEN'))
MY_TELEGRAM = int(os.getenv('MY_TELEGRAM'))

bot = telebot.TeleBot(TOKEN)

alt_tab_reply = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=False)
alt_tab_reply.add(types.KeyboardButton('To previous tab'), types.KeyboardButton('To next tab'), types.KeyboardButton('Enter'))

def get_uptime():
    cmd = 'powershell -command "(get-date) - (gcim Win32_OperatingSystem).LastBootUpTime"'
    result = subprocess.check_output(cmd, shell=True, text=True)
    
    total_hours = None
    total_minutes = None

    for line in result.splitlines():
        if "TotalHours" in line:
            total_hours = line.split(":")[1].strip().replace(',', '.')
        elif "TotalMinutes" in line:
            total_minutes = line.split(":")[1].strip().replace(',', '.')

    if total_hours:
        return f"{total_hours} hours"
    elif total_minutes:
        return f"{total_minutes} minutes"
    else:
        return "Uptime not available"


@bot.message_handler(commands=['uptime'])
def uptime_command(message):
    if message.chat.id != MY_TELEGRAM:
        return
    uptime = get_uptime()
    bot.send_message(message.chat.id, f"PC uptime: {uptime.split(' ')[0].split('.')[0]} hours")


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
    os.remove(filepath)


@bot.message_handler(commands=['lock'])
def lock_command(message):
    if message.chat.id != MY_TELEGRAM:
        return
    bot.send_message(message.chat.id, "Blocked")
    ctypes.windll.user32.LockWorkStation()


@bot.message_handler(commands=['shutdown'])
def shutdown_command(message):
    if message.chat.id != MY_TELEGRAM:
        return
    bot.send_message(message.chat.id, "PC was shutdowned")
    os.system("shutdown /s /t 1")


@bot.message_handler(commands=['reboot'])
def shutdown_command(message):
    if message.chat.id != MY_TELEGRAM:
        return
    bot.send_message(message.chat.id, "PC reboots")
    os.system("shutdown /r /t 1")


@bot.message_handler(commands=['alttab'])
def alttab_command(message):
    if message.chat.id != MY_TELEGRAM:
        return
    
    pyautogui.keyDown('alt')
    pyautogui.keyDown('tab')
    pyautogui.keyUp('tab')
    screenshot = pyautogui.screenshot()

    filepath = f"screenshot_{int(time.time())}.png"

    screenshot.save(filepath)

    with open(filepath, 'rb') as photo:
        bot.send_photo(message.chat.id, photo)
    os.remove(filepath)
    bot.send_message(message.chat.id, "Tab selecter was active", reply_markup=alt_tab_reply)


@bot.message_handler(func=lambda message: message.text == 'To previous tab')
def to_previous_tab(message):
    pyautogui.keyDown('shift')
    pyautogui.keyDown('tab')
    pyautogui.keyUp('shift')
    pyautogui.keyUp('tab')
    screenshot = pyautogui.screenshot()
    filepath = f"screenshot_{int(time.time())}.png"

    screenshot.save(filepath)

    with open(filepath, 'rb') as photo:
        bot.send_photo(message.chat.id, photo)
    os.remove(filepath)
    bot.send_message(message.chat.id, "Tab was switched to previous", reply_markup=alt_tab_reply)
    

@bot.message_handler(func=lambda message: message.text == 'To next tab')
def to_previous_tab(message):
    pyautogui.keyDown('tab')
    pyautogui.keyUp('tab')
    screenshot = pyautogui.screenshot()
    filepath = f"screenshot_{int(time.time())}.png"

    screenshot.save(filepath)

    with open(filepath, 'rb') as photo:
        bot.send_photo(message.chat.id, photo)
    os.remove(filepath)
    bot.send_message(message.chat.id, "Tab was switched to next", reply_markup=alt_tab_reply)


@bot.message_handler(func=lambda message: message.text == 'Enter')
def to_previous_tab(message):
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')

    screenshot = pyautogui.screenshot()
    filepath = f"screenshot_{int(time.time())}.png"

    screenshot.save(filepath)

    with open(filepath, 'rb') as photo:
        bot.send_photo(message.chat.id, photo)
    os.remove(filepath)
    bot.send_message(message.chat.id, "Tab successfuly getted", reply_markup=types.ReplyKeyboardRemove())


commands = [
    types.BotCommand("/lock", "Win+L"),
    types.BotCommand("/shutdown", "Shutdown"),
    types.BotCommand("/reboot", "Reboot"),
    types.BotCommand("/uptime", "Working time"),
    types.BotCommand("/screenshot", "Screenshot"),
    types.BotCommand("/alttab", "Alt+tab to next application"),
]
bot.set_my_commands(commands)



bot.polling()
