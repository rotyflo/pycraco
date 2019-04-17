import words

my_string = "Okay, let's see if we can count the amount of words in this string"
amount_of_words = words.count_words(my_string)

print(amount_of_words)

"""
import words
words.word_count()

from words import word_count
word_count()

from words import word_count as wc
wc()

import words as w
w.word_count()

# AVOID THIS STYLE TO PREVENT ISSUES
from words import *
word_count()
"""
