def cardnametoslug(cardname):
  
  cardname = cardname.lower()
  cardname = cardname.replace(" ", "-")
  cardname = cardname.replace(",", "")
  return cardname