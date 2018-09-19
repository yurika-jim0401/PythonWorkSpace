import json
# 此时的student是一个dict格式内容,不是json
student = {
    "name": "jim",
    "age": 23,
    "mobile": "18018598984"
}

print(type(student))

# 将python格式转换成json格式
stu_json = json.dumps(student)
print(type(stu_json))
print("JSON对象:{0}".format(stu_json))

# 将json格式读成python格式
stu_dict = json.loads(stu_json)
print(type(stu_dict))
print(stu_dict)
