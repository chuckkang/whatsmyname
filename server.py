from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")

first_name=''
@app.route('/submit', methods=['POST'])
def submit_form():
  first_name = request.form["first_name"]
  print first_name
  return render_template("results.html", fname=first_name)






app.run(debug=True) # run our server