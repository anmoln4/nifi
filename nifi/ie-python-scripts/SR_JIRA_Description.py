#!/usr/bin/python3

import sys
import json

flowFile = session.get()
if flowFile is not None:
    json_content = flowFile.read().decode('utf-8')
    json_array = json.loads(json_content)
    sorted_data = sorted(data, key=lambda x: x['questionSequence'])
    description = ""
    for item in sorted_data:
        description += f"{item['question']} \n {item['answer']} \n"
    print(description)