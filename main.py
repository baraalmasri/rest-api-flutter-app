from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from serpapi import GoogleSearch
from urllib.request import urlopen
import json

app = Flask(__name__)

app.config['PROPAGATE_EXCEPTIONS'] = True  # To allow flask propagating exception even if debug is set to false on app
app.secret_key = 'jose'
api = Api(app)


class job(Resource):
    def get(self, lng, name):
        params = {
            "engine": "google_jobs",
            "q": name,
            "hl": lng,
            "api_key": "03cd7f29ab888025430b062a8137136ad624e7b732ee223eeff46d5e9f6541be"
        }

        search = GoogleSearch(params)
        results = search.get_dict()
        jobs_results = results['jobs_results']
        return jobs_results

class corona_cases(Resource):

    def get(self, country):
        response = urlopen(f"https://covid-19.dataflowkit.com/v1/{country}")
        data_json = json.loads(response.read())
        return data_json


api.add_resource(job, '/job/<string:lng>/<string:name>')
api.add_resource(corona_cases, '/corona_cases/<string:country>')

if __name__ == '__main__':
    app.run(debug=True)  # important to mention debug=True
