import  requests

endpoint = "https://httpbin.org/anything"

get_response = requests.get(endpoint,json={"query":"Hello Wold"})
print(get_response.json())