import xml.dom.minidom
import tkinter as tk
form =tk.Tk()
form.title('XML Parsing')
form.geometry('300x100')
form.config(bg='#25D366')

def readXML():
    doc=xml.dom.minidom.parse('sample.xml')
    print(doc.nodeName)
    print(doc.firstChild.tagName)
    books=doc.getElementsByTagName('book')
    print('Books', books.length)
    for x in books:
        print(x.getAttribute('category'))
        Label01=tk.Label(form,text=x.getAttribute('category'),
        bg='#25D366',fg='#075E54',font='Arial 20 bold').pack()
readXML()
tk.mainloop()

