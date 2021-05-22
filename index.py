from flask import Flask,render_template 


app = Flask(__name__)

@app.route('/')
def home():
  return render_template('home.html')
 
@app.route('/')
def about():
  return 'About page'

if __name__ == '__name__':
  app.run(debug=True)
  
