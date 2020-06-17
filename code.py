from google.colab import files
uploaded = files.upload()
#reading file:
filename = "d2.txt"
file = open(filename, 'rt')
text = file.read()
print(text)
#!pip install -U spacy
#!python -m spacy download en_core_web_sm 
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
stopwords = list(STOP_WORDS)
# stopwords
nlp = spacy.load('en_core_web_sm')
doc=nlp(text)
tokens = [token.text for token in doc]
print(tokens)
punctuation = punctuation
punctuation
word_frequencies = {}
for word in doc:
  if word.text.lower() not in stopwords:
    if word.text.lower() not in punctuation:
      if word.text not in word_frequencies.keys():
        word_frequencies[word.text] = 1
      else:
          word_frequencies[word.text] += 1
word_frequencies
max_frequency = max(word_frequencies.values())
max_frequency
for word in word_frequencies.keys():
  word_frequencies[word] = word_frequencies[word]/max_frequency
 print(word_frequencies)
sentence_tokens = [sent for sent in doc.sents]
print(sentence_tokens)
sentence_scores = {}
for sent in sentence_tokens:
  for word in sent:
    if word.text.lower() in word_frequencies.keys():
      if sent not in sentence_scores.keys():
        sentence_scores[sent] = word_frequencies[word.text.lower()]
      else:
         sentence_scores[sent] += word_frequencies[word.text.lower()]
sentence_scores
from heapq import nlargest
select_length = int(len(sentence_tokens)*0.3)
select_length
summary = nlargest(select_length,sentence_scores,key=sentence_scores.get)
summary
 final_summary = [word.text for word in summary]
 summary = '\n=> '.join(final_summary)
 print("=>",summary)

