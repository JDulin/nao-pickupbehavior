#
# Summer at the Edge 2012 Project: Humanoid Robotics with NAO
# John Dulin, Case Western Reserve University
# July 11, 2012 
#
# Record the positions of all 11 joints from the robot's lower body over the course of a 2 meter walk.
# The recording is over the duration of the command ALMotion.walkTo(2.0, 0.0, 0.0) 
# May be too CPU intensive to collect all of these values on the robot (run remotely?)

AL_MEMORY_VALUES = [
"Device/SubDeviceList/LHipYawPitch/Position/Actuator/Value",
"Device/SubDeviceList/LHipYawPitch/Position/Sensor/Value",
"Device/SubDeviceList/LHipYawPitch/Hardness/Actuator/Value",
"Device/SubDeviceList/LHipYawPitch/ElectricCurrent/Sensor/Value",
"Device/SubDeviceList/LHipRoll/Position/Actuator/Value",
"Device/SubDeviceList/LHipRoll/Position/Sensor/Value",
"Device/SubDeviceList/LHipRoll/Hardness/Actuator/Value",
"Device/SubDeviceList/LHipRoll/ElectricCurrent/Sensor/Value",
"Device/SubDeviceList/RHipRoll/Position/Actuator/Value",
"Device/SubDeviceList/RHipRoll/Position/Sensor/Value",
"Device/SubDeviceList/RHipRoll/Hardness/Actuator/Value",
"Device/SubDeviceList/RHipRoll/ElectricCurrent/Sensor/Value",
"Device/SubDeviceList/LHipPitch/Position/Actuator/Value",
"Device/SubDeviceList/LHipPitch/Position/Sensor/Value",
"Device/SubDeviceList/LHipPitch/Hardness/Actuator/Value",
"Device/SubDeviceList/LHipPitch/ElectricCurrent/Sensor/Value",
"Device/SubDeviceList/LKneePitch/Position/Actuator/Value",
"Device/SubDeviceList/LKneePitch/Position/Sensor/Value",
"Device/SubDeviceList/LKneePitch/Hardness/Actuator/Value",
"Device/SubDeviceList/LKneePitch/ElectricCurrent/Sensor/Value",
"Device/SubDeviceList/RHipPitch/Position/Actuator/Value",
"Device/SubDeviceList/RHipPitch/Position/Sensor/Value",
"Device/SubDeviceList/RHipPitch/Hardness/Actuator/Value",
"Device/SubDeviceList/RHipPitch/ElectricCurrent/Sensor/Value",
"Device/SubDeviceList/RKneePitch/Position/Actuator/Value",
"Device/SubDeviceList/RKneePitch/Position/Sensor/Value",
"Device/SubDeviceList/RKneePitch/Hardness/Actuator/Value",
"Device/SubDeviceList/RKneePitch/ElectricCurrent/Sensor/Value",
"Device/SubDeviceList/LAnklePitch/Position/Actuator/Value",
"Device/SubDeviceList/LAnklePitch/Position/Sensor/Value"
"Device/SubDeviceList/LAnklePitch/Hardness/Actuator/Value",
"Device/SubDeviceList/LAnklePitch/ElectricCurrent/Sensor/Value",
"Device/SubDeviceList/LAnkleRoll/Position/Actuator/Value",
"Device/SubDeviceList/LAnkleRoll/Position/Sensor/Value",
"Device/SubDeviceList/LAnkleRoll/Hardness/Actuator/Value",
"Device/SubDeviceList/LAnkleRoll/ElectricCurrent/Sensor/Value",
"Device/SubDeviceList/RAnklePitch/Position/Actuator/Value",
"Device/SubDeviceList/RAnklePitch/Position/Sensor/Value",
"Device/SubDeviceList/RAnklePitch/Hardness/Actuator/Value",
"Device/SubDeviceList/RAnklePitch/ElectricCurrent/Sensor/Value",
"Device/SubDeviceList/RAnkleRoll/Position/Actuator/Value",
"Device/SubDeviceList/RAnkleRoll/Position/Sensor/Value",
"Device/SubDeviceList/RAnkleRoll/Hardness/Actuator/Value",
"Device/SubDeviceList/RAnkleRoll/ElectricCurrent/Sensor/Value"
]

import os
import sys
import time

from naoqi import ALProxy

IP = "nao.local"
PORT = 9559

def recordData(nao_ip):
	""" Records data from the specified robot on the memory values from AL_MEMORY_VALUES """

	memory = ALProxy("ALMemory", nao_ip, PORT)
	data = list()
	
	for i in xrange(1, 200):	
		line = list()
		for key in AL_MEMORY_VALUES:
			value = memory.getData(key)		
			line.append(value)
		data.append(line)
		time.sleep(0.1)
	return data

def main():
	""" Direct the robot to walk straight, run recordData, and write the collected data to a csv file. """

	if len(sys.argv) < 2:
		nao_ip = IP
	else:
		nao_ip = sys.argv[1]

	motion = ALProxy("ALMotion", nao_ip, PORT)	
	motion.setStiffnesses("Body", 1.0)
	motion.post.walkTo(2.0, 0.0, 0.0)
	
	data = recordData(nao_ip)

	output = os.path.abspath("walk.csv")
		
	with open(output, "w") as file:
		for line in data:
			file.write("; ".join(str(x) for x in line))
			file.write("\n")
	
	print "Results written to ", output

if __name__ == "__main__":
	# This is a hack to make sure I am in position to safely watch and protect the robot while it walks.
	time.sleep(10)
	main() 

