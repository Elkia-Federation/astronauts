# -*- coding: utf-8 -*-

'''
    read_essays.py

    This Python file can be used as a starting point for  
    teaching the computer to grade a school essay.
'''

# Don't worry about these 2 lines
from essays.en1 import essay_en1    
from essays.en2 import essay_en2

import nltk

essay_en1_tokens = nltk.word_tokenize(essay_en1)
essay_en2_tokens = nltk.word_tokenize(essay_en2)

"""                                                                                                  
    Expecting a string                                                                               
"""
def find_verbs(text):
    tokens = nltk.word_tokenize(text)
    tags = nltk.pos_tag(tokens)
    verbs = []
    for i in tags:
        if i[1][0:2] == 'VB':
            verbs.append(i)
    return verbs

"""                                                                                                  
    Expecting a string                                                                               
"""
def find_adverbs(text):
    tokens = nltk.word_tokenize(text)
    tags = nltk.pos_tag(tokens)
    adverbs = []
    for i in tags:
        if i[1][0:2] == 'RB':
            adverbs.append(i)
    return adverbs

"""                                                                                                  
    Expecting a string                                                                               
"""
def find_adjectives(text):
    tokens = nltk.word_tokenize(text)
    tags = nltk.pos_tag(tokens)
    adjectives = []
    for i in tags:
        if i[1][0:2] == 'JJ':
            adjectives.append(i)
    return adjectives

"""                                                                                                  
    Expecting a string                                                                               
"""
def find_nouns(text):
    tokens = nltk.word_tokenize(text)
    tags = nltk.pos_tag(tokens)
    nouns = []
    for i in tags:
        if i[1][0:2] == 'NN':
            nouns.append(i)
    return nouns

"""                                                                                                  
    Expecting a string                                                                               
"""
def evaluate_essay(essay):
    score = 0
    JJ_NN = len(find_adjectives(essay))/len(find_nouns(essay))
    RB_VB = len(find_adverbs(essay))/len(find_verbs(essay))
    score = (JJ_NN + RB_VB)/2
    return (score, JJ_NN, RB_VB)
    

print (evaluate_essay(essay_en1), evaluate_essay(essay_en2))

#if "really cool" in essay_en1:
#    print("The phrase 'really cool' appears in Essay 1.")
#else:
#    print("The phrase 'really cool' was NOT found.")
