from flask import Flask,redirect,url_for, render_template, Response
import time
import RPi.GPIO as GPIO          
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)

GPIO.output(13, GPIO.HIGH)


app = Flask(__name__)


def forward():
        GPIO.output(13, GPIO.LOW)
        GPIO.output(11, GPIO.LOW)

        

def backward():
        GPIO.output(13, GPIO.LOW)
        GPIO.output(11, GPIO.HIGH)

def left():
        pass

def right():
        pass

def stop():
        GPIO.output(13, GPIO.HIGH)

def changespeed():
        pass

@app.route('/')
def json():
    return render_template('json_old.html')


#background process happening without any refreshing
@app.route('/forward')
def f():
        forward()
        print("forward")
        return ""

@app.route('/reverse')
def b():
        backward();
        print("backward")
        return ""
        
        

@app.route('/stop')
def s():
        stop()
        print("stop")
        return ""
        

@app.route('/left')
def ll():
        left()
        print("left")
        return ""

@app.route('/right')
def rr():
        right()
        print("right")
        return ""


@app.route('/speed')
def sp():
        post = request.args.get('post', 0, type=int)
        #p.ChangeDutyCycle(post)
        changespeed(post)
        print("speed changed")
        return ""


if __name__ == "__main__":
	app.run(debug=True)