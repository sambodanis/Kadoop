import requests

json_header = {'content-type': 'application/json'}

url = 'http://ec2-54-183-120-129.us-west-1.compute.amazonaws.com:5000/'
# url = 'http://localhost:5000/work'
data = {'id': 'ffffffff-f65a-d3c4-ffff-ffffeb5b48c0'}
r = requests.post(url=url + 'work/',
                  data=data, headers=json_header)
print r.text
