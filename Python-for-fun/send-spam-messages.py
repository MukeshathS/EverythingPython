import random
import pyautogui as pg
import time

hi = ("Hiiiii", "Hi!", "Hiiiii!!!!",
      "Hi!!!!!!!!!", "hi!!!", "Hhhhiiiii!")
hru = ("HRU", "Howru", "How R U?", "How r u?",
       "How Are You?", "How are u?", "How are yu",
       "How Are you")
time.sleep(8)
for i in range(40):
    a = random.choice(hi)
    pg.write(a)
    b = random.choice(hru)
    pg.write(b)
    pg.press('enter')
