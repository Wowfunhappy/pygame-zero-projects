import pgzrun
import random

WIDTH = 800
HEIGHT = 480

player = Actor('dog')
player.x = 100
player.y = 400

fallingObject = Actor('banana')
fallingObject.x = 300
fallingObject.y = 0

score = 0

def update():
	global score
	screen.clear()
	
	fallingObject.y = fallingObject.y + 5
	
	if keyboard.left:
		player.x = player.x - 10
	if keyboard.right:
		player.x = player.x + 10
	
	if fallingObject.colliderect(player):
		fallingObject.y = 0
		fallingObject.x = random.randint(0, WIDTH)
		score = score + 1
		
	screen.draw.text(str(score), [20, 20])		
		
	if fallingObject.y > 480:
		screen.draw.text("GAME OVER", [WIDTH / 2, HEIGHT / 2])
			
	player.draw()
	fallingObject.draw()
	
pgzrun.go()