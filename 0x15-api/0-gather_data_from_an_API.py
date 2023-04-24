#!/usr/bin/python3

'''
...
'''
import requests
import sys
import json

todos_url = "https://jsonplaceholder.typicode.com/users/" + sys.argv[1] + "/todos"
name_url = "https://jsonplaceholder.typicode.com/users?id=" + sys.argv[1]
json_res = json.loads(requests.get(todos_url).text)
user_name = json.loads(requests.get(name_url).text)[0]["name"]
res_len = len(json_res)
tasks_done = "\n\t"
j = 0

for i in range(res_len):
    if json_res[i]["completed"] == True:
        j += 1
        tasks_done += json_res[i]["title"] + "\n" + "\t"

tasks_done = tasks_done[:len(tasks_done)-2]
print("Employee {} is done with tasks({}/{}):{}"
      .format(user_name, j, res_len, tasks_done))
