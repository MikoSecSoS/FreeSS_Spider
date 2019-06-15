#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime

import requests
import re

class FreeSSR:

    def __init__(self):
        self.header = {
            "user-agent": "Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36"
        }
        self.url = "https://www.youneed.win/free-ssr"
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
                                "<td align=\"center\"><a href=\"(.*?)\">.*?</a></td>\n"
                                "</tr>", req.text)
        print(data_list)
        for ip, port, passwd, crypton, protocol, confuse, link in data_list:
            yield {
                "IP": ip,
                "Port": port,
                "Password": passwd,
                "Crypton": crypton,
                "Protocol": protocol,
                "Confuse": confuse,
                "Link": link,
            }

    @staticmethod
    def decode(n, c):
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
        self.download(self, self.time+" FreeSSR.txt", data)

if __name__ == "__main__":
    Free_ssr = FreeSSR()
    Free_ssr.main()