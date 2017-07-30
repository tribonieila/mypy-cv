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

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
   app.run(host='0.0.0.0', port=port, debug = True)
