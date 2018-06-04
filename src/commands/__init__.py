"""
в качестве микрооптимизации:
скорее всего классам команд лучше приделать метод exec вместо call(), надо проверить
"""


class BotCommand:

    def __init__(self, *args, **kwargs):
        # если нужно включаем логирование, безопасность, бенчмарки и т.д.
        print("Command args: ", args)
        print("Command kwargs: ", kwargs)
        self.bot = kwargs['bot']
        self.client = kwargs['client']
        self.msg = kwargs['message']
        pass

    def __call__(self, *args, **kwargs):
        print("=======")
        self.cmd = args[0]
        self.user = self.msg['from']['id']
        print("Command args: ", args)
        print("Command kwargs: ", kwargs)
        print(self.bot)


class RegWallet(BotCommand):
    """
    User registers wallet
    """

    def __init__(self, *args, **kwargs):
        super(RegWallet, self).__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        BotCommand.__call__(self, *args, **kwargs)
        address = self.cmd[1]
        return self.bot.set_user_address(self.user, address)


class Want(BotCommand):
    """
    User wants money
    """

    def __init__(self, *args, **kwargs):
        super(Want, self).__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        BotCommand.__call__(self, *args, **kwargs)
        amount = self.cmd[1]
        token = None
        if len(self.cmd) > 2:
            print(self.cmd)
            token = self.cmd[2]

            # def send_resource(self, user, token_id=None, amount=1):

        result = self.bot.send_resource(self.user, token, amount)
        return result


class Stat(BotCommand):
    """
    User wants statistics
    """

    def __init__(self, *args, **kwargs):
        super(Stat, self).__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        BotCommand.__call__(self, *args, **kwargs)


class NewAddress(BotCommand):
    """
    User gets new wallet (id, name)
    """

    def __init__(self, *args, **kwargs):
        super(NewAddress, self).__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        BotCommand.__call__(self, *args, **kwargs)


class SetDefaultWallet(BotCommand):
    """
    User sets default wallet (by name?)
    """

    def __init__(self, *args, **kwargs):
        super(SetDefaultWallet, self).__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        BotCommand.__call__(self, *args, **kwargs)


class RenameWallet(BotCommand):
    """
    User sets default wallet (by name?)
    """

    def __init__(self, *args, **kwargs):
        super(RenameWallet, self).__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        BotCommand.__call__(self, *args, **kwargs)


class Help(BotCommand):
    """
    User sets default wallet (by name?)
    """

    def __init__(self, *args, **kwargs):
        super(Help, self).__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        BotCommand.__call__(self, *args, **kwargs)
        return "<b>/help</b> - get help \n" \
               "<b>/reg ADDRESS</b> - register user's wallet \n" \
               "<b>/tokens</b> - get available TOKEN_ID(s)' \n" \
               "<b>/want AMOUNT</b> - recieve AMOUNT waves if available \n" \
               "<b>/want AMOUNT TOKEN_ID</b> - recieve AMOUNT of TOKEN_ID if available \n"


class Tokens(BotCommand):

    def __init__(self, *args, **kwargs):
        super(Tokens, self).__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        BotCommand.__call__(self, *args, **kwargs)
        return self.bot.get_asset_ids()
