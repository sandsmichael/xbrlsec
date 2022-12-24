from bs4 import BeautifulSoup
import requests
import sys

header = {
"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
"X-Requested-With": "XMLHttpRequest"
}

class Instance():

    def __init__(self, url):
        self.url = url

        # self.response = requests.get(self.url, headers=header).text
        # with open('./output.xml', 'w') as file:
        #     file.write(self.response)

        with open('./output.xml', 'r') as file:
            self.response = file.read()

        soup = BeautifulSoup(self.response, features='xml')

        # print([tag.name for tag in soup.find_all()])
        for tag in soup.find_all():
            if tag.name == "InventoryNet":
                print(tag['contextRef'])
                print(tag['contextRef'].split('_')[-1])
                print(tag.text)




Instance( url = "https://www.sec.gov/Archives/edgar/data/1018724/000101872422000023/amzn-20220930_htm.xml" )