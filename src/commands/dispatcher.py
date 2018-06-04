from src.commands import *


class CommandDispatcher:
    def __init__(self):
        self._command_map = {
            'want': Want,
            'help': Help,
            'tokens': Tokens,
            'reg': RegWallet,
        }
        pass

    def dispatch(self, command_as_list, bot, client, full_message):
        cmd = command_as_list[0]

        if cmd not in self._command_map:
            return
        if self._command_map[cmd]:

            """
            strip first command and init command object with arguments [cache, throttling, etc]
            """

            print(self._command_map[cmd])

            command = self._command_map[cmd](bot=bot, client=client, message=full_message)

            # call it
            return command(command_as_list, bot=bot, client=client)
        else:
            print("wrong command")
            return ""
