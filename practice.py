from sys import argv

script, filename = argv
#prompt = '> '

#print "Hello there %s ! We are going to play a little game today!" % (username)
#print "Do you want to play?"
#ans=raw_input(prompt)

txt = open(filename)

print "Do you want to open", filename
ans=raw_input(">>>")

print txt.read()



