import random
from Constants import Constants
from Microbe import Microbe
from Bouncer import Bouncer
import matplotlib.pyplot as plt
import math

class PetriDish:
	
	def __init__(self):
		self.entities = []

	def getWidth(self):
		return Constants.PETRI_DISH_WIDTH

	def getHeight(self):
		return Constants.PETRI_DISH_HEIGHT

	def setup(self):
		self.setupBouncers()
		self.innoculateDish()
		#self.dropFood()

	def setupBouncers(self):
		x = Constants.BOUNCER_RADIUS + 10
		y = Constants.BOUNCER_RADIUS + 10
		bouncer = Bouncer(x, y)
		self.addEntity(bouncer)
		x = Constants.PETRI_DISH_WIDTH-Constants.BOUNCER_RADIUS - 10
		y = Constants.BOUNCER_RADIUS+ 10 
		bouncer = Bouncer(x, y)
		self.addEntity(bouncer)
		x = Constants.BOUNCER_RADIUS + 10
		y = Constants.PETRI_DISH_HEIGHT-Constants.BOUNCER_RADIUS - 10
		bouncer = Bouncer(x, y)
		self.addEntity(bouncer)
		x = Constants.PETRI_DISH_WIDTH-Constants.BOUNCER_RADIUS - 10
		y = Constants.PETRI_DISH_HEIGHT-Constants.BOUNCER_RADIUS - 10
		bouncer = Bouncer(x, y)
		self.addEntity(bouncer)
		x = Constants.PETRI_DISH_WIDTH/2
		y = Constants.PETRI_DISH_HEIGHT-Constants.BOUNCER_RADIUS - 10
		bouncer = Bouncer(x, y)
		self.addEntity(bouncer)
		x = Constants.PETRI_DISH_WIDTH/2
		y = Constants.BOUNCER_RADIUS + 10
		bouncer = Bouncer(x, y)
		self.addEntity(bouncer)



	def innoculateDish(self):
		for i in range(0, Constants.STARTING_MICROBES):
			overlapping = True
			while overlapping:
				overlapping = False
				x = random.uniform(Constants.MICROBE_RADIUS*2, Constants.PETRI_DISH_WIDTH-Constants.MICROBE_RADIUS*2)
				y = random.uniform(Constants.BOUNCER_RADIUS*2, Constants.PETRI_DISH_HEIGHT-Constants.BOUNCER_RADIUS*2)
				for entity in self.entities:
					delta = math.sqrt(abs(math.pow((entity.getMyX() - x), 2) + math.pow((entity.getMyY() - y), 2)))
					if (delta <= (entity.getRadius() + Constants.MICROBE_RADIUS + 20)):
						overlapping = True
			microbe = Microbe(x, y)
			self.addEntity(microbe)

	def dropFood(self):
		pass

	def addEntity(self, entity):
		self.entities.append(entity)

	def updateDish(self):
		for entity in self.getEntities():
			if (isinstanceof(entity, Microbe)):
				# Update microbe
				entity.update(self.getEntities())
			else:
				# Update non-microbe
				if (entity.getMyX() < entity.getRadius() or entity.getMyX() > self.getWidth() - entity.getRadius()):
					# out of bounds on x axis
					entity.setDx(entity.getDx() * -1)
				if (entity.getMyY() < entity.getRadius() or entity.getMyY() > self.getHeight() - entity.getRadius()):
					# out of bounds on the y axis
					entity.setDy(entity.getDy() * -1)
				if (entity.isColliding(self.getEntities())):
					# Colliding with another entity
					if (entity.getDx() > 0):
						entity.setDx(-1 * (1 + random.uniform(0,1)))
					else:
						entity.setDx(1 + random.uniform(0,1))
					if (entity.getDy() > 0):
						entity.setDy(-1 * (1 + random.uniform(0,1)))
					else:
						entity.setDy(1 + random.uniform(0,1))
				# Adjust the non-microbe position
				entity.setLocation((entity.getMyX() + (entity.getSpeed()*entity.getDx())), (entity.getMyY() + (entity.getSpeed()*entity.getDy())))

	def getEntities(self):
		return self.entities

	def visualizeDish(self):
		fig, ax = plt.subplots()

		ax.set_xlim((0, Constants.PETRI_DISH_WIDTH))
		ax.set_ylim((0, Constants.PETRI_DISH_HEIGHT))
		ax.set_facecolor('#d0fefe')
		fig.patch.set_facecolor('#D3D3D3')

		for entity in self.entities:
			drawnEntity = plt.Circle((entity.getMyX(), entity.getMyY()), entity.getRadius(), color=entity.getColor(), alpha=0.5)
			ax.add_artist(drawnEntity)

		plt.show()











