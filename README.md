# Api-Miku-says
Api to get inspiring random `Quotes` and random `Topics` to talk about

content Contributions are always welcomed

Quotes:
```py
import requests,json

r = requests.get('https://miku-says.benzene002.repl.co/quote')
quote = json.loads(r.text)
print(quote)

print(quote['author'])
print(quote['quote'])
```
```console
>>{'author': 'Charlie Chaplin', 'quote': 'The deeper the truth in a creative work, the longer it will live.  '}
>>Charlie Chaplin
>>The deeper the truth in a creative work, the longer it will live. 
```

Topics:

```py
import requests,json

r = requests.get('https://miku-says.benzene002.repl.co/topic')
topic = json.loads(r.text)
print(topic)
```
```console
>>Do you think that VR (virtual reality) will become mainstream in the near future?
```
