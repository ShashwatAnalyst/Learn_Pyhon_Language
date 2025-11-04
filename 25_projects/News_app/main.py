import requests
key = "Enter Your News API KEY for NewsAPI.org"
query = str(input("What do you want to know about? "))

url = f"https://newsapi.org/v2/everything?q={query}&from=2025-10-04&sortBy=publishedAt&apiKey={key}"

r = requests.get(url)

data = r.json()
articles = data["articles"]
for i,article in enumerate(articles):
    print(i + 1 ,article["title"])
    print(" ")
    print(article["url"])
    print("\n****************************************\n")
