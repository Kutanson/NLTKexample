import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk import FreqDist
from newspaper import Article,fulltext
import requests,string

new_stopwords=set(stopwords.words('turkish'))

url = 'https://www.indyturk.com//node/370856/dünya/dünya-genelinde-uluslararası-yayın-kuruluşlarının-internet-sitelerinde-çökme'

x = Article(url)
x.download()
x.parse()
metin =x.text

metindeki_kelimeler =word_tokenize(metin)  # metni kelimelere ayırır.
metindeki_cumleler =sent_tokenize(metin)   # metni cümlelere ayırır.


filtered_list =[]

for word in metindeki_kelimeler:
    if word.casefold() not in new_stopwords:
        filtered_list.append(word)
#metindeki stopwordsleri kaldırır.
filtered_list = [word for word in metindeki_kelimeler if word.casefold() not in new_stopwords ]
print(filtered_list)
stemmer = PorterStemmer()

stemmed_kelimeler =[stemmer.stem(word)for word in metindeki_kelimeler] #metindeki kelimeleri fiil tabanlı ayırma
print(stemmed_kelimeler)
lemmatizer = WordNetLemmatizer()

lemmatized_kelimeler =[lemmatizer.lemmatize(word)for word in metindeki_kelimeler]  # metindeki kelimeleri isim tabanlı ayırma
print(lemmatized_kelimeler)

print(nltk.pos_tag(metindeki_kelimeler)) #metindeki kelimeler sıfat, zamir gibi etiketlere ayırır.

grammar = "NP: {<DT>?<JJ>*<NN>}"
kelimeler_pos_tag = nltk.pos_tag(metindeki_kelimeler)
chunk_parser =nltk.RegexpParser(grammar)

tree = chunk_parser.parse(kelimeler_pos_tag)  #kelimeleri isim öbeklerine göre ayırır.
tree.draw()

en_cok_tekrar_edenler =FreqDist(metindeki_kelimeler)
en_cok_tekrar_edenler.most_common(10)  # metindeki kelimelerden en fazla tekrar eden 10 tanesini bulur.
print(en_cok_tekrar_edenler)
