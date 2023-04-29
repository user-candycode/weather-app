import subprocess
import json
# The path to your Bash script
script_path = "/home/candy/Desktop/weather app/main.sh"

# Execute the script and capture the output
output = subprocess.check_output(["bash", script_path])

# Print the output
print("Fetching data....")
#print(output.decode())
print("Data Fetched!")


print("Loading json data")

# Open the JSON file and read its contents
with open('/home/candy/Desktop/weather app/data.json', 'r') as file:
    json_data = file.read()

# Parse the JSON data into a Python object
data = json.loads(json_data)

# Access the data as a Python variable
name_of_city=data['data']["city"]["name"]
aqi_of_city=data['data']["aqi"]
weather_min=data['data']['forecast']['daily']['o3'][0]['min']
weather_max=data['data']['forecast']['daily']['o3'][0]['max']
date=data['data']['forecast']['daily']['o3'][0]['day']


#color PAllet
black   = "\033[0;30m"
green   = "\033[0;32m"
maroon  = "\033[31m"
orange  = "\033[33m"
purple  = "\033[35m"
red     = "\033[0;31m"
yellow  = "\033[0;33m"
white   = "\033[0;37m"
nocolor = "\033[0m"



print("")
print("name of the city is: \t\t\t",name_of_city)
if aqi_of_city<=50:
    print("aqi of this city is: \t\t\t",f"{green}",aqi_of_city,"(Good)",f"{nocolor}")
elif aqi_of_city<=100:
    print("aqi of this city is: \t\t\t",f"{yellow}",aqi_of_city,"(Moderate)",f"{nocolor}")
elif aqi_of_city<=150:
    print("aqi of this city is: \t\t\t",f"{orange}",aqi_of_city,"(Unhealthy for Sensitive Groups)",f"{nocolor}")
elif aqi_of_city<=200:
    print("aqi of this city is: \t\t\t",f"{red}",aqi_of_city,"(Unhealthy)",f"{nocolor}")
elif aqi_of_city<=300:
    print("aqi of this city is: \t\t\t",f"{purple}",aqi_of_city,"(Very Unhealthy)",f"{nocolor}")
elif aqi_of_city>301:
    print("aqi of this city is: \t\t\t",f"{maroon}",aqi_of_city,"(Hazardous)",f"{nocolor}")
else:
    print("Something went worng")

print("min and max weather of this city is: \t", f"MIN:{weather_min}\u2103  MAX:{weather_max}\u2103")
