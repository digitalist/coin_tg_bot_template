import os
CONFIG = {
        'telegram': {
            'token': os.getenv('telegram_token', None)
        },
        'waves': {
            'chain': 'testnet',
            'node': 'https://testnode1.wavesnodes.com',
            'botPrivateKey': os.getenv('waves_private_key', None)
        }
}
