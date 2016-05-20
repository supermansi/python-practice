#prompt = '> '

#print "Hello there %s ! We are going to play a little game today!" % (username)
#print "Do you want to play?"
#ans=raw_input(prompt)

print "Which file do you want to open?"
filename = raw_input("> ")

txt=open(filename)

print txt.read()



