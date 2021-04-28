from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import ui
import time
import random
import threading
import os
import requests
import mouse
import pyautogui


def baglantiResetle():
    os.system("nmcli networking off")
    time.sleep(10)
    os.system("nmcli networking on")
    time.sleep(10)

aranacakListe = []

while(True):
    
    path = "/home/memoli/.mozilla/firefox/qs7j27h7.default-release"
    firefoxProfile = webdriver.FirefoxProfile(path)
    firefoxProfile.set_preference("browser.privatebrowsing.autostart",True)
    firefoxProfile.set_preference("extensions.lastAppBuildId", "<apppID> -1 ")    
    driver = webdriver.Firefox(firefox_profile=firefoxProfile,)

    driver.get("https://www.google.com.tr/")
    aramaCubugu = driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[2]/div[1]/div[1]/div/div[2]/input")
    aramaCubugu.send_keys(aranacakListe[random.randint(0,len(aranacakListe)-1)])
    aramaCubugu.send_keys(Keys.ENTER)
    time.sleep(5)
    #1136,13  1100,103  
    pyautogui.moveTo(1310,82)
    pyautogui.click()
    time.sleep(5)
    pyautogui.moveTo(1134,251)
    pyautogui.click()
    

    time.sleep(8)
    
    reklamLinkleri = driver.find_elements_by_partial_link_text("Reklam")
    
    for i in reklamLinkleri:
        i.send_keys(Keys.CONTROL + Keys.RETURN)
    
    for i in reklamLinkleri:
        time.sleep(5)
        i.send_keys(Keys.CONTROL + "w")
    
    pyautogui.moveTo(1310,82)
    pyautogui.click()
    time.sleep()
    pyautogui.moveTo(1134,251)
    pyautogui.click()

    time.sleep(8)
    baglantiResetle()
    driver.close()