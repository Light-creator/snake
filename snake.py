import pygame
import random
import sys
snake_color = (0,255,0)
background = (0,0,0)
apple_color = (255,0,0)
height = 10															# Snake size	
width = 10
screen_height = 300
screen_width = 400
win = pygame.display.set_mode((screen_width, screen_height))		# Screen
walk = 10															# Speed
head = [100, 100]													# Head position
body = [[100, 100], [90, 100], [80, 100]]							# Body position
def exit():
	print("GAME OVER")
	pygame.quit()
	sys.exit()
def game_over():
	if head[0] == screen_width or head[1] == screen_height or head[0] == 0 or head[1] == 0:			# Screen collision
		exit()

	for pos in body:																				# Body collision
		if head[0] == pos[0] and head[1] == pos[1] and pos != body[0]:
				exit()
def change_moove(change):
	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT] and change != "right":
		change = "left"
	if keys[pygame.K_RIGHT] and change != "left":
		change = "right"
	if keys[pygame.K_UP] and change != "down":
		change = "up"
	if keys[pygame.K_DOWN] and change != "up":
		change = "down"
	return change
def main():
	appleX = random.randrange(1, screen_width/10)*10   # First appearance of apple
	appleY = random.randrange(1, screen_height/10)*10
	change = "up"
	pygame.init()
	while True:
		pygame.time.delay(100)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT] and change != "right":
			change = "left"
		if keys[pygame.K_RIGHT] and change != "left":
			change = "right"
		if keys[pygame.K_UP] and change != "down":
			change = "up"
		if keys[pygame.K_DOWN] and change != "up":
			change = "down"
		if change == "left":
			head[0] -= 10
		elif change == "right":
			head[0] += 10
		elif change == "up":
			head[1] -= 10
		else:
			head[1] += 10
		game_over()
		body.insert(0, list(head))
		for pos in body:
			pygame.draw.rect(win, snake_color, pygame.Rect(pos[0], pos[1], width, height))
		if pos[0] == appleX and pos[1] == appleY:
			appleX = random.randrange(1, screen_width/10)*10
			appleY = random.randrange(1, screen_height/10)*10
		else:
			body.pop()
		apple = pygame.draw.rect(win, apple_color, (appleX, appleY, 10, 10))
		pygame.display.update()
		win.fill(background)
if __name__ == "__main__":
	main()




