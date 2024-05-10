import pgzrun
import random

WIDTH = 640
HEIGHT = 480

obsticles = []
lasers = []
laserCooldown = False

car = Actor('car.png')
car.x = 100

def addObsticle():
	obsticle = Actor('cone.png')
	obsticle.x = WIDTH + 50
	obsticle.y = random.randint(0, HEIGHT)
	obsticles.append(obsticle)
	clock.schedule(addObsticle, 0.5)

gameOver = Actor('gameover.png')
gameOver.x = WIDTH / 2
gameOver.y = HEIGHT / 2
isGameOver = False
	
clock.schedule(addObsticle, 1.0)

def endLaserCooldown():
	global laserCooldown
	laserCooldown = False

def update():
	global isGameOver
	global laserCooldown
	
	if isGameOver:
		gameOver.draw()
	else:
		screen.clear()
		
		for obsticle in obsticles:
			obsticle.x = obsticle.x - 3
			obsticle.draw()
			if obsticle.colliderect(car):
				isGameOver = True
		
		car.angle = 0
		if keyboard.UP:
			car.y = car.y - 5
			if car.y < 0:
				car.y = 0
		if keyboard.DOWN:
			car.y = car.y + 5
			if car.y > HEIGHT:
				car.y = HEIGHT
		
		if keyboard.SPACE and not laserCooldown:
			laser = Actor('laser.png')
			laser.x = car.x
			laser.y = car.y
			lasers.append(laser)
			laserCooldown = True
			clock.schedule(endLaserCooldown, 0.5)
		
		for laser in lasers:
			laser.x = laser.x + 10
			laser.draw()
			for obsticle in obsticles:
				if obsticle.colliderect(laser):
					obsticles.remove(obsticle)
					lasers.remove(laser)
					
		car.draw()
	
pgzrun.go()