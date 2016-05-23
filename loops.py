fnames = ['archie', 'betty', 'veronica', 'reggie', 'jughead']
for index, n in enumerate(fnames): # to include the index and value of list
	print index+1, n #comma is to separate with a ' ' <space>
	
gender = {}
for n in fnames:
	if n[len(n)-1] == 'e' or n[len(n)-1] == 'd':
		gender[n] = 'M'
	else:
		gender[n] = 'F'

print gender

l1 = [1,2,3,4,5]
l2 = [6,21,4,5,1]
l3 = [1,4,6]

for a, b, c in zip(l1, l2, l3): #considers respective order of multiple lists
	print a + b + c, #goes only until len(c)
	
'''
Using else with loops:

1. while loop - else outside while loop will be executed only when loop ends normaly or never enters the loop. Not when there is a break statement.
2. for loop - else outside the loop will be executed only when loop ends normaly
'''

def is_int(x):
    x = abs(x)
    if x-int(x) > 0:
    	print 'no'
        return True
    print 'int'
    return False
is_int(11.0)
is_int(11.04)
is_int(11)
