from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/feedback')
 #function for log in to take admin to feedback page

 #function to add feedback to feedback page. 

app.run(host='0.0.0.0',port=8080)