from flask import Flask,redirect,url_for, render_template
import picar
from picar import front_wheels,back_wheels 
import time

picar.setup()
fspeed = 0
rspeed = 0
fw = front_wheels.Front_Wheels(db='config')
bw = back_wheels.Back_Wheels(db='config')

l_angle = 0
r_angle = 0

def forward():
        global fspeed
        global rspeed
        rspeed = 0
        fspeed+=20
        if fspeed>90:
                fspeed=90
        bw.forward()
        bw.speed=fspeed

def reverse():
        global fspeed
        global rspeed
        fspeed=0
        rspeed+=20
        if rspeed>90:
                rspeed=90
        bw.backward()
        bw.speed=rspeed

def left():
        global r_angle
        global l_angle
        r_angle=0
        l_angle+=20
        if 90-l_angle<50:
                l_angle=40
        fw.turn(90-l_angle)

def right():
        global r_angle
        global l_angle
        l_angle=0
        r_angle+=20
        if 90+r_angle>130:
                r_angle=40
        fw.turn(90+r_angle)

def stop():
        bw.stop()
        fw.turn(90)x`


app = Flask(__name__)

@app.route('/')
def json():
    return render_template('json.html')

#background process happening without any refreshing
@app.route('/forward')
def f():
    forward()
    return ("nothing")

@app.route('/reverse')
def r():
    reverse()
    return ("nothing")

@app.route('/stop')
def s():
    stop()
    return ("nothing")

@app.route('/left')
def l():
    left()
    return ("nothing")

@app.route('/right')
def r():
    right()
    return ("nothing")


if __name__ == "__main__":
	app.run()
