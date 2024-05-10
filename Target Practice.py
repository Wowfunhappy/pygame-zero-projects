import pgzrun
import random

WIDTH = 640
HEIGHT = 480

background = Actor('hills.png')

bow = Actor('bow.png')
bow.x = 70
bow.direction = "down"
bow.speed = 5

arrow = Actor('arrow.png')
arrow.wasFired = False

target = Actor('target.png')
target.x = 550
target.y = random.randint(40, HEIGHT - 40)

gameOver = Actor('gameover.png')
gameOver.x = WIDTH / 2
gameOver.y = HEIGHT / 2
isGameOver = False

score = 0
time = 20

def decreaseTime():
	global time
	global isGameOver
	if time > 0 and not isGameOver:
		time = time - 1
	else:
		isGameOver = True
	clock.schedule(decreaseTime, 1.0)
	
clock.schedule(decreaseTime, 1.0)

def update():
	global isGameOver
	global score
	global time
	
	screen.clear()
	background.draw()
	
	if isGameOver:
		gameOver.draw()
	else:
		if bow.direction == "down":
			bow.y = bow.y + bow.speed
			if bow.y > HEIGHT:
				bow.direction = "up"
		if bow.direction == "up":
			bow.y = bow.y - bow.speed
			if bow.y < 0:
				bow.direction = "down"

		if keyboard.SPACE and not arrow.wasFired:
			arrow.wasFired = True
		
		if arrow.wasFired:
			arrow.x = arrow.x + 20
		else:
			arrow.x = bow.x
			arrow.y = bow.y
		
		if arrow.colliderect(target):
			score = score + 1
			bow.speed = bow.speed + 1
			arrow.wasFired = False
			target.y = random.randint(40, HEIGHT - 40)
		
		if arrow.x > WIDTH:
			isGameOver = True
			
	bow.draw()
	arrow.draw()
	target.draw()
	
	screen.draw.text("Score: " + str(score), [238, 10], color="black")
	screen.draw.text("Time: " + str(time), [338, 10], color="black")
	
pgzrun.go()