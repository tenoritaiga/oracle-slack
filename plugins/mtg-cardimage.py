"""!mtg <card name>: return the image for the specified card from MTGImage"""

from urllib import quote
import re
import requests

def mtg(cardname):
  cardname = quote(cardname)
  
  searchurl = "http://mtgimage.com/card/"+cardname+".jpg"
  searchurl = searchurl.replace(" ", "_")
  
  resp = requests.get(searchurl);
  
  if resp.status_code == 200:
    return searchurl
  else:
    return "Got no results for that search, sorry."
  
def on_message(msg, server):
  text = msg.get("text", "")
  match = re.findall(r"!mtg (.*)", text)
  if not match: return
  
  searchterm = match[0]
  return mtg(searchterm)