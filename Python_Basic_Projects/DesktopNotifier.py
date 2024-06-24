#Desktop notifier using python
from plyer import notification
import time
if __name__ =="__main__":
    while True:
        notification.notify(
            title="***Take Rest***",
            message="Rest is vital for better mental health.",
            #app_icon="",
            timeout=5)
        time.sleep(3600)


#pythonw DesktopNotier