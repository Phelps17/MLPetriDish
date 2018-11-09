from NonMicrobe import NonMicrobe
from Constants import Constants
import math

class Bouncer (NonMicrobe):
	# Initializer
	def __init__(self, xLocation, yLocation):
		super().__init__(xLocation, yLocation, Constants.BOUNCER_RADIUS)
		self.setColor(Constants.BOUNCER_COLOR)
		self.setSpeed(1)


	def isColliding(self, entities):
		for entity in entities:
			if (entity != self) :
				delta = math.sqrt(abs(math.pow((entity.getMyX() - self.getMyX()), 2) + math.pow((entity.getMyY() - self.getMyX()), 2)))
				if (delta <= (entity.getRadius() + self.getRadius())):
					self.setAlerted(True)
					self.shockClock = Constants.SHOCK_CLOCK
					
					return True

		if (self.shockClock <= 0) :
			self.setAlerted(False)
		else :
			self.shockClock = self.shockClock - 1

		return False