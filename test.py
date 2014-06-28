import requests
import json


json_header = {'content-type': 'application/json'}

# url = 'http://ec2-54-183-120-129.us-west-1.compute.amazonaws.com:5000/'
url = 'http://localhost:5000/'
work_path = 'work/'
code_path = 'code/'

device_ids = ['ffffffff-f65a-d3c4-ffff-ffffeb5b48c0',
              'gggggggg-g65a-d3c4-gggg-ggggeb5b48c0']

code_maps = [{'data': [x for x in range(100)], 'code': 'lambda x: x + 1'}]


def add_device(device_id):
    device_data = {'id': device_id}
    r = requests.post(url=url + work_path,
                      params=device_data, headers=json_header)
    print r.text


def add_code(code_map):
    r = requests.post(url=url + code_path,
                      data=json.dumps(code_map),
                      headers=json_header)
    print r.text

map(add_device, device_ids)
map(add_code, code_maps)
