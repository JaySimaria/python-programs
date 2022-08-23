# 20-7-22
# handling missing keys
# creating a dictionary
country_code = {'India': '0091',
                'Russia': '0007',
                'Brazil': '0055'}
# searching a dictionary for  country code of india
print(country_code.get('India', 'Not Found'))
# searching a dictionary for  country code of brazil
print(country_code.get('Brazil', 'Not Found'))
# searching a dictionary for  country code of ukraine
print(country_code.get('Ukraine', 'Not Found'))



