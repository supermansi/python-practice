#My version

pyg = 'ay'
print("Enter a word to conver to pyglatin: ")
old_word = input("> ")
vowels = ['a', 'e', 'i', 'o', 'u']
word = old_word.lower()
if(word[0] not in vowels):
	new_word = word[1:len(word)] + word[0] + pyg
	print(new_word)
else:
	print(word + pyg)


#Codecademy version (there's no difference though)	
pyg = 'ay'

original = raw_input('Enter a word:')
if len(original) > 0 and original.isalpha():
    print original
    word = original.lower()
    first = word[0]
    new_word = word[1:len(word)]
    new_word = new_word + first + pyg
    print(new_word)
    
else:
    print 'empty'
