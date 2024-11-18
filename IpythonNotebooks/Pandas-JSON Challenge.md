# Challenge - parse json file into a Pandas dataframe

Using JSON data file: "https://raw.githubusercontent.com/stevewatkins17/PythonForDataAnalysis/refs/heads/mainline/Data/nws_weather_4HourForecast.json"

Display the following dataframe (in index sort order)

	startTime	                shortForecast	temperature	probabilityOfPrecipitation	relativeHumidity	dewpoint
0	2024-11-16T11:00:00-05:00	Partly Sunny	51	        0	                        71	                5.555556
1	2024-11-16T12:00:00-05:00	Partly Sunny	53	        0	                        69	                6.111111
2	2024-11-16T13:00:00-05:00	Partly Sunny	54	        0	                        69	                6.666667
3	2024-11-16T14:00:00-05:00	Partly Sunny	54	        0	                        66	                6.111111

## Suggested pre-requisites
- Create a new python project in vscode 
- create a virtual (venv) environment for your project
- Create a new jupyter notebook that uses the new venv as its kernal

## steps
- Download JSON file "nws_weather_4HourForecast.json" to the root directory of your python project.
- Import the json file into a Python dictionary.
- Iterate through the "Properties" key, loading keys and values into a Pandas dataframe 
- Display as a table the following columns:
  "startTime" ,"shortForecast" ,"temperature" ,"probabilityOfPrecipitation" ,"relativeHumidity"

# More Challenge
The above not enough for you? Try these:
- download the JSON file directly into your Jupyter notebook by making a URL request to the address shown above
- rename columns to shorter, easier-to-display names
- reformat the datetime value to something easier to read for someone in its offset timezone (US Eastern)
- convert the dewpoint's Celsius value to Fahrenheit
- concatenate columns "temperature" and "temperatureUnit" so that the reader better understands the "temperature" value
- use a json datafile that you download directly from the source "https://api.weather.gov"
