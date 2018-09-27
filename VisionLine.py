
class VisionLine:

	# Initializer
	def __init__(self, microbe, end_x, end_y):
		self.microbe = microbe
		self.end_x = end_x
		self.end_y = end_y

	def checkVision(self):
		# TODO update depending on what teh line sees
		pass

	def getVisionX(self):
		return self.microbe.getMyX() + self.end_x

	def getVisionY(self):
		return self.microbe.getMyY() + self.end_y