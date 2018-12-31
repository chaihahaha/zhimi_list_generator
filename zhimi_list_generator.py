import sys
import re
f = open(sys.argv[1])
text = f.read()
words = re.findall('\w+', text.lower())
uniq_words = set(words)
w = open(sys.argv[2],'w')
for i in uniq_words:
	if len(i) > 3 and not any(char.isdigit() for char in i):
		w.write(i)
		w.write('\n')
f.close()
w.close()
