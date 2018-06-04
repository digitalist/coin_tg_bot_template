class Client:
    """
    Client: receives money. Has stats, wallets. Can be stored in memory [cache] for active sessions
    """

    def __init__(self, address):

        pw.setNode(node='https://testnode1.wavesnodes.com', chain='testnet')  # connects to node

        # have Bot wallet address here, with a private key (enables us to send/issue tokens)
        self._wallet = pw.Address(privateKey=pk)

        # asset cache should store most used asset objects
        # maybe lru cache later
        self._asset_cache = []
