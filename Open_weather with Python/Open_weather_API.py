import requests


print ("Enter Zip in US:")
zip = str(input()) # str conv
response = requests.get("https://api.openweathermap.org/data/2.5/forecast?zip="+zip+",us&appid= #Add API ID#")# add parameter to the url using str concatenate
data = response.json() # Json format
temp_dict = {}
#temp_dict = {"key":"value"}
print(" Date       Temp          Precipitation")
for record in data ['list']:
    max_temp = record['main']['temp_max']
    min_temp = record['main']['temp_min']
    precipitation = record['pop']
    date = str.split(record['dt_txt'], " ")
    date = date[0]
    if date in temp_dict:
        if temp_dict[date]["max"] < max_temp:
            temp_dict[date]["max"] = max_temp
        if temp_dict[date]["min"] > min_temp:
            temp_dict[date]["min"] = min_temp
    else:
        temp_dict.update({date:{"max":max_temp, "min":min_temp, "precipitation":precipitation}})

for keys in temp_dict:
    print(keys,temp_dict[keys]["max"],temp_dict[keys]["min"],temp_dict[keys]["precipitation"])
