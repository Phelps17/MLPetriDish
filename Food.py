from NonMicrobe import NonMicrobe
from Constants import Constants

class Food (NonMicrobe):
	# Initializer
	def __init__(self, xLocation, yLocation):
		super().__init__(xLocation, yLocation, Constants.FOOD_RADIUS)
		self.setColor(Constants.FOOD_COLOR)
		self.setSpeed(3)