import requests
from bs4 import BeautifulSoup

URL = "https://www.lovepanky.com/flirting-flings/get-flirty/flirty-text-messages-that-are-sure-to-make-her-smile"
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
result = []
for p in soup.find_all('p'):
    text = " ".join(p.text.split())
    result.append(text)

#print(len(result))
#for i in range(0, len(result)):
#    print(len(result[i]))
#    print(i)

text_file  = open("quotes.txt","w", encoding="utf-8")
for i in range(0, len(result)):
    for j in range(0, len(result[i])):
        if result[i][j] == "#":
            text_file.write(result[i][3:])
            text_file.write("\n")
text_file.close()
