'''
Word Frequency Counter:
   sentence = "the cat sat on the mat the cat"
   - প্রতিটা word কতবার আছে dict এ রাখো
   - সবচেয়ে বেশিবার আসা word টা বের করো
'''
sentence = "the cat sat on the mat the cat"
words = sentence.split()

freq={}
for word in words:
    freq[word]= freq.get(word,0)+1

# highest freq word
highest_freq = max (freq, key=freq.get)
print(f"Most frequent word '{highest_freq}' comes with {freq[highest_freq]} times ")