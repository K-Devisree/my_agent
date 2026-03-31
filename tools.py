import requests

def get_weather(city):
    url = f"https://wttr.in/{city}?format=3"
    return requests.get(url).text

def get_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    res = requests.get(url).json()
    return res["setup"] + " " + res["punchline"]

def get_news():
    url = "https://api.currentsapi.services/v1/latest-news?apiKey=demo"
    res = requests.get(url).json()
    news_list = res.get("news", [])
    if news_list:
        return news_list[0]["title"]
    return "No news available right now."