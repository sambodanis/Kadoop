# from requests_toolbelt import MultipartEncoder
import requests
import json


json_header = {'content-type': 'application/json'}

# url = 'http://ec2-54-183-120-129.us-west-1.compute.amazonaws.com/'
url = 'http://localhost:5000/'
work_path = 'work/'
code_path = 'code/'

device_ids = ['ffffffff-f65a-d3c4-ffff-ffffeb5b48c0',
              'gggggggg-g65a-d3c4-gggg-ggggeb5b48c0']

# code_maps = [{'data': [1, 2, 3], 'code': 'lambda x: x + 1'}]
code_maps = [{'data': 'data.json', 'code': 'lambda x: x + 1'}]


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


# def add_code_file(code_map):
#     fields = {}
#     file_path = code_map['data']
#     fields['file'] = (file_path, open(
#         file_path, 'rb'), guess_type(file_path)[0])
#     fields['code'] = code_map['code']
#     m = MultipartEncoder(fields=tb_fields)
#     r = requests.post(url=url + code_path,
#                       data=m, headers={'Content-Type': m.content_type})
#     print r.text


map(add_device, device_ids)
map(add_code, code_maps)
