# import requests

# # Weather function using OpenWeatherMap free API
# def get_weather(city):
#     API_KEY = ""  # Replace with your free API key
#     url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
#     try:
#         res = requests.get(url).json()
#         if res.get("cod") == 200:
#             temp = res["main"]["temp"]
#             desc = res["weather"][0]["description"]
#             return f"Weather in {city}: {temp}°C, {desc}"
#         else:
#             return f"Could not fetch weather for {city}. Error: {res.get('message', 'Unknown')}"
#     except Exception as e:
#         return f"Error fetching weather: {e}"


# # Joke function using Official Joke API
# def get_joke():
#     try:
#         url = "https://official-joke-api.appspot.com/random_joke"
#         res = requests.get(url).json()
#         return res.get("setup", "") + " " + res.get("punchline", "")
#     except Exception as e:
#         return f"Error fetching joke: {e}"


# # News function using Currents API (requires API key)
# def get_news():
#     API_KEY = ""  # Replace with your free API key from currentsapi.services
#     url = f"https://api.currentsapi.services/v1/latest-news?apiKey={API_KEY}"
#     try:
#         res = requests.get(url).json()
#         news_list = res.get("news", [])
#         if news_list:
#             return news_list[0]["title"]
#         return "No news available right now."
#     except Exception as e:
#         return f"Error fetching news: {e}"


# tools.py
import requests
from twilio.rest import Client

# --- WEATHER ---
def get_weather(city):
    API_KEY = "d8fc10f4c8a70a6ca31d1672cb300b82"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        res = requests.get(url).json()
        if res.get("cod") == 200:
            temp = res["main"]["temp"]
            desc = res["weather"][0]["description"]
            return f"Weather in {city}: {temp}°C, {desc}"
        else:
            return f"Could not fetch weather for {city}. Error: {res.get('message', 'Unknown')}"
    except Exception as e:
        return f"Error fetching weather: {e}"

# --- JOKE ---
def get_joke():
    try:
        url = "https://official-joke-api.appspot.com/random_joke"
        res = requests.get(url).json()
        return res.get("setup", "") + " " + res.get("punchline", "")
    except Exception as e:
        return f"Error fetching joke: {e}"

# --- NEWS ---
def get_news():
    API_KEY = "4WPZq8BF5Sr9ngzMdp3zrKuO43M9d6sO-Iebim_zpFDIqr_b"
    url = f"https://api.currentsapi.services/v1/latest-news?apiKey={API_KEY}"
    try:
        res = requests.get(url).json()
        news_list = res.get("news", [])
        if news_list:
            return news_list[0]["title"]
        return "No news available right now."
    except Exception as e:
        return f"Error fetching news: {e}"

# --- WHATSAPP ---
def send_whatsapp(to_number, message):
    account_sid = "YOUR_TWILIO_SID"
    auth_token = "YOUR_TWILIO_AUTH_TOKEN"
    from_whatsapp = "whatsapp:+14155238886"  # Twilio sandbox
    client = Client(account_sid, auth_token)
    msg = client.messages.create(
        body=message,
        from_=from_whatsapp,
        to=f"whatsapp:{to_number}"
    )
    # Log the message to data.txt
    with open("data.txt", "a") as f:
        f.write(f"To: {to_number}\n{message}\n---\n")
    return msg.sid