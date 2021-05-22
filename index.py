from flask import Flask 

app = Flask(__name__)

@app.route('/')
def home():
  return 'Home page'
 
@app.route('/')
def about():
  return 'About page'

if __name__ == '__name__':
  app.run()
  
