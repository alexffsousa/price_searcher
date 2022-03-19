from tkinter import *
my_w = Tk()
my_w.geometry("500x500")  # Size of the window 

def my_upd():
    print('Radiobutton  value :',r1_v.get())

r1_v = IntVar() # We used integer variable here 

r1 = Radiobutton(my_w, text='Passed', variable=r1_v, value=1,command=my_upd)
r1.grid(row=1,column=1) 

r2 = Radiobutton(my_w, text='Failed', variable=r1_v, value=0,command=my_upd)
r2.grid(row=1,column=2) 

r3 = Radiobutton(my_w, text='Appearing', variable=r1_v, value=5,command=my_upd )
r3.grid(row=1,column=3) 



class website_func:
   def __init__(self, website, id_procura, id_cookies, id_produto, id_preço):
      self.nome = website
      self.procura = id_procura
      self.cookies = id_cookies
      self.produto = id_produto
      self.preco = id_preço


websites_array = []
websites_array.append( website_func('https://www.worten.pt/', 'search-input', 'w-button-primary', 'w-product__wrapper', 'w-product-price__main') )
websites_array.append( website_func('https://www.pcdiga.com/', 'search', 'btn-cookie', 'df-card__main', 'price') )

print(websites_array(1).nome)

for website in websites_array:
   print( website.nome, website.preco)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

my_w.mainloop()  # Keep the window open