from weather.api import get_weather

def test_api():
    data = get_weather("Paris")
    assert "city" in data
from weather.formatter import format_weather

def test_format():
    text = format_weather({"city": "A", "temp": 10, "status": "ok"})
    assert isinstance(text, str)
from weather.history import add_to_history, get_history

def test_history():
    add_to_history({"city": "X"})
    assert len(get_history()) > 0
