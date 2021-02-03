# Gruik coded by GuiguiAbloc
import flask
import time
import keyboard
app = flask.Flask(__name__)


@app.route('/')
def index():
  return 'Server Works!'
 
@app.route('/camera/pause')
def campause():
  try:
      keyboard.press_and_release('p')
      return("ok") 
  except:
      print("Error")
      return "Error"

@app.route('/camera/resume')
def camresume():
  try:
      keyboard.press_and_release('r')
      return("ok") 
  except:
      print("Error")
      return "Error"


@app.route('/camera/1')
def cam1():
  try:
      keyboard.press_and_release('F1')
      return("ok") 
  except:
      print("Error")
      return "Error"

@app.route('/camera/2')
def cam2():
  try:
      keyboard.press_and_release('F2')
      return("ok") 
  except:
      print("Error")
      return "Error"

@app.route('/camera/3')
def cam3():
  try:
      keyboard.press_and_release('F3')
      return("ok") 
  except:
      print("Error")
      return "Error"
      
@app.route('/camera/4')
def cam4():
  try:
      keyboard.press_and_release('F4')
      return("ok") 
  except:
      print("Error")
      return "Error"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)

