'''
from collections import Counter
def char_freq(s):
    return dict(Counter(s))
print(char_freq("anurag"))
'''
def char_freq(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq
print(char_freq("banana"))