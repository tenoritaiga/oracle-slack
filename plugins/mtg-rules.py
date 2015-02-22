"""!rule <rule number>: return the Comprehensive Rule corresponding to the searched rule number"""

from urllib import quote
import re

def rule(rulenumber):
  
  rules = open('comprules.txt')
  
  found = False
  
  for line in rules:
    if re.search(r'^'+rulenumber+'.*',line):
      found = True
      break
    
  if found:
    return line
  else:
    return "Can't find a rule by that number."
  
def on_message(msg, server):
  text = msg.get("text", "")
  match = re.findall(r"!rule (.*)", text)
  if not match: return
  
  rulenumber = match[0]
  return rule(rulenumber)