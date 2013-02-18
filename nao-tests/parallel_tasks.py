# John Dulin
# July 6, 2012
# Testing module for parallel tasks on the NAO

import time
from naoqi import ALProxy

motion = ALProxy("ALMotion")
speech = ALProxy("ALTextToSpeech")

motion.setStiffnesses("Body", 1.0)

motion.walkInit()
motion.post.walkTo(0.5,0,0)
speech.say("I'm walking")

speech.say("I'm going to shut off my motors, make sure I don't fall!")
time.sleep(3)
motion.setStiffnesses("Body", 0.0) 
