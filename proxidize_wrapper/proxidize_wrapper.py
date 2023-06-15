"""Main module."""

from requests import get
import time
from requests.auth import HTTPProxyAuth


class Proxy:
    def __init__(self, http_proxy, change_port, sock5_port=0) -> None:
        # accept in format of 1.1.1.1:1565:abc:xyz
        self.ip = http_proxy.split(":")[0]
        self.http_port = http_proxy.split(":")[1]
        self.username = http_proxy.split(":")[2]
        self.password = http_proxy.split(":")[3]
        self.proxy_ip = self.get_ip()
        self.sock5_port = sock5_port

        self.change_port = change_port

    def get_change_url(self):
        return f"http://{self.ip}:{self.change_port}/change_ip?t={self.username}{self.password}"

    def change_ip(self, delay=25):
        x = get(self.get_change_url())
        if "success" not in x.text.lower():
            raise ValueError("Invalid Credentials")
        time.sleep(delay)
        return self.get_ip() 

    def get_http_proxy(self):
        return f'http://{self.username}:{self.password}@{self.ip}:{self.http_port}'
    
    def get_sock5_proxy(self):
        return f'socks5://{self.username}:{self.password}@{self.ip}:{self.sock5_port}'
    
    def __str__(self) -> str:
        return self.get_http_proxy()
    
    def get_ip(self):
        proxies = {"http":f"http://{self.ip}:{self.http_port}"}
        auth = HTTPProxyAuth(self.username, self.password)
        print(proxies, auth)
        r = get('https://api.ipify.org/', proxies=proxies, auth=auth) 
        proxy_ip = r.text
        return proxy_ip 
        

if __name__ == "__main__":
    p = Proxy(input(), input())
    print(p.proxy_ip)
    print(p.change_ip())
    print(p.proxy_ip)