import requests

json_header = {'content-type': 'application/json'}

r = requests.post(url='http://localhost:5000/work',
                  data={'key': 'value'}, headers=json_header)
print r.text
