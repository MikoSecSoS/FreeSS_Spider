#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime

import requests
import re

class FreeSS:

    def __init__(self):
        self.header = {
            "user-agent": "Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36"
        }
        self.url = "https://www.youneed.win/free-ss"
        self.time = datetime.datetime.now().strftime("%Y-%m-%d")

    @staticmethod
    def get_data(self, url):
        req = requests.get(url, headers=self.header)
        data_list = re.findall( "<tr>\n"
                                "<td align=\"center\">(.*?)</td>\n"
                                "<td align=\"center\">(.*?)</td>\n"
                                "<td align=\"center\">(.*?)</td>\n"
                                "<td align=\"center\">(.*?)</td>\n"
                                "<td align=\"center\">(.*?)</td>\n"
                                "<td align=\"center\">(.*?)</td>\n"
                                "</tr>", req.text)
        for ip, port, passwd, crypton, time, county in data_list:
            if "data-cfemail=" in passwd:
                data_cfemail = re.findall('data-cfemail="(.*?)">', passwd)
                passwd = self.decode(data_cfemail[0], 0) + passwd[passwd.index("</a>")+4:]
            yield {
                "IP": ip,
                "Port": port,
                "Password": passwd,
                "Crypton": crypton,
                "Time": time,
                "County": county,
            }

    @staticmethod
    def decode(n, c):
        # https://www.youneed.win/cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js
        return "".join([chr(int(n[i:i+2], 16)^int(n[c:c+2], 16)) for i in range (2, len(n), 2)])

    @staticmethod
    def download(self, filename, data):
        with open(filename, "w+") as f:
            for data_dict in self.get_data(self, self.url):
                print(data_dict)
                f.write(str(data_dict)[1:-2]+"\n")
                f.flush()

    def main(self):
        data = self.get_data(self, self.url)
        self.download(self, self.time+" FreeSS.txt", data)

if __name__ == "__main__":
    Free_SS = FreeSS()
    Free_SS.main()
