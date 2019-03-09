from bs4 import BeautifulSoup
import requests

#to do:
def format_html():
    pass

page_link = 'https://data.rada.gov.ua/ogd/zal/agenda/skl8/sten/20141127-1.htm'

page_response = requests.get(page_link, timeout=5)
page_content = BeautifulSoup(page_response.content, "html.parser")

textContent = []
for i in range(0, len(page_content.find_all("p", attrs={"align": None}))):
    paragraphs = page_content.find_all("p", attrs={"align": None})[i].text
    textContent.append(paragraphs)
print(textContent)
