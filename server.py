from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
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


@app.route("/test/", methods=['GET'])
def get_params():
	begin_date = ''
	end_date = ''
	if(request.method == 'GET'):
		begin_date = request.args.get('begin')
		end_date = request.args.get('end')
	dates = json.dumps({'begin':begin_date, 'end':end_date})
	accidents = TrafficAccident.query.all()
	return accidents[0].district

if __name__ == '__main__':
	db.create_all()
	app.run()