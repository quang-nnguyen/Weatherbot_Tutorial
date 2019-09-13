from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import requests


ACCESS_KEY = '...' #your apixu key


def getweather(location='Boston'):

	params = {
		'access_key': ACCESS_KEY,
		'query': location
	}

	api_result = requests.get('http://api.weatherstack.com/current', params)

	api_response = api_result.json()

	return api_response


class ActionWeather(Action):
	def name(self):
		return 'action_weather'
		
	def run(self, dispatcher, tracker, domain):
		# from apixu.client import ApixuClient
		# api_key = '42a1e2a273a3626db124c9b032710158' #your apixu key
		# client = ApixuClient(api_key)
		
		loc = tracker.get_slot('location')
		# current = client.getcurrent(q=loc)
		current = getweather(loc)
		
		country = current['location']['country']
		city = current['location']['name']

		#condition = current['current']['condition']['text']
		condition = current['current']['weather_descriptions']

		temperature_c = current['current']['temperature']
		humidity = current['current']['humidity']
		wind_mph = current['current']['wind_speed']

		response = """It is currently {} in {} at the moment. The temperature is {} degrees, the humidity is {}% and the wind speed is {} mph.""".format(condition, city, temperature_c, humidity, wind_mph)
						
		dispatcher.utter_message(response)
		return [SlotSet('location',loc)]