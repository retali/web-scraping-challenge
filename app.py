from flask import Flask, render_template, redirect, request 
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

    mission_to_mars = mongo.db.mission_to_mars.find_one()
    return render_template("index.html", mission_to_mars = mission_to_mars)
    
@app.route("/")
def scrape():

    # Run the scrape function
    mission_to_mars = mongo.db.mission_to_mars
    data_web = scrape_mars.scrapeNews()
    data_web = scrape_mars.scrapeImage()
    data_web = scrape_mars.scrapeFacts()
    data_web = scrape_mars.scrape_Cerberus()
    data_web = scrape_mars.scrape_Schiaparelli()
    data_web = scrape_mars.scrape_yrtisMajor()
    data_web = scrape_mars.scrape_VallesMarineris()
    
    # Update Database
    mars.update({}, data_web, upsert=True)
    
    # Back to home page
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)
