# 17-1-23
# merge two dictionaries
D1 = {'name': 'Jay',
      'age': 25,
      'job': 'Devops engineer',
      'salary': '300000'
      }

D2 = {'Name': 'Messi',
      'age': 30,
      'city': 'Argentina',
      'email': 'lionMessi@gmail.com',
      'profession': 'footballer'}

D1.update(D2)
print(D1)
