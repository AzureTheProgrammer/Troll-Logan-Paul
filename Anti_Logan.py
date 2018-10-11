import requests, random, threading, time

url = 'https://loganpaul.com/mail/mail.php'
url2 = 'https://loganpaul.com'

names = open('names.txt').read().splitlines()

message = input("What message would you like to give logan? >>> ")
amount = int(input("How many messages? >>> "))

def Send():  
 while True:
   name = random.choice(names)
   rand_email = name + "@yahoo.com"

   requests.post(url,data={
    'name': name,
    'email': rand_email,
    'message': message,
    'url': url2 
   })
   time.sleep(0.5)
   print(f"{name} has sent a message to Logan Paul: '{message}'")

for i in range(0, amount):
  t = threading.Thread(target=Send)
  time.sleep(0.5)
  t.start()
