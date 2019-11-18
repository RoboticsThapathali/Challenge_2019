#solution by Pukar 

import requests as rq
import re
import os

data = {}
with open("wordlist.txt", "r") as infile:
    for word in infile.readlines():
        word = word.strip()
        key = "".join(sorted(word))
        data.update({key: word})

requests = rq.session()
url_string = "http://secretmsg.6te.net/chpage.php"
strings = requests.get(url_string).text
words = re.findall('<li>+(.*?)</li>', strings)
ans = "{ "
for word in words:
    ans = ans+data["".join(sorted(word.strip()))]+" "
ans += "}"
submission = {
    "ans": ans,
    "name": "Pukar Giri",
    "roll": "THA074BEX025"
}
page = requests.post("http://secretmsg.6te.net/result.php", data=submission)
with open("result.html", "w") as outfile:
    outfile.write(page.text)

file_path = os.path.join(os.getcwd(), "result.html")
os.system("google-chrome '"+file_path+"'")
