import random
from Constants import Constants
from Microbe import Microbe
from Bouncer import Bouncer
from Food import Food
import matplotlib.pyplot as plt
from matplotlib import collections as mc
import math

class PetriDish:
	
	def __init__(self):
		self.entities = []
		self.microbes = []

	def getWidth(self):
		return Constants.PETRI_DISH_WIDTH

	def getHeight(self):
		return Constants.PETRI_DISH_HEIGHT

	def setup(self):
		self.setupBouncers()
		#self.innoculateDish()
		self.dropFood()

	def setupBouncers(self):
		self.addEntity(Bouncer(480, 380))
		self.addEntity(Bouncer(70 , 380))
		self.addEntity(Bouncer(70, 70))
		self.addEntity(Bouncer(480, 70))
		self.addEntity(Bouncer(275, 225))
		self.addEntity(Bouncer(225, 525))
		self.addEntity(Bouncer(775, 225))
		self.addEntity(Bouncer(725, 525))

	# TODO use the isColliding method to clean this shit up

	def innoculateDish(self):
		for i in range(0, Constants.STARTING_MICROBES):
			overlapping = True
			while overlapping:
				overlapping = False
				x = random.uniform(Constants.MICROBE_RADIUS*2, Constants.PETRI_DISH_WIDTH-Constants.MICROBE_RADIUS*2)
				y = random.uniform(Constants.MICROBE_RADIUS*2, Constants.PETRI_DISH_HEIGHT-Constants.MICROBE_RADIUS*2)
				for entity in self.entities:
					delta = math.sqrt(abs(math.pow((entity.getMyX() - x), 2) + math.pow((entity.getMyY() - y), 2)))
					if (delta <= (entity.getRadius() + Constants.MICROBE_RADIUS + 20)):
						overlapping = True
				for microbe in self.microbes:
					delta = math.sqrt(abs(math.pow((microbe.getMyX() - x), 2) + math.pow((microbe.getMyY() - y), 2)))
					if (delta <= (microbe.getRadius() + Constants.MICROBE_RADIUS + 20)):
						overlapping = True
			microbe = Microbe(x, y)
			self.addMicrobe(microbe)

	def dropFood(self):
		for i in range(0, Constants.STARTING_FOOD):
			overlapping = True
			while overlapping:
				overlapping = False
				x = random.uniform(Constants.FOOD_RADIUS*2, Constants.PETRI_DISH_WIDTH-Constants.FOOD_RADIUS*2)
				y = random.uniform(Constants.FOOD_RADIUS*2, Constants.PETRI_DISH_HEIGHT-Constants.FOOD_RADIUS*2)
				for entity in self.entities:
					delta = math.sqrt(abs(math.pow((entity.getMyX() - x), 2) + math.pow((entity.getMyY() - y), 2)))
					if (delta <= (entity.getRadius() + Constants.FOOD_RADIUS + 20)):
						overlapping = True
				for microbe in self.microbes:
					delta = math.sqrt(abs(math.pow((microbe.getMyX() - x), 2) + math.pow((microbe.getMyY() - y), 2)))
					if (delta <= (microbe.getRadius() + Constants.FOOD_RADIUS + 20)):
						overlapping = True
			food = Food(x, y)
			self.addEntity(food)

	def addEntity(self, entity):
		self.entities.append(entity)

	def addMicrobe(self, microbe):
		self.microbes.append(microbe)

	def updateDish(self):
		# TODO update microbes

		# Update non-microbe
		for entity in self.getEntities():
			changedDirection = False

			if (entity.getMyX() <= entity.getRadius()) or (entity.getMyX() >= (self.getWidth() - entity.getRadius())):
				entity.setDx(entity.getDx() * -1)
				changedDirection = True
			if (entity.getMyY() <= entity.getRadius()) or (entity.getMyY() >= (self.getHeight() - entity.getRadius())):
				entity.setDy(entity.getDy() * -1)
				changedDirection = True

			#if (not changedDirection) :
			#	if (entity.isColliding(self.getEntities())):
					# Colliding with another entity
			#		if (entity.getDx() > 0):
			#			entity.setDx(-1 * (1 + random.uniform(0,1)))
			#		else:
			#			entity.setDx(1 + random.uniform(0,1))

			#		if (entity.getDy() > 0):
			#			entity.setDy(-1 * (1 + random.uniform(0,1)))
			#		else:
			#			entity.setDy(1 + random.uniform(0,1))

			if (entity.getMyX() < 0 or entity.getMyX() > self.getWidth() or entity.getMyY() < 0 or entity.getMyY() > self.getHeight()):
				print("COLLISION LOGIC ERROR!")
				self.visualizeDish()
				exit()

			# Adjust the non-microbe position
			entity.setLocation((entity.getMyX() + (entity.getSpeed()*entity.getDx())), (entity.getMyY() + (entity.getSpeed()*entity.getDy())))

	def getEntities(self):
		return self.entities

	def getMicrobes(self):
		return self.microbes

	def visualizeDish(self):
		fig, ax = plt.subplots()

		ax.set_xlim((0, Constants.PETRI_DISH_WIDTH))
		ax.set_ylim((0, Constants.PETRI_DISH_HEIGHT))
		ax.patch.set_facecolor(Constants.DISH_COLOR)
		fig.patch.set_facecolor(Constants.FRAME)

		for entity in self.entities:
			drawnEntity = plt.Circle((entity.getMyX(), entity.getMyY()), entity.getRadius(), color=entity.getColor(), alpha=0.5, linewidth=2)
			ax.add_artist(drawnEntity)
			edgeColor = plt.Circle((entity.getMyX(), entity.getMyY()), entity.getRadius(), color="#0000FF", fill=False, linewidth=2)
			ax.add_artist(edgeColor)

		for microbe in self.microbes:
			drawnEntity = plt.Circle((microbe.getMyX(), microbe.getMyY()), microbe.getRadius(), color=microbe.getColor(), alpha=0.5, linewidth=2)
			ax.add_artist(drawnEntity)
			sightLines = mc.LineCollection(microbe.getSightLineCoordinates(), color='black', linewidths=0.5)
			ax.add_collection(sightLines)

		plt.show()











