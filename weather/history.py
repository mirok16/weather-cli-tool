# weather/history.py
history = []
def add_to_history(record):
    history.append(record)
def get_history():
    return history
from weather.api import get_weather
from weather.history import add_to_history

def fetch(city):
    data = get_weather(city)
    add_to_history(data)
    return data
