from cProfile import label
from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time

def search():
    item = '' + item_to_search.get()
    lbl1 = Label(root, text=item)

    driver = webdriver.Firefox()
    url = 'https://www.pcdiga.com/'
    driver.get(url)
    driver.implicitly_wait(5)
    time.sleep(2)    
    try:
        elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'search')))
        elem.send_keys(item)
        elem.send_keys(Keys.RETURN)
        elem  = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'btn-cookie')))
        elem.click()
        elem  = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'df-card__main')))
        elem.click()
        elem  = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'price')))
        print(elem.text)
    except:
        print('wtf error')
    
root = Tk()
root.title('Let me check that price for u :)')
root.geometry('860x720')

lbl = Label(root, text = 'What should I look for?')
lbl.pack()
item_to_search = Entry(root, width=50, text='Write it here')
item_to_search.pack()

button1 = Button(root, text='Go search this', command=search)
button1.pack()


root.mainloop()