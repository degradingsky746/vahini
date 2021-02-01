import picar
from picar import front_wheels,back_wheels 
import time

picar.setup()
speed = 20
fw = front_wheels.Front_Wheels(db='config')
bw = back_wheels.Back_Wheels(db='config')
angle = 90
l_angle = 0
r_angle = 0

def forward():
	bw.forward()
	bw.speed=speed

def reverse():
	bw.backward()
	bw.speed=speed

def left():
	global l_angle
	l_angle+=20
	if 90-l_angle<30:
		l_angle=60
	fw.turn(90-l_angle)

def right():
	globla r_angle
	r_angle+=20
	if 90+angle>150:
		r_angle=60
	fw.turn(90+r_angle)

def stop():
	bw.stop()
	fw.turn(90)


while True:
	command = input()
	if command == "f":
		forward()
	elif command == "r":
		reverse()
	elif command == "s":
		stop()
	elif command == "l":
		left()
	elif command == "r":
		right()