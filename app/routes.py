from flask import render_template, request, redirect
from app import app
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    user={"month":"stone"} 
    return render_template('index.html')
    
def results():
    return render_template('results.html')
    
@app.route("/sendMonth", methods=["GET", "POST"])
def handle_birthstone():
    if request.method == "GET":
        return "This is your bstone"
    else:
        user_data= request.form
        print(user_data)
        month = user_data["month"]
        print(month)
        birthstone = model.give(month)
        print(birthstone)
        #give_stone = model.give(stone)
        return render_template ("results.html", user_data = birthstone )

