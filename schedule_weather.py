"""
Written 07/03/2014
Schedule runs for script that parses MMDA-Interaksyon webpage for traffic status. 
"""

from numpy import *
import sched
import time
import os

scheduler=sched.scheduler(time.time,time.sleep)

def run_script():
	fn_script="weather.py"
	minutes=float(time.strftime("%M"))
	tstr=time.strftime("%Y%m%d")+"_"+time.strftime("%H")+"_%d" % (minutes/15+1)
	fn_out="output/status_%s.csv" % (tstr) # 4th quarter of 21st hour of this day
	print ("Start: "+time.strftime("%x")+" "+time.strftime("%X"))
	print ("Running: python3 %s %s" % (fn_script, fn_out))
	os.system("python3 %s %s" % (fn_script, fn_out))
	print ("Done: "+time.strftime("%x")+" "+time.strftime("%X"))

for i in arange(24): # for next 6 hours
	#scheduler.enter(0,1,run_script,'') # delay time in seconds
	scheduler.enter(i*15*60,1,run_script,'') # run every 15 minutes

scheduler.run()