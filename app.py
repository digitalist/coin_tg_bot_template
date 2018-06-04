
import asyncio
import telepot
import logging

from aoiklivereload import LiveReloader
from src.commands.dispatcher import CommandDispatcher

from telepot.aio.loop import MessageLoop
from telepot.aio.delegate import pave_event_space, per_chat_id, create_open

import pywaves as pw
from src.bot import BotServer
from src.util import get_config
from config import CONFIG

reloader = LiveReloader()
reloader.start_watcher_thread()



def parse_message_text(msg):
    print(msg)
    if msg['entities'][0]['type'] != 'bot_command':
         return None

    text = msg['text'].split()
    if text[0][0] != "/":
        return None
    else:
        text[0] = text[0][1:].lower()

        return text


class MessageHandler(telepot.aio.helper.ChatHandler):

    def __init__(self, *args, **kwargs):
        super(MessageHandler, self).__init__(*args, **kwargs)
        self._count = 0
        self._cd = CommandDispatcher()
        self._bot = BotServer(get_config(CONFIG, 'waves_botPrivateKey'))

    async def on_chat_message(self, msg):
        self._count += 1
        print(msg)
        command_as_list = parse_message_text(msg)
        if command_as_list:
            command_result = self._cd.dispatch(command_as_list, self._bot, None, msg)
        else:
            command_result = 'Error: see /help'
        await self.sender.sendMessage(str(command_result), parse_mode='HTML')


TOKEN = get_config(CONFIG, 'telegram_token')

bot = telepot.aio.DelegatorBot(TOKEN, [
    pave_event_space()(
        per_chat_id(), create_open, MessageHandler, timeout=10),
])


loop = asyncio.get_event_loop()
loop.create_task(MessageLoop(bot).run_forever())
print('Listening ...')

loop.run_forever()
