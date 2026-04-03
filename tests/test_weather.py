from weather.api import get_weather

def test_api():
    data = get_weather("Paris")
    assert "city" in data
from weather.formatter import format_weather

def test_format():
    text = format_weather({"city": "A", "temp": 10, "status": "ok"})
    assert isinstance(text, str)
