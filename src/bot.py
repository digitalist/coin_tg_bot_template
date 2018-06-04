import pywaves as pw


class BotServer:
    """
    Bot-object has a big wallet and all in all is an awesome guy. Gives you money and all
    """

    def __init__(self, pk):
        pw.setNode(node='https://testnode1.wavesnodes.com', chain='testnet')  # connects to node

        # have Bot wallet address here, with a private key (enables us to send/issue tokens)
        self._wallet = pw.Address(privateKey=pk)

        # asset cache should store most used asset objects
        # maybe lru cache later
        self._asset_cache = []

        self.users = {
            # 'user': {'address' : 'string' }
        }

    def get_asset_ids(self):
        if not len(self._asset_cache):
            self._asset_cache = self._wallet.assets()

        return self._asset_cache

    def add_user(self, user):
        if user not in self.users:
            self.users[user] = {}

    def set_user_address(self, user, address):
        self.add_user(user)
        self.users[user]['address'] = address
        print('user address addded', self.users)
        return "Address added"

    def send_resource(self, user, token_id=None, amount=1):

        bot_wallet = self._wallet

        # waves are default
        if user not in self.users:
            print(self.users)
            return "Address is not registered. Use /reg VALID_ADDRESS"
        saved_address = self.users[user]['address']
        client_address = pw.Address(address=saved_address)
        result = None
        amount = int(amount)
        if not token_id:
            result = bot_wallet.sendWaves(client_address, amount)
        else:
            requested_token = pw.Asset(token_id)
            if requested_token:
                result = bot_wallet.sendAsset(recipient=client_address,
                                              asset=requested_token,
                                              amount=amount)
        return result
