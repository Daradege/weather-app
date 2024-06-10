import requests

def connected():
    try:
        res = requests.get('https://openweathermap.org')
    except:
        return 'Not Connected'
    if res.status_code == 200:
        return 'successful'
    return 'unsuccessful'  
