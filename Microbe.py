import math
import random
from Constants import Constants
from VisionLine import VisionLine
from Entity import Entity

class Microbe (Entity):

	# Initializer
	def __init__(self, xLocation, yLocation):
		super().__init__(xLocation, yLocation)
		self.setRadius(Constants.MICROBE_RADIUS)


		# Build needed pieces
		self.rotation = random.randint(0,359)
		self.addVisionField()

		# Define Lineage
		self.parent1 = None
		self.parent2 = None
		self.age = 0
		self.generation = 0
		self.clan = random.randint(900000,1000000)
		self.name = self.clan + (random.randint(900,1000) * 1000000)
		self.generateRace()
		
	def setParents(self, parent1, parent2):
		# Adjust Lineage
		self.parent1 = parent1
		self.parent2 = parent2
		self.generation = (parent1.getGeneration() + 1)
		self.clan = parent1.getClan()
		self.name = self.clan + (random.randint(900,1000) * 1000000)
		self.generateRace()

		# Adjust Race
		self.rPigment = ((parent1.getrPigment() + parent2.getrPigment()) / 2)
		self.gPigment = ((parent1.getgPigment() + parent2.getgPigment()) / 2)
		self.bPigment = ((parent1.getbPigment() + parent2.getbPigment()) / 2)

	def addVisionField(self):
		self.vision_field_distance = random.uniform(Constants.MICROBE_RADIUS, Constants.MICROBE_MAX_VISION_FIELD)
		self.setVisionField()

	def setVisionField(self):
		self.sight1 = VisionLine(self, (Constants.MICROBE_RADIUS*self.vision_field_distance*math.cos(math.radians(self.rotation-25))), (Constants.MICROBE_RADIUS*self.vision_field_distance*math.sin(math.radians(self.rotation-25))))
		self.sight2 = VisionLine(self, (Constants.MICROBE_RADIUS*self.vision_field_distance*math.cos(math.radians(self.rotation-45))), (Constants.MICROBE_RADIUS*self.vision_field_distance*math.sin(math.radians(self.rotation-45))))
		self.sight3 = VisionLine(self, (Constants.MICROBE_RADIUS*self.vision_field_distance*math.cos(math.radians(self.rotation-60))), (Constants.MICROBE_RADIUS*self.vision_field_distance*math.sin(math.radians(self.rotation-60))))
		self.sight4 = VisionLine(self, (Constants.MICROBE_RADIUS*self.vision_field_distance*math.cos(math.radians(self.rotation-90))), (Constants.MICROBE_RADIUS*self.vision_field_distance*math.sin(math.radians(self.rotation-90))))
		self.sight5 = VisionLine(self, (Constants.MICROBE_RADIUS*self.vision_field_distance*math.cos(math.radians(self.rotation-115))), (Constants.MICROBE_RADIUS*self.vision_field_distance*math.sin(math.radians(self.rotation-120))))
		self.sight6 = VisionLine(self, (Constants.MICROBE_RADIUS*self.vision_field_distance*math.cos(math.radians(self.rotation-135))), (Constants.MICROBE_RADIUS*self.vision_field_distance*math.sin(math.radians(self.rotation-135))))
		self.sight7 = VisionLine(self, (Constants.MICROBE_RADIUS*self.vision_field_distance*math.cos(math.radians(self.rotation-150))), (Constants.MICROBE_RADIUS*self.vision_field_distance*math.sin(math.radians(self.rotation-155))))

	def generateRace(self):
		self.rPigment = random.uniform(0, 1)
		self.gPigment = random.uniform(0, 1)
		self.bPigment = random.uniform(0, 1)
		self.setColor([self.rPigment, self.gPigment, self.bPigment])

	def getVisionFieldDistance(self):
		return self.vision_field_distance

	def getrPigment(self):
		return self.rPigment

	def getgPigment(self):
		return self.gPigment

	def getbPigment(self):
		return self.bPigment

	def getAge(self):
		return self.age

	def setAge(self, age):
		self.age = age

	def getGeneration(self):
		return self.generation

	def getName(self):
		return self.name

	def getClan(self):
		return self.clan

	def getParent1(self):
		return self.parent1

	def getParent2(self):
		return self.parent2

	def reproduceWith(self, partner):
		self.setAge(self.getAge() + 1)
		partner.setAge(self.getAge() + 1)

		baby = Microbe(random.uniform(Constants.MICROBE_RADIUS, Constants.PETRI_DISH_WIDTH), random.uniform(Constants.MICROBE_RADIUS, Constants.PETRI_DISH_HEIGHT))
		baby.setParents(self, partner)
		return baby

	def update(self, surroundings) :
		# TODO check surroundings
		# TODO turn aroudn and move accordingly

		delta = 0

		for entity in surroundings :
			if (entity != self) :
				myX = self.getMyX()
				myY = self.getMyY()
				itsX = entity.getMyX()
				itsY = entity.getMyY()

				delta = math.sqrt(math.abs(Math.pow((myX - itsX), 2) + math.pow((myY - itsY), 2)))

				if (isinstanceof(entity, Microbe)) :
					if (delta < (2*Constants.MICROBE_RADIUS)) :
						print(self.getName() + " collided with " + entity.getName() + ". Delta = " + delta)
						# TODO microbe interaction logic
				elif (isinstanceof(entity, NonMicrobe)) :
					print(self.getName() + " collided with an environment entity. Delta = " + delta)
					# TODO environment interaction logic
				else :
					print("Error. Unrecognized entitiy.")
					exit()

	def toString(self):
		parentString = ""
		if (self.getParent1() is None):
			parentString = "inoculation"
		else :
			parentString = str(self.getParent1().getName()) + " " + str(self.getParent2().getName())
		
		myX = str(self.getMyX())
		myY = str(self.getMyY())

		return "Name: " + str(self.name) +"\nParents: " + parentString + "\nClan: " + str(self.clan) + "\nGeneration: " +  str(self.generation) + "\nAge: " + str(self.age) + "\nRGB: " + str(self.rPigment) + " " + str(self.gPigment) + " " + str(self.bPigment) + "\nCurrent Coordinates: (" + myX + ", " + myY + ")"




