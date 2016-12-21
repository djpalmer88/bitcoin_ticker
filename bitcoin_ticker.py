import schedule
import time
import requests

def job():
    try:
        r = requests.get('http://api.coindesk.com/v1/bpi/currentprice/AUD.json')
        print("Price (AUD): %s" % r.json()['bpi']['AUD']['rate_float'])
    except requests.exceptions.ConnectionError:
        print("Connection Error, moving on...")

schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
