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
apiKey = "UcQfHx7Wd2Pz0CwbtTeRvS9TFhniPxgH"
pb = PushBullet(apiKey)

#grab and set device to push to
devices = pb.getDevices()
phone = devices[1]["iden"]

pb.pushNote(phone, "What you need to clear", "Jarvis Coast to Crest Trail" + '\n' + "https://www.ingress.com/intel?ll=33.067689,-117.065426&z=17&pll=33.067689,-117.065426" + '\n' + "Jarvis Mule Hill Trail" + '\n' + "https://www.ingress.com/intel?ll=33.066623,-117.06773&z=17&pll=33.066623,-117.06773" + '\n' + "Destroy Del Lago Transit Station" +'\n' + "https://www.ingress.com/intel?ll=33.071919,-117.071246&z=17&pll=33.071919,-117.071246" + '\n' + "Destroy Felicita Park" + '\n' + "https://www.ingress.com/intel?ll=33.080889,-117.083148&z=17&pll=33.080889,-117.083148" + '\n' + "Destroy The Church Of Latter Day Saints" + '\n' + "https://www.ingress.com/intel?ll=33.092688,-117.085975&z=17&pll=33.092688,-117.085975" + '\n' + "Destroy Self Realization Fellowship" + '\n' + "https://www.ingress.com/intel?ll=33.103015,-117.102485&z=17&pll=33.103015,-117.102485" + '\n' + "Destroy Diablo Park Entrance" + '\n' "https://www.ingress.com/intel?ll=33.101994,-117.107791&z=17&pll=33.101994,-117.107791" + '\n' + "Link Ridgeline Trailhead" + '\n' + "https://www.ingress.com/intel?ll=33.107485,-117.166221&z=17&pll=33.107485,-117.166221" + '\n' + "Destroy Rancho Santa Fe Post Office" + '\n' + "https://www.ingress.com/intel?ll=33.018768,-117.202263&z=17&pll=33.018768,-117.202263" + '\n' + "Destroy Rancho Santa Fe Public Library" + '\n' + "https://www.ingress.com/intel?ll=33.020933,-117.205221&z=17&pll=33.020933,-117.205221" + '\n' + "Destroy Ewing Preserve" + '\n' + "https://www.ingress.com/intel?ll=33.015215,-117.214162&z=17&pll=33.015215,-117.214162" + '\n' + "Link El Camino Bell" + '\n' + "https://www.ingress.com/intel?ll=33.010593,-117.240016&z=17&pll=33.010593,-117.240016")

pb.pushNote(phone, "What they need to clear", "4S Vase Overflowing" + '\n' + "https://www.ingress.com/intel?ll=33.020522,-117.112232&z=17&pll=33.020522,-117.112232" + '\n' + "Karl Strauss Brewery" + '\n' + "https://www.ingress.com/intel?ll=33.02133,-117.113302&z=17&pll=33.02133,-117.113302")