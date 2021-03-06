from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/home')
def home():
   return render_template('home.html')

@app.route('/experience')
def experience():
   return render_template('experience.html')

@app.route('/expertise')
def expertise():
   return render_template('expertise.html')

@app.route('/projects')
def projects():
   return render_template('projects.html')

@app.route('/education')
def education():
   return render_template('education.html')

if __name__ == '__main__':
   app.run(debug = True)
