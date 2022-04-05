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