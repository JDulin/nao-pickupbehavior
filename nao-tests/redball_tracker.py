# This is a testbed for the NAO's funcitonality tracking a red ball using
# the ALRedBallTracker.py module.
# John Dulin
# July 9, 2012

import sys
import time
from naoqi import ALProxy

IP = "127.0.0.1"
PORT = "9559"

speech = ALProxy("ALTextToSpeech", IP, PORT)
motion = ALProxy("ALMotion", IP, PORT)
tracker = ALProxy("ALRedBallTracker", IP, PORT)

# First, set the head stiffness to on.
motion.setStiffnesses("Head", 1.0)

# Then, start the tracker.
tracker.startTracker()

print "Tracker started successfully, now show a ball to Nao!"
speech.say("Show a ball to me!")
print "The tracker will stop in 60 seconds"

time.sleep(60)

print "Tracker is stopping..."
speech.say("Alright, I'm tired of that.")
tracker.stopTracker()
motion.setStiffnesses("Head", 0.0)
