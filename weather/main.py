from weather.api import get_weather
from weather.formatter import format_weather

if __name__ == "__main__":
    data = get_weather("Berlin")
    print(format_weather(data))
city = input("Enter city: ")
data = get_weather(city)
print(format_weather(data))
