from ast import If
from cProfile import label
from json import tool
from tkinter import *
from tkinter import ttk
from turtle import back
from click import command
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

def open_popup():
   top= Toplevel(root)
   top.geometry("750x250")
   top.title("Child Window")
   Label(top, text= "Hello World!", font=('Mistral 18 bold')).place(x=150,y=80)


def websites_search():
    x = radio_value.get()
    if x==1:
        print('I will search this websites')
    
root = Tk()
root.title('Let me check that price for u :)')
root.geometry('860x720')

lbl = Label(root, text = 'What should I look for?')
lbl.pack()
item_to_search = Entry(root, width=50, text='Write it here')
item_to_search.pack()

button1 = Button(root, text='Go search this', command=search)
button1.pack()

menubar = Menu(root, background='#9E9997')
file = Menu(root, tearoff=0)
file.add_command(label='Add new item', command=root.quit)
file.add_separator()
file.add_command(label='Exit program', command=root.quit)
menubar.add_cascade(label='File', menu=file)
#------------------------------------------------------------#
tools = Menu(root, tearoff=0)
tools.add_command(label='Edit item', command=root.quit)
tools.add_command(label='Remove item')
menubar.add_cascade(label='Tools', menu=tools)
#------------------------------------------------------------#
about = Menu(root, tearoff=0)
about.add_command(label='Version', command=open_popup)
about.add_command(label='The project')
about.add_command(label='The coders')
menubar.add_cascade(label='About', menu=about)

radio_value = IntVar()
r1 = Radiobutton(root, text='Worten', variable=radio_value, value=1,command=websites_search)
r1.pack()

websites = ['Worten', 'Fnac', 'PCDiga', 'Radio Popular', 'Media Markt']

for website in websites:
    websites_search()

root.config(menu=menubar)
root.mainloop()