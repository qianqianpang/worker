# -- coding: utf-8 --**
import json
import os

import PyPDF2
import docx
import requests


def detect_file_type(path):
    file = os.path.splitext(path)
    filename, type = file
    if 'pdf' in type:
        return 'PDF'
    elif 'docx' in type or 'doc' in type:
        return 'Word'
    elif 'txt' in type:
        return 'TXT'
    else:
        return 'Unknown'


def read_file(type, path):
    text = ''
    if type == 'PDF':
        with open(path, 'rb') as file:
            pdf = PyPDF2.PdfReader(file)
            for page in range(len(pdf.pages)):
                text += pdf.pages[page].extract_text()
    elif type == 'Word':
        doc = docx.Document(path)
        for paragraph in doc.paragraphs:
            text += paragraph.text
    else:
        with open(path, 'r') as file:
            text = file.read()
    return text


def request(content, language, lib='*'):
    if lib != '*':
        question = "根据以下文档撰写测试代码，要求：保证代码的正确性、简洁性，使用{}语言，指定库{}，关键代码请给出注释，用MarkDown格式输出。文档如下：{}".format(
            language, lib, content)
    else:
        question = "根据以下文档撰写测试代码，要求：保证代码的正确性、简洁性，使用{}语言，关键代码请给出注释，用MarkDown格式输出。文档如下：{}".format(
            language, content)
    os.environ['no_proxy'] = '190.92.219.187'
    url = "http://190.92.219.187:31698/openai/v1/chat/completions"
    payload = json.dumps({
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "user",
                "content": question
            }
        ]
    })
    headers = {
        'Authorization': 'Bearer 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',
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return json.loads(response.text)['choices'][0]['message']['content'].strip()


if __name__ == '__main__':
    file_path = input("Please enter a path(absolute path): ")
    language = input("Please enter a language(python/JS/java/c++,etc): ")
    lib = input("Please enter a specified library(optional...): ")

    file_type = detect_file_type(file_path)
    content = read_file(file_type, file_path)
    result = request(content, language, lib)
    print("res:{}".format(result))
