from plyer import notification
import time

while True:
    print("Plese drink some water")
    notification.notify(title= "Please drink some water",message= "Its been an hour since you drank water")
    time.sleep(60*60)
