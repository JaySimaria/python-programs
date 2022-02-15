#converting lists into a dictionary
#take two separate lists with elements
countries=["USA","India","Germany","France"]
cities=['Washington','New Delhi','Berlin','Paris']

#make a dictionary
z=zip(countries,cities)
d=dict(z)

#display key- value pairs from dictionary d
print('{:15s} -- {:15s}'.format('COUNTRY','CAPITAL'))
for k in d:
    print('{:15s} -- {:15s}'.format(k, d[k]))
