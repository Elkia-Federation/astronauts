# -*- coding: utf-8 -*-

'''
    read_essays.py

    This Python file can be used as a starting point for
    teaching the computer to grade a school essay.
'''

# Don't worry about these 2 lines
from essays.en1 import essay_en1
from essays.en2 import essay_en2
from textblob import TextBlob

essay1 = TextBlob(essay_en1)
essay2 = TextBlob(essay_en2)

if essay1.sentiment.polarity > essay2.sentiment.polarity:
    print("essay 1 wins")
else: print ("essay 2 wins")
print(essay1.sentiment)
print(essay2.sentiment)
