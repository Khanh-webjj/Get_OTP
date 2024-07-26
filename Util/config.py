# config.py

# API configuration

# api form: API_URL_MAIN_TEMPLATE + API_MODE +"/"+ brandName +"/"+ acount +"/"+ API_KEY
# exp: http://api.happyfarm.click/api/get-msisdn/msverify/CanTest_gw/nfpheeadlmdgdovoupzbmiquzk
API_URL_MAIN_TEMPLATE = "http://api.happyfarm.click/api"

API_GET_MSISDN_MODE = "get-msisdn"
API_GET_OTP_MODE = "get-otp"

API_KEY = "nfpheeadlmdgdovoupzbmiquzk"
# nfpheeadlmdgdovoupzbmiquzk

TIMEOUT = 30  # Timeout in seconds

BRAND_NAME = {
    "TIKTOK" : 'tiktok',
    "AIRBNB" : 'airbnb',
    "SHEIN" : 'shein',
    "ALIBABA" : 'alibaba',
    "TIKTOKADS" : 'tiktokads',
    "AMAZON" : 'amazon',
    "TINDER" : 'tinder',
    "PINTEREST" : 'pinterest',
}

# Database configuration Mongodb
DB_HOST = "localhost"
DB_PORT = 27017
DB_USER = ""
DB_PASSWORD = "your_password"
DB_NAME = "your_database_name"

# Other configurations
DEBUG_MODE = True

PROXY = "88.209.207.107:50100"
