import requests
import json
import jsonpath

# Post (Add) request url
url = "https://reqres.in/api/users"

# First make a json file with the input content

# Now read the input Json file
infile = open("C:\\Users\\petro\\Repos\\python\\APITesting\\test.json", "r")  #read the data
json_input = infile.read() #string format now
request_json = json.loads(json_input)  #makes it into json format

# Make the post request with json Input body and get the response
response = requests.post(url, request_json)

# validate the response code
assert response.status_code == 201

# fetch header from the response
#print(response.headers.get('Content-Length'))

# Parse the response to Json format (currently in string)
response_json = response.json()

# Pick Id using json path
id = response_json["id"]
print(id)
