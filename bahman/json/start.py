import json

"""
JSON : Java Scripting Object Notation

json.load(f) => load json data file from file 

json.loads(f) => load json data from string

json.dump(object , f) => write json object to file

json.dumps(object) => output json object as string 
"""



string = """{\"name\": \"amir\", \"email\": \"<EMAIL>\", \"age\":30}"""

# convert x in dic
# loads : string to dict
string_to_json = json.loads(string)

print(string_to_json) # dict all
print(string_to_json['name']) # value name
print(type(string_to_json))


dictionary = {
    "name" : "amir",
    "email" : "<EMAIL>",
    "address":"123 Main St",
    "age":23,
    "F":False,
    "Null": None
}

# convert x in string
# dict to string
dict_to_json = json.dumps(dictionary)

print(dict_to_json)
print(type(dict_to_json)) # string

# -------------------------------------------
# dumps

# list
print(json.dumps([1,2,3]))
# None
print(json.dumps(None))
# False
print(json.dumps(False))
# True
print(json.dumps(True))

# -------------------------------------

# indent => \n
print(json.dumps([1,2,3,4], indent=4) )

# -----------------------------------------
# write, read to file

file = open("tx.text", "r", encoding="utf-8")
text = json.load(file)

print(text)
print(type(text))

print(text['entities']['user_mentions'])


json_file = open("js.json", "w", encoding="utf-8")
json.dump(text, json_file, ensure_ascii=False, indent=4)

file.close()
json_file.close()