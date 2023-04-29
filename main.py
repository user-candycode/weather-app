import subprocess

# The path to your Bash script
script_path = "/home/candy/Desktop/weather app/main.sh"

# Execute the script and capture the output
output = subprocess.check_output(["bash", script_path])

# Print the output
print("Fetching data....")
print(output.decode())
print("Data Fetched!")


print("Loading json data")



# The URL you want to retrieve
# with open('/home/candy/Desktop/weather app/delhi pollution', 'rt') as l:
#     link=l.readline()

# print(link)

# url = link
# print("url is: ",url)
# # The curl command to execute
# curl_command = ["curl -i", url]
# print("curl_command is: ",curl_command)

# # Execute the command and capture the output
# output = subprocess.check_output(curl_command)

# # Print the output
# print(output.decode())
