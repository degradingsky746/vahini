from flask import Flask,redirect,url_for, render_template,request
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
my_pwm=GPIO.PWM(11,100)
my_pwm.start(50)

app = Flask(__name__)

@app.route('/')
def json():
    return render_template('json.html')

#background process happening without any refreshing
@app.route('/forward',methods=['GET','POST'])
def f():
    post = request.args.get('post', 0, type=int)
    print(post)
    my_pwm.ChangeDutyCycle(post%100)
    return ("nothing")


if __name__ == "__main__":
    app.run()
