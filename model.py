from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
connection_string = 'mysql://root:12345678@167.99.192.185:3306/tulasafewalk'
app.config['SQLALCHEMY_DATABASE_URI'] = connection_string
db = SQLAlchemy(app)

class TrafficAccident(db.Model):
	__tablename__ = 'TrafficAccidents'
	id = db.Column('id', db.Integer, primary_key = True)
	date = db.Column(db.Integer)
	latitude = db.Column(db.Float)
	longitude = db.Column(db.Float)
	district = db.Column(db.String(30))
	accident_type =  db.Column(db.String(80))

	def __init__(self, date, latitude, longitude, district, accident_type):
		self.date = date
		self.latitude = latitude
		self.longitude = longitude
		self.district = district
		self.accident_type = accident_type

	def as_json(self):
		return dict(
			input_id=self.id, date = self.date,
			latitude = self.latitude, 
			longitude = self.longitude,
			district = self.district,
			accident_type = self.accident_type)

	def coordinates_as_json(self):
		return dict( position = {
				'lat' : self.latitude, 
				'lng' : self.longitude
			}
		)