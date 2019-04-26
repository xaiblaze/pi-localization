import datetime 
import requests

class MyLogger:
  def __init__ (self, host='http://egorv1.herokuapp.com/api/logging/'):
    self.host = host

  def date(self):
    return datetime.date.today()

  def time(self):
    return datetime.datetime.now().time()

  def send(self, packet):
    json = {
            'packet'  : str(packet),
            'date'    : str(self.date()),
            'time'    : str(self.time()) 
    }
    res = requests.post(self.host, data=json)