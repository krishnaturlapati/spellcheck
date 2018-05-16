## Spell Check Python 

Objectives:
* SpellCheck should find misspelled words 
* SpellCheck should suggest possible/closet correct spelling 
* For input in text file SpellCheck should print the line number the word is misspelled 


English dictionary source: https://raw.githubusercontent.com/matthewreagan/WebstersEnglishDictionary/master/dictionary.json

Pickle words in dict 

```
>>> import pickle 
>>> import json
>>> data = open('dictionary.json', 'r').read()
>>> eng_words=json.loads(data).keys()
>>> eng_words_list=list(eng_words)
>>> with open('dictwords.pkl', 'wb') as the_file:
...     pickle.dump(eng_words_list, the_file)

```
