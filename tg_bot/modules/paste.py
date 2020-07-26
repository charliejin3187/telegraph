from typing import List

import requests
from telegram import Update, Bot, ParseMode
from telegram.ext import run_async

from tg_bot import dispatcher
from tg_bot.modules.disable import DisableAbleCommandHandler


@run_async
def paste(bot: Bot, update: Update, args: List[str]):
    message = update.effective_message

    if message.reply_to_message:
        data = message.reply_to_message.text

    elif len(args) >= 1:
        data = message.text.split(None, 1)[1]

    else:
        message.reply_text(("""*○ My Name* : `Google Lens`
*○ Creator* : [Charlie_jin](https://t.me/charlie_jin)
*○ Credits* : `Everyone in this journey`
*○ Language* : `Python3`
*○ Library* : [Pyrogram asyncio 0.16.1](https://docs.pyrogram.org/)
*○ Source Code* : [👉Click Here](https://t.me/nokkiirunnoippokittum)
*○ Server* : `Heroku`
*○ Build Status* : `V2 [+0.4]` """), parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)
        return

    key = requests.post('https://nekobin.com/api/documents', json={"content": data}).json().get('result').get('key')

    url = f'https://nekobin.com/{key}'

    reply_text = f'Nekofied to *Nekobin* : {url}'

    message.reply_text(reply_text, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)



PASTE_HANDLER = DisableAbleCommandHandler("about", paste, pass_args=True)
dispatcher.add_handler(PASTE_HANDLER)


__command_list__ = ["paste"]
__handlers__ = [PASTE_HANDLER]
