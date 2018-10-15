from NonMicrobe import NonMicrobe
from Constants import Constants

class Bouncer (NonMicrobe):
	# Initializer
	def __init__(self, xLocation, yLocation):
		super().__init__(xLocation, yLocation, Constants.BOUNCER_RADIUS)
		self.setColor(Constants.BOUNCER_COLOR)