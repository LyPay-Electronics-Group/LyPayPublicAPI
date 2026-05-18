from ssl import create_default_context as ssl_create_default_context, CERT_NONE
from os import getenv
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent / '.env')

class CONFIGURATION:
    PROXY = getenv("LYPAY_CORE_PROXY")
    TOKEN = getenv("LYPAY_CORE_TOKEN") if getenv("LYPAY_CORE_TOKEN") != '' else None

    SSL = ssl_create_default_context()
    SSL.check_hostname = False
    SSL.verify_mode = CERT_NONE

    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Referer': 'https://google.com'
    }


VERSION = "v2.6.1p"
NAME = "Public API"
BUILD = 21.1
