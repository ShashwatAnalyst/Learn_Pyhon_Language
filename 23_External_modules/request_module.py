import requests

r = requests.get("https://api.github.com/users/shashwatanalyst")

with open("my_git_info.txt","w") as f:
    f.write(r.text)

