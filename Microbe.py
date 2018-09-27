import math
import random
import Constants
from VisionLine import VisionLine

class Microbe:

	# Initializer
	def __init__(self, xLocation, yLocation):
		# Build needed pieces
		self.rotation = random.randint(0,359)
		self.addVisionField()

		# Define Lineage
		self.parent1 = None
		self.parent2 = None
		self.age = 0
		self.generation = 0;
		self.clan = random.randint(900000,1000000)
		self.name = self.clan + (random.randint(900,1000) * 1000000)
		self.generateRace()

		# Place in dish
		self.setLocation(xLocation, yLocation)
		
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


	def setLocation(self, xLocation, yLocation):
		self.xLocation = xLocation
		self.yLocation = yLocation

	def addVisionField(self):
		self.vision_field_distance = random.uniform(0, 1) * Constants.MICROBE_MAX_VISION_FIELD
		self.setVisionField()

	def setVisionField(self):
		self.sight1 = VisionLine(self, (Constants.MICROBE_RADIUS_DEFAULT*self.vision_field_distance*math.cos(math.radians(self.rotation-25))), (Constants.MICROBE_RADIUS_DEFAULT*self.vision_field_distance*math.sin(math.radians(self.rotation-25))))
		self.sight2 = VisionLine(self, (Constants.MICROBE_RADIUS_DEFAULT*self.vision_field_distance*math.cos(math.radians(self.rotation-45))), (Constants.MICROBE_RADIUS_DEFAULT*self.vision_field_distance*math.sin(math.radians(self.rotation-45))))
		self.sight3 = VisionLine(self, (Constants.MICROBE_RADIUS_DEFAULT*self.vision_field_distance*math.cos(math.radians(self.rotation-60))), (Constants.MICROBE_RADIUS_DEFAULT*self.vision_field_distance*math.sin(math.radians(self.rotation-60))))
		self.sight4 = VisionLine(self, (Constants.MICROBE_RADIUS_DEFAULT*self.vision_field_distance*math.cos(math.radians(self.rotation-90))), (Constants.MICROBE_RADIUS_DEFAULT*self.vision_field_distance*math.sin(math.radians(self.rotation-90))))
		self.sight5 = VisionLine(self, (Constants.MICROBE_RADIUS_DEFAULT*self.vision_field_distance*math.cos(math.radians(self.rotation-115))), (Constants.MICROBE_RADIUS_DEFAULT*self.vision_field_distance*math.sin(math.radians(self.rotation-120))))
		self.sight6 = VisionLine(self, (Constants.MICROBE_RADIUS_DEFAULT*self.vision_field_distance*math.cos(math.radians(self.rotation-135))), (Constants.MICROBE_RADIUS_DEFAULT*self.vision_field_distance*math.sin(math.radians(self.rotation-135))))
		self.sight7 = VisionLine(self, (Constants.MICROBE_RADIUS_DEFAULT*self.vision_field_distance*math.cos(math.radians(self.rotation-150))), (Constants.MICROBE_RADIUS_DEFAULT*self.vision_field_distance*math.sin(math.radians(self.rotation-155))))

	def generateRace(self):
		self.rPigment = random.uniform(0, 1)
		self.gPigment = random.uniform(0, 1)
		self.bPigment = random.uniform(0, 1)

	def getMyX(self):
		return self.xLocation

	def getMyY(self):
		return self.yLocation

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

	def toString(self):
		parentString = ""
		if (self.getParent1() is None):
			parentString = "inoculation";
		else :
			parentString = str(self.getParent1().getName()) + " " + str(self.getParent2().getName())
		
		myX = str(self.getMyX());
		myY = str(self.getMyY());

		return "Name: " + str(self.name) +"\nParents: " + parentString + "\nClan: " + str(self.clan) + "\nGeneration: " +  str(self.generation) + "\nAge: " + str(self.age) + "\nRGB: " + str(self.rPigment) + " " + str(self.gPigment) + " " + str(self.bPigment) + "\nCurrent Coordinates: (" + myX + ", " + myY + ")";

microbe1 = Microbe(300, 100)
microbe2 = Microbe(320, 100)
microbe3 = Microbe(300, 120)
microbe4 = Microbe(300, 100)
microbe4.setParents(microbe1, microbe2)
microbe5 = Microbe(320, 100)
microbe5.setParents(microbe2, microbe3)
microbe6 = Microbe(300, 120)
microbe6.setParents(microbe4, microbe5)
#print(microbe.getMyX(), microbe.getMyY())
#print(microbe.sight1.getVisionX(), microbe.sight1.getVisionY())
#print(microbe.sight2.getVisionX(), microbe.sight2.getVisionY())
#print(microbe.sight3.getVisionX(), microbe.sight3.getVisionY())
#print(microbe.sight4.getVisionX(), microbe.sight4.getVisionY())
#print(microbe.sight5.getVisionX(), microbe.sight5.getVisionY())
#print(microbe.sight6.getVisionX(), microbe.sight6.getVisionY())
#print(microbe.sight7.getVisionX(), microbe.sight7.getVisionY())
print(microbe1.toString())
print("========================================================================")
print(microbe2.toString())
print("========================================================================")
print(microbe3.toString())
print("========================================================================")
print(microbe4.toString())
print("========================================================================")
print(microbe5.toString())
print("========================================================================")
print(microbe6.toString())









