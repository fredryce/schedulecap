import os, sys, glob
import datetime

#schedule the program to run all the time
default_dir = "C:/Users/Jenna/Desktop/Captures"

class Schedule(object):
	def __init__(self, all_classes=None):
		self.all_classes = []
		if all_classes:
			self.all_classes = all_classes
			#tues, thurs
		self.all_classes.append(Class("phyclass", [1, 3], datetime.time(10,40,0), datetime.time(11,30,0)))
		self.all_classes.append(Class("phydiss", [2, 4], datetime.time(11,45,0), datetime.time(12,35,0)))
		#wed fri
class Class(object):
	def __init__(self, name, weekday, start_time, end_time): 
		self.name = name
		self.weekday = weekday
		self.start_time = start_time #class time list
		self.end_time = end_time #class time list


class Scheduler(object):
	def __init__(self):
		self.my_schedule = Schedule()
		self.checkfolders()


	def checkfolders(self):
		'''
		making sure the folders for the classes exist
		'''
		for myclass in self.my_schedule.all_classes:
			if not os.path.isdir(os.path.join(default_dir, myclass.name)):
				os.mkdir(os.path.join(default_dir, myclass.name))
				print(f"{myclass.name} doesnt exist, creating.....")
	def findclosest(self, time_recording):
		'''
		given the time of the recording, find the closest class before the current time

		'''
		print(time_recording)
		print(type(time_recording))

		time_created = datetime.datetime.fromtimestamp(time_recording)#.strftime('%Y-%m-%d %H:%M:%S')
		print(time_created)
		print(time_created.weekday())

		for myclass in self.my_schedule.all_classes:
			if not time_created.weekday() in myclass.weekday:
				continue
			#print(time_created.timestamp())
			start_timestamp = myclass.start_time.timestamp() 
			stop_timestamp =  myclass.end_time.timestamp()
			rssvalue = ((time_created.timestamp() - start_timestamp)**2) + ((time_created.timestamp()-stop_timestamp)**2)
			print(f"{myclass.name} {s}")

		return "phydiss"

	def run(self):
		while True:
			files = glob.glob(os.path.join(default_dir, r"*.mp4"))
			if files:
				print("find files ", files)
				for file in files:
					time_created = os.path.getctime(file)
					folder = self.findclosest(time_created)
					#os.rename(file, os.path.join(os.path.join(default_dir, folder), f"{datetime.datetime.today().date()}.mp4"))
					exit()




	

if __name__ == "__main__":
	mysch = Scheduler()
	mysch.run()

