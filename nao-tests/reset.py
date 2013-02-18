#
# Summer at the Edge 2012 Project: Humanoid Robotics with NAO
# John Dulin, Case Western Reserve University
# August 3, 2012
#
# This simple script resets the robot after an error.  It removes motor stiffness and stops the tracker.
# This should only be ran when someone is ready to catch the robot when it falls.
#

from naoqi import ALProxy

motion = ALProxy("ALMotion", "127.0.0.1", 9559)
tracker = ALProxy("ALRedBallTracker", "127.0.0.1", 9559)

tracker.stopTracker()
motion.setStiffnesses("Body", 0)
