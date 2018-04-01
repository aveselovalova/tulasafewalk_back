from flask import request
import json
from model import TrafficAccident, app, db

@app.route("/get-data/", methods=['GET'])
def main():
	begin_date = ''
	end_date = ''
	if(request.method == 'GET'):
		begin_date = request.args.get('begin')
		end_date = request.args.get('end')

	return get_coordinates(begin_date, end_date)

def select_data(begin_date, end_date):
	return TrafficAccident.query.filter(
			TrafficAccident.date >= begin_date,
			TrafficAccident.date <= end_date,
		).all()

def get_coordinates(begin_date, end_date):
	accidents = select_data(begin_date, end_date)
	results = [json.dumps(accident.coordinates_as_json(), ensure_ascii=False) for accident in accidents]
	return json.dumps(results, ensure_ascii=False)


if __name__ == '__main__':
	db.create_all()
	app.run(host="0.0.0.0")
