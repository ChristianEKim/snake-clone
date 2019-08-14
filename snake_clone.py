import pygame
import random

pygame.init()

screen_width = 600
screen_height = 600

wn = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake Clone')

clock = pygame.time.Clock()


class Snake(object):	
	def __init__(self, x, y):
		self.x = x 
		self.y = y 
		self.up = False
		self.down = False
		self.left = False 
		self.right = False 
		self.vel = 15
		self.tail = 1
		
	def draw(self, wn):
		for x,y in to_draw:
			pygame.draw.rect(wn, (255, 255, 255), [x, y, 15, 15], 2)


class Block(object):
	def __init__(self):
		self.y = random.randint(0, 39) * 15
		self.x = random.randint(0, 39) * 15
		self.redraw = False 
		
	def draw(self, wn):
		if self.redraw:
			self.y = random.randint(0, 39) * 15
			self.x = random.randint(0, 39) * 15
			self.redraw = False 
		
		if (self.x, self.y) in to_draw:	
			self.y = random.randint(0, 39) * 15
			self.x = random.randint(0, 39) * 15
		else:
			pygame.draw.rect(wn, (255, 0, 0), [self.x, self.y, 15, 15])
		


def redraw_game_window():
	wn.fill((0,0,0))
	block.draw(wn)
	snake.draw(wn)

	pygame.display.update()
	
def restart():
	del to_draw[:]
	snake.x, snake.y = 300, 300
	snake.tail = 1
	block.redraw = True 
	snake.up = False
	snake.down = False 
	snake.left = False 
	snake.right = False 
	


snake = Snake(300, 300)
block = Block()
to_draw = []

# main game loop
run = True

while run:
	clock.tick(15)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	
	keys = pygame.key.get_pressed()
	
	if keys[pygame.K_w] and not snake.down:
		snake.up = True
		snake.down = False 
		snake.left = False 
		snake.right = False 
		
	if keys[pygame.K_s] and not snake.up:
		snake.up = False
		snake.down = True
		snake.left = False 
		snake.right = False 
		
	if keys[pygame.K_a] and not snake.right:
		snake.up = False
		snake.down = False 
		snake.left = True
		snake.right = False 
		
	if keys[pygame.K_d] and not snake.left:
		snake.up = False
		snake.down = False 
		snake.left = False 
		snake.right = True
		
	if snake.up:
		snake.y -= snake.vel
	elif snake.down:
		snake.y += snake.vel
	elif snake.left:
		snake.x -= snake.vel
	elif snake.right:
		snake.x += snake.vel 
	
	# hitting borders
	if screen_width - 15 < snake.x  or snake.x < 0:
		restart()
	if screen_height - 15 < snake.y or snake.y < 0:
		restart()
		
	# eating the block
	if block.x == snake.x and block.y == snake.y:
		block.redraw = True 
		snake.tail += 4
		
	# collision
	if (snake.x, snake.y) in to_draw and (snake.up or snake.down or snake.left or snake.right):
		restart() 
		

	to_draw.append((snake.x, snake.y))
	
	if len(to_draw) > snake.tail:
		del to_draw[0]
	

	redraw_game_window()
	
pygame.quit()