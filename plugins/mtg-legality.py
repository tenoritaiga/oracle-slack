"""!legality <card name>: return a card's play legality in all possible formats"""

from urllib import quote
import re
import requests
import helpers

def legality(cardname):
  
  legalformats = cardname + ": \n"
  cardname = quote(cardname)
  cardname = helpers.cardnametoslug(cardname)
  
  searchurl = "http://api.mtgdb.info/cards/"+cardname
  
  resp = requests.get(searchurl)
  
  if len(resp.text) < 3:
    return "Got no results for that search, sorry."
  else:
    resp_object = resp.json()
    
    for formats in resp_object[0]['formats']:
      legalformats += formats['name'] + ": " + formats['legality'] + "\n"
    return legalformats
  
def on_message(msg, server):
  text = msg.get("text", "")
  match = re.findall(r"!legality (.*)", text)
  if not match: return
  
  searchterm = match[0]
  
  if searchterm.lower() == "little girl":
    return "Hric confirmed for pedophile."
  else:
    return legality(searchterm)