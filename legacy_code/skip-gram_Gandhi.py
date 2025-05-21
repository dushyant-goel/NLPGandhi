import pandas as pd
import matplotlib.pyplot as plt

import numpy as np
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
import re
import pandas as pd  
from time import time
from collections import defaultdict

import spacy
from gensim.models import Word2Vec
import logging  
logging.basicConfig(format="%(levelname)s - %(asctime)s: %(message)s", datefmt= '%H:%M:%S', level=logging.INFO)
from sklearn.manifold import TSNE
from numpy import dot
from numpy.linalg import norm

sent = []
for n in range(1,15):
	file = "../Data/Corpus_txt/mahatma-gandhi-collected-works-volume-" + str(n) + ".txt" 
	file_pointer = open(file,"r")
	file_text = file_pointer.read()
	sent.append(file_text.split())

# Train the gensim word2vec model with our own custom corpus
model = Word2Vec(sent, min_count=1, size=50, workers=3, window=3, sg=1)

print
print 
print

print "Words associated with corruption:"
print "Pre-1915"

similar = model.most_similar('corruption')

for a in similar:
	print a
print

sent = []
for n in range(15,62):
	file = "../Data/Corpus_txt/mahatma-gandhi-collected-works-volume-" + str(n) + ".txt"
	file_pointer = open(file,"r")
	file_text = file_pointer.read()
	sent.append(file_text.split())

# Train the gensim word2vec model with our own custom corpus
model = Word2Vec(sent, min_count=1, size=50, workers=3, window=3, sg=1)

print
print 
print

print "Words associated with corruption:"
print "1915-1934"

similar = model.most_similar('corruption')

for a in similar:
	print a
print

sent = []
for n in range(62,99):
	file = "../Data/Corpus_txt/mahatma-gandhi-collected-works-volume-" + str(n) + ".txt"
	file_pointer = open(file,"r")
	file_text = file_pointer.read()
	sent.append(file_text.split())

# Train the gensim word2vec model with our own custom corpus
model = Word2Vec(sent, min_count=1, size=50, workers=3, window=3, sg=1)

print
print 
print

print "Words associated with corruption:"
print "Post 1934"

similar = model.most_similar('corruption')

for a in similar:
	print a
print

