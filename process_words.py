import nltk

words = nltk.corpus.words.words()

word_set = set()
for w in words:
	w = w.lower()
	if w.isalpha():
		word_set.add(w)

lengths = [3,4,5,6,7,8,9,10]

#Easy mode words
for l in lengths:
	words_l = [w for w in word_set if len(w)==l and len(set(w))==l]
	words_l.sort()
	with open(f'words/easy_words_{l}.txt','w') as f:
		f.write('\n'.join(words_l))

#Hard mode words
for l in lengths:
	words_l = [w for w in word_set if len(w)==l]
	words_l.sort()
	with open(f'words/hard_words_{l}.txt','w') as f:
		f.write('\n'.join(words_l))