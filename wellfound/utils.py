# import requests
from enum import Enum
# from bs4 import BeautifulSoup
# import sys
# import time


try:
    from urllib import urlencode, urlunsplit
except ImportError:
    from urllib.parse import urlunsplit, urlencode


class Base(str, Enum):
    URL = "https://wellfound.com"

    def __str__(self):
        return str(self.value)


class Header(str, Enum):
    PAYLOAD = {"Content-Type": "text/html; charset=UTF-8"}

    def __str__(self):
        return str(self.value)

# class LoginURL(object):
#     URL = "/login"

#     def __str__(self):
#         return str(self.URL)

def check_login_status(self):
    """Checks if the user is logged in."""
    # self.driver.get(f"{Base.URL}/jobs")

    if self.driver.current_url == f"{Base.URL}/jobs":
        return True
    # return self.wait_for_login_to_complete()
    return False



print(Base.URL)
print(Header.PAYLOAD)
