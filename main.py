from pyrogram import Client, filters
from pyrogram.errors import FloodWait

from time import sleep

app = Client("my_account")

# type
@app.on_message(filters.command("type", prefixes=".") & filters.me)
def type(_, msg):
    orig_text = msg.text.split(".type ", maxsplit=1)[1]
    text = orig_text
    tbr = ""
    typing_symbol = "▓"

    while(tbr != orig_text):
        try:
            msg.edit(tbr + typing_symbol)
            sleep(0.05)

            tbr = tbr + text[0]
            text = text[1:]

            msg.edit(tbr)
            sleep(0.05)

        except FloodWait as e:
            sleep(e.x)

app.run()