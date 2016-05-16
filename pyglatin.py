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
