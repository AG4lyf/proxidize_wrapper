"""Main module."""

from requests import get
import time

class Proxy:
    def __init__(self, arg) -> None:
        # accept in format of 1.1.1.1:1565:abc:xyz
        self.ip = arg.split(":")[0]
        self.port = arg.split(":")[1]
        self.username = arg.split(":")[2]
        self.password = arg.split(":")[3]
    
    def get_proxy(self):
        return f"{self.ip}:{self.port}:{self.username}:{self.password}"
    
    def change_ip(self):
        try:
            address = f"http://{self.ip}:{self.port}/change_ip?t={self.username}{self.password}"
            print(address)
            x = get(address)
        except Exception as e:
            raise e
        if "success" not in x.text.lower():
            raise ValueError("Invalid credentials")
        
        tries = 10
        d = ""
        while True:
            try:
                d = self.get_ip()
            except Exception as e:
                tries -= 1
                time.sleep(3)
                if tries == 0:
                    raise e
            else:
                return d
            
    def get_ip(self):
        return get("https://api.ipify.org/", timeout=1).text
