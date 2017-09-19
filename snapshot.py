import random
import time

currentstate={}

class Process(object):
	def __init__(self,pid,budget,quantity):
		self.pid=pid
		self.budget=budget
		self.quantity=quantity
		self.marker_received=False

	def receivemarker(self):
		if self.marker_received==False:
			self.marker_received=True
			self.recordlocalstate()
			self.sendmarkers()
	def sendmessage(self,pid,)


