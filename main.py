import tinder_bot as tb
import time

login = input("Insert email/phone number connected with your FB account: ")
password = input("Insert password to your FB account: ")

print("Currenty bot works slowly, however, it can handle every pop up, you just have to wait. \nFirst actions are going to happen in 40 seconds due to location pop up. \nTinder sometimes also changes their site, so there are new buttons, if there are any problems conntact me\nPlease be patient :)")
bot = tb.tinder_bot()
bot.login(login, password)
time.sleep(5)
bot.close_location_pop()
bot.auto_like()

