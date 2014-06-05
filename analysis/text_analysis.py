import requests
import lxml.html
from textblob import TextBlob

r = requests.get("htttps://www.google.com/")
html = lxml.html.fromstring(r.text)
obj = html.xpath("//p")

text = [elem.text_content() for elem in obj]
ave_happiness = 0
for i in text:
    text_obj = TextBlob(i)
    ave_happiness += text_obj.sentiment.polarity
print text[0].sentiment.polarity
#print ave_happiness /= float(len(text))


