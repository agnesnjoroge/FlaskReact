from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return "python flask django"

if __name__ == '__main__':
   app.debug = True
   app.run()
   app.run(debug = True)
   