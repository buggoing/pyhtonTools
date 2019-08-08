import smtplib

sender = 'user@test.com'
recipent = 'user@test.com'
password = '***'

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(sender, password)
server.sendmail(
  sender, 
  recipent, 
  "this message is from me")
server.quit()
