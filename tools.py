from unittest import result
import requests

def exch():
    import datetime
    day = int(str(datetime.date.today()).replace("-", ""))
    r = requests.get(
        "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=USD&date=" + str(day) + "&json")
    r2 = requests.get(
        "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=USD&date=" + str(day - 1) + "&json")
    data = r.text.split(",")
    data2 = r2.text.split(",")
    delta = float(data[2][7:]) - float(data2[2][7:])
    result = " USD/UAH " + data[2][7:] + " Δ" + str(delta)
    return result

def weather():
    try:
        import tokenbot
        res = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Kiev,ua&units=metric", params={'APPID': tokenbot.weather})
        data = res.json()
        result = "In Kiev now " + str( data['weather'][0]['main'] ) + ", temp is: "+ str( data['main']['temp'])
    except Exception as e:
        print("Exception (weather):", e)
        result = -1
        pass
    return result