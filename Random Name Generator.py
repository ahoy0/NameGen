import os
import urllib.request
import numpy as np
import time

def name_generator():
    dictionary = "https://raw.githubusercontent.com/dwyl/english-words/master/words.txt"
    response = urllib.request.urlopen(dictionary)
    long_txt = response.read().decode()
    words = long_txt.splitlines()
    var1 = np.random.randint(1, high=466550)
    var2 = np.random.randint(1, high=466550)
    return print(words[var1], words[var2]), time.sleep(1)

while True:
    name_generator()
