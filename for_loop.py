# 30-1-23
# for loop
forecast = {'Mon': 'Rainy', 'Tues': 'Partly Cloudy', 'Wed': 'Sunny', 'Thu': 'Windy', 'Fri': 'Warm', 'Sat': 'Hot',
            'Sun': 'Clear'}

for day, weather in forecast.items():
    print(day + ' will be ' + weather)