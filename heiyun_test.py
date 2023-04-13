import base64
import filecmp
import json
import os
from time import sleep

import pandas as pd
import requests
from deepdiff import DeepDiff

api = "http://192.168.0.115:6274"
token_api = "http://192.168.0.115:31004"


def get_login_token():
    url = f"{token_api}/v1/token"
    payload = json.dumps(get_login_info())
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    token = response.json()["token"]
    token = f'Bearer {token}'
    return token


def get_login_info():
    return {
        "email": "admin@heiyunkeji.com",
        "password": "e10adc3949ba59abbe56e057f20f883e"
    }


def test_getOCR():
    url = f"{api}/get-key-files"
    payload = json.dumps({
        "workspace": "testApi",
        "key": "testApi",
        "filenames": [
            "raw.txt"
        ]
    })
    headers = {
        'x-auth-key': get_login_token(),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    res = response.json()['raw.txt']
    with open("res/raw.txt", "r", encoding='utf-8') as f:
        data = f.read()
    assert res == data


def test_getOCR_entity():
    url = f"{api}/get-key-files"
    payload = json.dumps({
        "workspace": "testApi",
        "key": "testApi",
        "filenames": [
            "raw.txt",
            "entity_extraction.tag.json"
        ]
    })
    headers = {
        'x-auth-key': get_login_token(),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    res1 = response.json()['raw.txt']
    res2 = response.json()['entity_extraction.tag.json']
    with open("res/raw.txt", "r", encoding='utf-8') as f:
        data1 = f.read()
    assert res1 == data1

    with open("res/entity_extraction.tag.json", 'r', encoding='utf-8') as f:
        data2 = json.load(f)
    assert res2 == data2


def test_formOCR():
    url = f"{api}/get-key-files"
    payload = json.dumps({
        "workspace": "testApi",
        "key": "testApi",
        "filenames": [
            "dag.json",
            "classify_table.tag.json"
        ]
    })
    headers = {
        'x-auth-key': get_login_token(),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    res1 = response.json()['dag.json']
    res2 = response.json()['classify_table.tag.json']
    with open("res/dag.json", 'r', encoding='utf-8') as f:
        data1 = json.load(f)
    assert res1 == data1

    with open("res/classify_table.tag.json", 'r', encoding='utf-8') as f:
        data2 = json.load(f)
    assert res2 == data2


def test_getpic_getOCR():
    url = f"{api}/list-folders"
    payload = json.dumps({
        "workspace": "testApi",
        "key": "testApi",
        "path": "image_elements"
    })
    headers = {
        'x-auth-key': get_login_token(),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    with open("res/file_list.json", "r", encoding='utf-8') as f:
        data = json.load(f)
    assert response.json().sort() == data.sort()

    url = f"{api}/get-key-files"
    filenames_list = []
    for name in data:
        filenames_list.append("image_elements/" + name + "/raw.jpg")
    payload = json.dumps({
        "workspace": "testApi",
        "key": "testApi",
        "filenames": filenames_list
    })
    headers = {
        'x-auth-key': get_login_token(),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    with open("res/img_base64.json", "r", encoding='utf-8') as f:
        data = json.load(f)
    assert response.json() == data

    # 解码并保存文件
    # for key in data.keys():
    #     decoded = data[key]
    #     decoded = decoded.encode('raw_unicode_escape')  # str转bytes
    #     decoded = base64.b64decode(decoded)
    #     file_name = "res/img/" + key.replace('/', '_')
    #     with open(file_name, 'wb') as wf:
    #         wf.write(decoded)

    url = f"{api}/get-key-files"
    payload = json.dumps({
        "workspace": "testApi",
        "key": "testApi",
        "filenames": [
            "classify_pdf_image_element.tag.json"
        ]
    })
    headers = {
        'x-auth-key': get_login_token(),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    with open("res/classify_pdf_image_element_tag.json", "r", encoding='utf-8') as f:
        data = json.load(f)
    assert response.json() == data


def test_download_category_folder():
    url = f"{api}/download-image-elements"
    payload = json.dumps({
        "workspace": "testApi",
        "key": "testApi"
    })
    headers = {
        'x-auth-key': get_login_token(),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    with open("res/zip_base64.txt", 'w', ) as f:
        f.write(response.text[1:-1])
    with open("res/res_zip.zip", 'wb') as f:
        f.write(base64.b64decode(response.text[1:-1]))
    assert filecmp.cmp('res/standard_zip.zip', 'res/res_zip.zip')


def test_download_table_tag():
    url = f"{api}/download-table-tag"

    payload = json.dumps({
        "workspace": "testApi",
        "key": "exportExcel",
    })
    headers = {
        'x-auth-key': get_login_token(),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    with open("res/export_excel.xlsx", 'wb') as f:
        f.write(base64.b64decode(response.json()))
    df1 = pd.read_excel('res/export_excel.xlsx')
    df2 = pd.read_excel('res/standard_excel.xlsx')
    assert DeepDiff(df1, df2) == {}
