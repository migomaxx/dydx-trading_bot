from dydx3.constants import API_HOST_GOERLI, API_HOST_MAINNET
from decouple import config

# !!! SELECT MODE !!!

MODE = "PRODUCTION" #Production(mainnet)

TOKEN_FACTOR_10 = ["XLM-USD","DOGE-USD","TRX-USD",]

#Close all positions and orders
ABORT_ALL_POSITIONS = False


FIND_COINTEGRATED = True

#Place Trades
PLACE_TRADES = True

MANAGE_EXITS = True

#Resolution
RESOLUTION = "1HOUR"

#Stats Window
WINDOW = 21 #MA

#Thresholds - Opening trade
MAX_HALF_LIFE = 24
ZSCORE_THRESH = 1.5 #попробуй выше поставить
USD_PER_TRADE = 10
USD_MIN_COLLATERAL = 150 #?????

#Thresholds - Closing
CLOSE_AT_ZSCORE_CROSS = True

#Ethereum address
ETHEREUM_ADDRESS = "0x3E672E408c38a71B35E5d876e9d35BbAe9815338"

#KEYS - Production
#Must to be on MAINNET DYDX
STARK_PRIVATE_KEY_MAINNET = config("STARK_PRIVATE_KEY_MAINNET")
DYDX_API_KEY_MAINNET = config("DYDX_API_KEY_MAINNET")
DYDX_API_SECRET_MAINNET = config("DYDX_API_SECRET_MAINNET")
DYDX_API_PASSPHRASE_MAINNET = config("DYDX_API_PASSPHRASE_MAINNET")

#KEYS - Development
#Must to be on TESTNET DYDX
STARK_PRIVATE_KEY_TESTNET = config("STARK_PRIVATE_KEY_TESTNET")
DYDX_API_KEY_TESTNET = config("DYDX_API_KEY_TESTNET")
DYDX_API_SECRET_TESTNET = config("DYDX_API_SECRET_TESTNET")
DYDX_API_PASSPHRASE_TESTNET = config("DYDX_API_PASSPHRASE_TESTNET")

#KEYS - Export
STARK_PRIVATE_KEY = STARK_PRIVATE_KEY_MAINNET if MODE =="PRODUCTION" else STARK_PRIVATE_KEY_TESTNET
DYDX_API_KEY = DYDX_API_KEY_MAINNET if MODE =="PRODUCTION" else DYDX_API_KEY_TESTNET
DYDX_API_SECRET = DYDX_API_SECRET_MAINNET if MODE =="PRODUCTION" else DYDX_API_SECRET_TESTNET
DYDX_API_PASSPHRASE = DYDX_API_PASSPHRASE_MAINNET if MODE =="PRODUCTION" else DYDX_API_PASSPHRASE_TESTNET

#HOst - Export
HOST = API_HOST_MAINNET if MODE =="PRODUCTION" else API_HOST_GOERLI

#HTTP Provider

HTTP_PROVIDER_MAINNET = "https://eth-mainnet.g.alchemy.com/v2/Zq_snQHViqhzEew3DRpHjqBrEnqy47ES"
HTTP_PROVIDER_TESTNET = "https://eth-goerli.g.alchemy.com/v2/oDH5uTCs6o5lalQXzsiRcg8jZsO-Sema"
HTTP_PROVIDER = HTTP_PROVIDER_MAINNET if MODE =="PRODUCTION" else HTTP_PROVIDER_TESTNET

