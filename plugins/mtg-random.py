"""!random: return a random card image from MTGImage"""

from urllib import quote
import re
import requests
import json

def random():

  randomurl = "http://api.mtgdb.info/cards/random"
  
  random_cardname_resp = requests.get(randomurl)
  
  if random_cardname_resp.status_code == 200:
    data = random_cardname_resp.json()
    
    searchurl = "http://mtgimage.com/card/"+data['name']+".jpg"
    searchurl = searchurl.replace(" ", "_")
    
    random_card_image_resp = requests.get(searchurl)
    if random_card_image_resp.status_code == 200:
      return searchurl
  else:
    return "Can't seem to get a random card. Try again?"
  
def on_message(msg, server):
  text = msg.get("text", "")
  match = re.findall(r"!random", text)
  if not match: return
  
  return random()