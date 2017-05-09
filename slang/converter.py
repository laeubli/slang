#!/usr/bin/env python3

import random

def convert(sentence):
    """Converts a Swiss German sentence into slang xD"""
    # all lower case
    sentence = sentence.lower()
    # fancy people shriibed so
    sentence = sentence.replace("sch", "sh")
    # remove whitespace and regular punctuation at end of sentence
    while sentence[-1] in ' .!?':
        sentence = sentence[:-1]
    # append random stuff to end of sentence
    sentence += random.choice([' xD', '!!!', '!?!?!?', ' 🤓 ', ' 😎 ', ' 💩 ', ', alte?!'])
    return sentence
