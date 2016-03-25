import pygame, sys

pygame.init()

screen = pygame.display.set_mode([1000,1000])

r=pygame.Color("red")
w=pygame.Color("white")
b=pygame.Color("blue")
y=pygame.Color("yellow")

data = [
	[w,w,w,w,w,w,w,w,w,w],
	[w,w,w,w,w,w,w,w,w,w],
	[w,w,w,w,b,b,w,w,w,w],
	[w,w,w,b,y,y,b,w,w,w],
	[w,w,b,y,r,r,y,b,w,w],
	[w,w,b,y,r,r,y,b,w,w],
	[w,b,y,r,w,w,r,y,b,w],
	[b,y,r,r,w,w,r,r,y,b],
	[b,y,r,w,w,w,w,r,y,b],
	[b,y,r,w,w,w,w,r,y,b],
]

for y, row in enumerate(data):
	for x, color in enumerate(row):
		rect=pygame.Rect(x*100,y*100,100,100)
		screen.fill(color,rect=rect)
		
pygame.display.update()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
