from Entity import Entity
from Microbe import Microbe
import math
from Constants import Constants

class NonMicrobe (Entity):
	
	# Initializer
	def __init__(self, xLocation, yLocation, radius):
		super().__init__(xLocation, yLocation)

		self.radius = radius
		self.dx = 1
		self.dy = 1
		self.speed = 0
		self.shockClock = Constants.SHOCK_CLOCK
		self.resetClock = Constants.RESET_CLOCK
		self.lastCollision = None
		self.alerted = False

	def getTop(self):
		return (self.getMyY() + self.getRadius())

	def getBottom(self):
		return (self.getMyY() - self.getRadius())

	def getRight(self):
		return (self.getMyX() + self.getRadius())

	def getLeft(self):
		return (self.getMyX() - self.getRadius())

	def setAlerted(self, setting):
		self.isAlerted = setting

	def isAlerted(self):
		return self.alerted

	def getDx(self):
		return self.dx

	def getDy(self):
		return self.dy

	def setDx(self, dx):
		self.dx = dx

	def setDy(self, dy):
		self.dy = dy

	def setLastCollision(self, lastCollision):
		self.lastCollision = lastCollision

	def getLastCollision(self):
		return self.lastCollision

	def isColliding(self, entities):
		for entity in entities:
			if (entity != self) :
				delta = math.sqrt(abs(math.pow((entity.getMyX() - self.getMyX()), 2) + math.pow((entity.getMyY() - self.getMyX()), 2)))
				if (delta <= (entity.getRadius() + self.getRadius())):
					self.setAlerted(True)
					self.shockClock = Constants.SHOCK_CLOCK

					if (entity == self.getLastCollision()):
						self.resetClock = self.resetClock - 1
						if (self.resetClock <= 0) :
							# TODO reset position randomly here
							self.setLastCollision(None)
					else :
						self.setLastCollision(entity)
						self.resetClock = Constants.RESET_CLOCK
					
					return True

		if (self.shockClock <= 0) :
			self.setAlerted(False)
		else :
			self.shockClock = self.shockClock - 1

		return False


