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

	