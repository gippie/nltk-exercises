import nltk

nltk.corpus.gutenberg.fileids()

from nltk.corpus import gutenberg

for fileid in gutenberg.fileids():
    num_chars = len(gutenberg.raw(fileid))
    num_words = len(gutenberg.words(fileid))
    num_sents = len(gutenberg.sents(fileid))
    num_vocab = len(set(w.lower() for w in gutenberg.words(fileid)))
    print(round(num_chars/num_words), round(num_words/num_sents), round(num_words/num_vocab), fileid)   #lunghezza media parola, lunghezza media frase, quante volte appare una parola nel testo in media

macbeth_sentences = gutenberg.sents('shakespeare-macbeth.txt')  #sents divide il testo in frasi
macbeth_sentences
macbeth_sentences[1116]
longest_len = max(len(s) for s in macbeth_sentences)
[s for s in macbeth_sentences if len(s) == longest_len] #cerco la frase più lunga nel testo

from nltk.corpus import webtext
for fileid in webtext.fileids():
    print(fileid, webtext.raw(fileid)[:65], '...')

from nltk.corpus import nps_chat
chatroom = nps_chat.posts('10-19-20s_706posts.xml')
chatroom[123]

from nltk.corpus import brown
brown.categories()
brown.words(categories='news')
brown.words(fileids=['cg22'])
brown.sents(categories=['news', 'editorial', 'reviews'])

news_text = brown.words(categories='news')
fdist = nltk.FreqDist(w.lower() for w in news_text)
modals = ['can', 'could', 'may', 'might', 'must', 'will'] #definisco verbi modali per comparare quanto vengono usati in diversi generi
for m in modals:
    print(m + ':', fdist[m], end=' ') #scrivo end per mantenere tutto in linea

mystery_text = brown.words(categories='mystery') #esercizio proposto, cerco le parole wh nella categoria mystery
fdist_m = nltk.FreqDist(w.lower() for w in mystery_text)
wh_words = ['what', 'when', 'why', 'where', 'who']
for w in wh_words:
    print(w + ':', fdist_m[w], end=' ')
    
cfd = nltk.ConditionalFreqDist(
          (genre, word)
          for genre in brown.categories()
          for word in brown.words(categories=genre))
genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
modals = ['can', 'could', 'may', 'might', 'must', 'will']
cfd.tabulate(conditions=genres, samples=modals) #comparo le varie categorie usando il supporto integrato di NLTK per le conditional frequency distributions