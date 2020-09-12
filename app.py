from flask import Flask 
from flask import render_template
from flask import redirect
from flask import request
from flask_pymongo import PyMongo
import scrape_mars
from pymongo import MongoClient
import pymongo

# Create an instance of Flask
app = Flask(__name__)

# setup mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mission_to_mars"
mongo = PyMongo(app)

# Route to render index.html template using data from Mongo
@app.route("/")
def index():

    mission_to_mars_db = mongo.db.mission_to_mars.find_one()
    return render_template("index.html", mission_to_mars = mission_to_mars_db)
    
@app.route("/scrape")
def scrape():

    # Run the scrape function
    data_web = scrape_mars.scpeNews()
    data_web = scrape_mars.scpeImage()
    data_web = scrape_mars.scpeFacts()
    data_web = scrape_mars.scpe_Cerberus()
    data_web = scrape_mars.scpe_Schiaparelli()
    data_web = scrape_mars.scpe_yrtisMajor()
    data_web = scrape_mars.scpe_VallesMarineris()
    
    # Update Database
     mongo.db.mission_to_mars_db.update({},data_web,upsert=True)
    # Back to home page
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)
