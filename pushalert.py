#!/usr/bin/python2.7
#pushbullet python library - https://github.com/Azelphur/pyPushBullet
from pushbullet.pushbullet import PushBullet
import csv
import os, sys
import glob
import datetime as dt
from operator import sub
#emoji for python https://pypi.python.org/pypi/emoji
import emoji

#pushbullet api key
apiKey = "your pushbullet key"
pb = PushBullet(apiKey)

#grab and set device to push to
devices = pb.getDevices()
phone = devices[1]["iden"]

#get current date
date = dt.datetime.now().date()

#emoji cheatsheet at http://www.emoji-cheat-sheet.com/
meh = (emoji.emojize(':unamused:', use_aliases=True))
sweat = (emoji.emojize(':sweat:', use_aliases=True))
fear = (emoji.emojize(':fearful:', use_aliases=True))

'''
parse csv file
NOTE: csv file must be saved as windows comma seperated values format
	  Saving CSV on a windows machine should be ok but saving on Mac
	  or Linux seems to throw a weird error if not resaved as Windows format
'''
for name in glob.glob('csv/*.csv'):
	with open(name,'rb') as f:
		next(f) #skip header line
		reader = csv.reader(f)
		for row in reader:
			agent = row[0]
			portalName = row[1]
			portalLink = row[4]
			#convert to datetime object for day calculation
			portalBorn = dt.datetime.strptime(row[5], '%m/%d/%y').date()
			#subtract days and remove time method
			daysOld = (date - portalBorn).days

			#check to see if agent already has 150
			if daysOld >= 150:
				push = pb.pushNote(phone, agent, "Already has Onyx Guardian" + '\n' + meh)
				break
			#check to see if date is over 140
			elif daysOld >= 140 <= 149:
				#convert int to string for push
				stringDate = str(daysOld)
				push = pb.pushNote(phone, agent + " | " + portalName, portalLink + '\n' + "Onyx Alert! | Days Old: " + stringDate + " " + sweat)
			#check if portal is about to hit platinum
			elif daysOld >= 80 <= 89:
				stringDate = str(daysOld)
				push = pb.pushNote(phone, agent + " | " + portalName, portalLink + '\n' + "Plat Alert! | Days Old: " + stringDate + " " + fear)
