from Constants import Constants
import math

class Entity:
	def __init__(self, xLocation, yLocation):
		self.setLocation(xLocation, yLocation)
		self.radius = 0
		self.speed = 0
		self.color = 0
		self.setBorderColor(Constants.BLUE);

	def setLocation(self, xLocation, yLocation):
		self.xLocation = xLocation
		self.yLocation = yLocation

	def printLocation(self):
		print("(",self.getMyX(),",",self.getMyY(),")")

	def getMyX(self):
		return self.xLocation

	def getMyY(self):
		return self.yLocation

	def getRadius(self):
		return self.radius

	def setRadius(self, radius):
		self.radius = radius

	def getSpeed(self):
		return self.speed 

	def setSpeed(self, speed):
		self.speed = speed

	def getColor(self):
		return self.color 

	def setColor(self, color):
		self.color = color

	def setBorderColor(self, color):
		self.color = color

	def getBorderColor(self):
		return self.color



