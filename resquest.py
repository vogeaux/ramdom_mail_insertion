import requests
# import pandas as pd
x=1000

#payload = {"key":"Add_Google_API_Key_Here", "address":"Redhot Ranch"}
#response = requests.get(url="https://randomuser.me/api/?results="+str(x)+"&format=json&nat=fr", 
                        #params=payload,
                        #timeout=5) # optional: set a 5 second timeout for the http request


response_api_user = requests.get(url="https://randomuser.me/api/?results="+str(x)+"&format=json&nat=fr",timeout=5) # optional: set a 5 second timeout for the http request
#print(response.text)
#print(response.status_code)
data_api_user = response_api_user.json()

#https://api.motdepasse.xyz/create/?include_lowercase&include_digits&include_uppercase&password_length=4&quantity=1

for i in range (0,x):
    name_result_user = data_api_user['results'][i]['email']
    name_result_user=name_result_user.replace("@example.com", "@intra-tech.fr")
    name_result_password = data_api_user['results'][i]['login']['password']
    print(name_result_user)
    print(name_result_password)
