import datetime 
import requests

class MyLogger:
    def __init__ (self, host='https://ece813.herokuapp.com/api/logging/'):
        self.host = host
        self.distance = -1  #initial value

    def date(self):
        return datetime.date.today()

    def time(self):
        return datetime.datetime.now().time()
  
    def set_distance(self, value):
        self.distance = value
    
    def get_distance(self):
        return self.distance

    def send(self, packet=None):
        json = {
            'packet'  : str(packet),
            'date'    : str(self.date()),
            'time'    : str(self.time()),
            'distance': self.get_distance()
        }
        res = requests.post(self.host, data=json)
