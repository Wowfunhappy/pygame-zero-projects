import pgzrun
import random

WIDTH = 640
HEIGHT = 480

bee = Actor("bee.png")
bee.x = random.randint(0, WIDTH)
bee.y = random.randint(0, HEIGHT)

honey = Actor("honey.png")
honey.x = random.randint(0, WIDTH)
honey.y = random.randint(0, HEIGHT)

score = 0
time = 15

isGameOver = False
gameOver = Actor("game over.png")
gameOver.x = WIDTH / 2
gameOver.y = HEIGHT / 2

def decreaseTime():
	global time
	global isGameOver
	
	if time > 0:
		time -= 1
		clock.schedule(decreaseTime, 1)
	
	if time == 0:
		isGameOver = True

decreaseTime()
	
def update():
	global score
	global time
	global isGameOver
	
	screen.clear()
	
	if not isGameOver:
		if keyboard.UP:
			bee.y -= 5
		if keyboard.DOWN:
			bee.y += 5
		if keyboard.LEFT:
			bee.x -= 5
		if keyboard.RIGHT:
			bee.x += 5
			
		if bee.x > WIDTH:
			bee.x = 0
		if bee.x < 0:
			bee.x = WIDTH
		if bee.y > HEIGHT:
			bee.y = 0
		if bee.y < 0:
			bee.y = HEIGHT
		
		if bee.colliderect(honey):
			honey.x = random.randint(0, WIDTH)
			honey.y = random.randint(0, HEIGHT)
			score += 1
			
	bee.draw()
	honey.draw()
	
	if isGameOver:
		gameOver.draw()
		screen.draw.text("Press space to play again!", centerx = WIDTH / 2, centery = (HEIGHT / 2) + 60)
		if keyboard.SPACE:
			time = 15
			score = 0
			isGameOver = False
			
			bee.x = random.randint(0, WIDTH)
			bee.y = random.randint(0, HEIGHT)

			honey.x = random.randint(0, WIDTH)
			honey.y = random.randint(0, HEIGHT)
			
			decreaseTime()
	
	screen.draw.text("Score: " + str(score), [20, 10])
	screen.draw.text("Time: " + str(time), [WIDTH - 80, 10])

pgzrun.go()
	