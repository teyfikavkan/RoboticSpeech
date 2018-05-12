# -*- coding: utf-8 -*-
import tkMessageBox
from Tkinter import *
import ttk
import BotConnection
from json import dumps
from firebase import firebase

firebase = firebase.FirebaseApplication('https://robotic-speech-questions.firebaseio.com/', None)
result = firebase.get('/UnansweredQuestions',None)

print list(result.keys())[0]   # firebasede ilk satırın key'ini veriyor
print list(result.values())[0] # firebasede ilk satırın değerini veriyor
print dumps(result.items()[0])      #firebasede ilk satırı veriyor
print len(result)   # kaç tane cevapsız soru olduğunu gösteriyor

root = Tk()


tree = ttk.Treeview(root)

tree["columns"]=("one","two")
tree.column("one", width=250 )
tree.column("two", width=400)
tree.heading("one", text="KEY")
tree.heading("two", text="SORU")

for i in range(len(result)):
            tree.insert("", 0, text="Soru "+str(i+1), values=(list(result.keys())[i], list(result.values())[i]))



def refresh():
    x = tree.get_children()
    for item in x: ## Changing all children from root item
        tree.delete(item)
    result = firebase.get('/UnansweredQuestions', None)
    for i in range(len(result)):
        tree.insert("", 0, text="Soru " + str(i + 1), values=(list(result.keys())[i], list(result.values())[i]))

def delete():
    selected_item = tree.selection()[0] ## get selected item
    curItem = tree.focus()
    print tree.item(curItem)
    print tree.item(curItem)['values'][2]
    tkMessageBox.showinfo("Information", str(tree.item(curItem)['text']) + " has been deleted!")
    firebase.delete('/UnansweredQuestions', tree.item(curItem)['values'][0])
    tree.delete(selected_item)

def addAnswer():
    global strEntryAnswer
    global strEntrySablon
    contentEntry = strEntryAnswer.get()
    contentSablon = strEntrySablon.get()

    curItem = tree.focus()


    print contentEntry

    query = ' {!RET cmdaddresponsewithpatterns '+tree.item(curItem)['values'][1]+','+contentSablon+','+ contentEntry+'!}-'
    print query

    print BotConnection.connectBot(query);


    #firebase.delete('/UnansweredQuestions', tree.item(curItem)['values'][0])
    #tree.delete(selected_item)

tree.pack()
button_del = Button(root, text="del", command=delete)
button_del.pack( padx=5, pady=5)
button_refresh = Button(root, text="refresh", command=refresh)
button_refresh.pack( padx=5, pady=5)

strEntrySablon = StringVar()
entry_sablon = Entry(width = 70,  textvariable=strEntrySablon)
strEntrySablon.set('.*')
entry_sablon.pack( padx=5, pady=5)

strEntryAnswer = StringVar()
entry_answer = Entry(width = 70, textvariable=strEntryAnswer)
entry_answer.pack( padx=5, pady=5)
strEntryAnswer.set('Buraya cevabı giriniz')

button_enter = Button(root, text="Add Answer", command=addAnswer)
button_enter.pack()




root.mainloop()