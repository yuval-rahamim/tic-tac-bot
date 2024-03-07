from selenium import webdriver
from selenium.webdriver.common.by import By
import random

num = 0

class MyButton:
    def __init__(self, button, st):
        self.button = button
        self.st = st

def checknum():
    global num
    num = 0
    for but_seq in buttonArr:
        for but in but_seq:
            if but.button.is_enabled()==False:
                but.st = but.button.text
                num += 1
    # print(num)

def place():
    global num
    isdisable = True
    while isdisable:
        ran1 = random.randint(0, 2)
        ran2 = random.randint(0, 2)
        if buttonArr[ran1][ran2].button.is_enabled():
            isdisable = False
    buttonArr[ran1][ran2].button.click()
    checknum()
    newnum = num
    while newnum== num:
        checknum()
    place()

browser = webdriver.Chrome()
browser.get("https://ix-igul.netlify.app/")
edit = browser.find_element(By.XPATH, "/html/body/div/main/div/ol[1]/li[2]/button")
edit.click()
name = input("what is your name ")
namein = browser.find_element(By.XPATH,"/html/body/div/main/div/ol[1]/li[2]/span/input")
namein.clear()
namein.send_keys(name)
edit.click()
buttonArr = [
[MyButton(browser.find_element(By.XPATH,"/html/body/div/main/div/ol[2]/li[1]/ol/li[1]/button"),""),MyButton(browser.find_element(By.XPATH,"/html/body/div/main/div/ol[2]/li[1]/ol/li[2]/button"),""),MyButton(browser.find_element(By.XPATH,"/html/body/div/main/div/ol[2]/li[1]/ol/li[3]/button"),"")],
[MyButton(browser.find_element(By.XPATH,"/html/body/div/main/div/ol[2]/li[2]/ol/li[1]/button"),""),MyButton(browser.find_element(By.XPATH,"/html/body/div/main/div/ol[2]/li[2]/ol/li[2]/button"),""),MyButton(browser.find_element(By.XPATH,"/html/body/div/main/div/ol[2]/li[2]/ol/li[3]/button"),"")],
[MyButton(browser.find_element(By.XPATH,"/html/body/div/main/div/ol[2]/li[3]/ol/li[1]/button"),""),MyButton(browser.find_element(By.XPATH,"/html/body/div/main/div/ol[2]/li[3]/ol/li[2]/button"),""),MyButton(browser.find_element(By.XPATH,"/html/body/div/main/div/ol[2]/li[3]/ol/li[3]/button"),"")]
]
place()