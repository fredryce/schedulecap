import os, sys, glob
import datetime
import cv2
import pyautogui

#schedule the program to run all the time


class Schedule(object):
	def __init__(self, all_classes=None):
		self.all_classes = []
		if all_classes:
			self.all_classes = all_classes

class Class(object):
	def __init__(self, name, start_time, end_time):
		self.name = name
		self.start_time = start_time
		self.end_time = end_time


class Scheduler(object):
	def __init__(self):
		my_schedule = Schedule()

	

if __name__ == "__main__":
	mysch = Scheduler()

