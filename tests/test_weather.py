from weather.api import get_weather

def test_api():
    data = get_weather("Paris")
    assert "city" in data
