
class NonMicrobe :
	
	# Initializer
	def __init__(self, xLocation, yLocation, radius):
		self.setLocation(xLocation, yLocation)
		self.radius = radius

	def setLocation(self, xLocation, yLocation):
		self.xLocation = xLocation
		self.yLocation = yLocation

	def getMyX(self):
		return self.xLocation

	def getMyY(self):
		return self.yLocation

	def getRadus(self):
		return self.radius

	def getTop(self):
		return (self.getMyY() + self.getRadius())

	def getBottom(self):
		return (self.getMyY() - self.getRadius())

	def getRight(self):
		return (self.getMyX() + self.getRadius())

	def getLeft(self):
		return (self.getMyX() - self.getRadius())

	def isColliding(self):
		pass