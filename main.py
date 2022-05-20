import webscrape
import emailSender

# emailTo = ['oliver.s.maund@icloud.com', 'milesabbotthome@gmail.com', 'hughmcmenamin18@gmail.com']

emailTo = ['william.f.powell@outlook.com', "will63powell@gmail.com"]

if __name__=="__main__":
  web = webscrape.Webscrape('debug')
  email = emailSender.EmailSender()

  if not web.checkPage('https://www.passport.service.gov.uk/urgent/', 'sorry'):
    email.send(emailTo, 'PASSPORT RENEWAL', 'URGENT - PASSPORT RENEWAL IS NOW OPEN', ' If you have received this email it means https://www.passport.service.gov.uk/urgent/ is now accepting passport renewals. Cheers, Will')

  if not web.checkPage('https://www.passportappointment.service.gov.uk/outreach/publicbooking.ofml', 'sorry'):
    email.send(emailTo, 'PASSPORT RENEWAL', 'URGENT - PASSPORT RENEWAL IS NOW OPEN', ' If you have received this email it means https://www.passportappointment.service.gov.uk/outreach/publicbooking.ofml is now accepting passport renewals. Cheers, Will')
