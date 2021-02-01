from flask import Flask,redirect,url_for, render_template,request
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
my_pwm=GPIO.PWM(11,100)
my_pwm.start(50)

post = 0

app = Flask(__name__)

@app.route('/')
def json():
    return render_template('json.html')

#background process happening without any refreshing
@app.route('/forward',methods=['GET','POST'])
def f():
    global post
    prev_post = post
    post = request.args.get('post', 0, type=int)

    if post>prev_post:
        print("increasing speed from"+str(prev_post)+"to"+str(post))
        for x in range(prev_post,post):
            print("Setting speed to:"+str(x))
            my_pwm.ChangeDutyCycle(x)
            time.sleep(.1)
    if post<prev_post:
        print("decreasing speed from"+str(prev_post)+"to"+str(post))
        for x in range(prev_post,post,-1):
            print("Setting speed to:"+str(x))
            my_pwm.ChangeDutyCycle(x)
            time.sleep(.1)
    
    return ("nothing")


if __name__ == "__main__":
    app.run()
