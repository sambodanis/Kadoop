import requests

json_header = {'content-type': 'application/json'}

url = 'http://ec2-54-183-120-129.us-west-1.compute.amazonaws.com/'
# url = 'http://localhost:5000/work'

r = requests.post(url=url,
                  data={'key': 'value'}, headers=json_header)
print r.text
