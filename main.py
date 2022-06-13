from tkinter import *



import requests
from lxml import etree
from xml.etree import ElementTree




# setup
window = Tk()  # instance of a window
window.geometry("400x400")
window.title("F1 Requests")
window.config(background="grey")


yearLabel = Label(window, text="Enter a year"
                  , fg='green'
                  , bg='black'
                  , relief=RAISED,
                  bd=10
                  , padx=10
                  , pady=10
                  )

roundLabel = Label(window, text="Enter a round"
                  , fg='green'
                  , bg='black'
                  , relief=RAISED,
                  bd=10
                  , padx=10
                  , pady=10
                  )

def submit():

    #if yearBox.get == range(1970, 2022) and roundBox.get == range(0, 11):  # work on this
        year = str(yearBox.get())
        round = str(roundBox.get())


        print("Your details were correct good job")


        r = requests.get("http://ergast.com/api/f1/"+year+"/"+round)
        # r = requests.get("http://ergast.com/api/f1/2021/1") # test
        f = open('data.xml', 'a')


        f.truncate(0)
        f.write(r.text)




def deleteAll():
    yearBox.delete(0,END)
    roundBox.delete(0,END)


yearBox = Entry(window, font='italics'
                , fg='green'
                , bg='black'
                , relief=RAISED
                , bd=10
                )

roundBox = Entry(window, font='italics'
                , fg='green'
                , bg='black'
                , relief=RAISED
                , bd=10
                )

yearBox.insert(0, '') # default text


submitButton = Button(window, text="Enter",
                      command=submit,
                      fg='green',
                      bg='black',
                      relief=RAISED,
                      activebackground='black',
                      activeforeground='green',
                      bd=10)


deleteButton = Button(window, text="Delete TextFields",
                      command=deleteAll,
                      fg='green',
                      bg='black',
                      activebackground='black',
                      activeforeground='green',
                      relief=RAISED,
                      bd=10
                      )




yearLabel.pack()
yearBox.pack()
roundLabel.pack()
roundBox.pack()
submitButton.place(x=100, y=200)
deleteButton.place(x=190, y=200)


#####################
# year = input("What year?: ")
# round = input("What round?: ")
#r = requests.get("http://ergast.com/api/f1/"+year+"/"+round)
# f = open('data.xml', 'a')
#
# f.truncate(0)
# f.write(r.text)
#
# x = etree.parse('data.xml')
# print(etree.tostring(x, pretty_print=True))
#########################


window.mainloop()  #makes the window and listen for events

if __name__ == '__main__':
    print()
