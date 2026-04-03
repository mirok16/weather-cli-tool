# weather/formatter.py
def format_weather(data):
    return f"{data['city']}: {data['temp']}°C, {data['status']}"
def format_weather(data):
    return f"Weather in {data['city']}: {data['temp']}°C ({data['status']})"
