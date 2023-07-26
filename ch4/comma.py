def comma(lst):
	s = ''
	for i, it in enumerate(lst):
		if(i == len(lst)-1):
			s += 'and ' + it
		else:
			s += it + ', '
	return s

spam = ['apples', 'bananas', 'tofu', 'cats']
print(comma(spam))