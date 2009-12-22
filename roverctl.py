import pygame
from pygame.locals import * 
import socket
import time

HOST="192.168.2.1"
#HOST="localhost"
PORT=6666

# blah

class Knuebbel:
	def __init__(self):
		print "Initializing..."
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.connect((HOST, PORT))

		pygame.init() 
		window = pygame.display.set_mode((468, 60))

		self.state = {"direction": 90, "speed": 90}

		#self.go_init()
		self.state["direction"] = 90
		self.send_it()

		print "Ready."

		self.loop()

	def send_it(self):
		tosend = "%003i%003i"%(self.state["speed"],self.state["direction"])
		print tosend
		self.s.send(tosend)

	def go_init(self):
		self.state["direction"] = 90
		self.send_it()
		time.sleep(2)
		self.state["direction"] = 90
		self.send_it()
		time.sleep(2)
		self.state["direction"] = 0
		self.send_it()
		time.sleep(2)
		self.state["direction"] = 60
		self.send_it()

	def go_left(self):
		self.state["direction"] = 60+45
		self.send_it()

	def go_right(self):
		self.state["direction"] = 60-45
		self.send_it()

	def go_ahead(self):
		self.state["direction"] = 60
		self.send_it()

	def go_backwards(self):
		self.state["speed"] = 70
		self.send_it()

	def go_forwards(self):
		self.state["speed"] = 110
		self.send_it()

	def go_stop(self):
		self.state["speed"] = 90
		self.send_it()

	def input(self, events):
		for event in events:
			if event.type == QUIT: 
				sys.exit(0)
			elif event.type == KEYUP:
				print "Keyup",
				if event.key == 273:
					print "up"
					self.go_stop()
				elif event.key == 276:
					print "left"
					self.go_ahead()
				elif event.key == 275:
					print "right"
					self.go_ahead()
				elif event.key == 274:
					print "down"
					self.go_stop()
			elif event.type == KEYDOWN:
				print "Keydown",
				#print event
				if event.key == 273:
					print "up"
					self.go_forwards()
				elif event.key == 276:
					print "left"
					self.go_left()
				elif event.key == 275:
					print "right"
					self.go_right()
				elif event.key == 274:
					print "down"
					self.go_backwards()
				elif event.key == 13:
					print "init"
					self.go_init()

			else: 
				#print event
				pass
	
	def loop(self):
		while True: 
			self.input(pygame.event.get())

Knuebbel()
