
from tkinter import *
from tkinter import messagebox
import sqlite3
from tkinter import messagebox


window = Tk()
window.title("DATABASE FORM")
window.geometry("600x650")
window.configure(bg='black')

conn = sqlite3.connect('information.db')

cursor = conn.cursor()

#save fn ************

def save():

    conn = sqlite3.connect('information.db')

    cursor = conn.cursor()

    record_id = sel_id.get()
    
    cursor.execute(''' UPDATE infos SET
    first_name = :first,
    last_name = :last,
    address = :address,
    city = :city,
    state = :state,
    pincode = :pincode 
    
    WHERE oid = :oid''',
    {
        'first': f_name_updated.get(),
        'last': l_name_updated.get(),
        'address': address_updated.get(),
        'city': city_updated.get(),
        'state': state_updated.get(),
        'pincode': p_code_updated.get(),

        'oid':record_id


    })

    conn.commit()

    conn.close()
    
    updated.destroy()

#submit function ************

def submit():

    conn = sqlite3.connect('information.db')

    cursor = conn.cursor()

    cursor.execute('''INSERT INTO infos VALUES(:f_name, :l_name, :address, :city, :state, :p_code)''',
                 {
                    'f_name':f_name.get(),
                    'l_name':l_name.get(),
                    'address':address.get(),
                    'city':city.get(),
                    'state':state.get(),
                    'p_code':p_code.get(), 
                 })

    conn.commit()

    conn.close()

    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    p_code.delete(0, END)

# show button function *********

def show():

    conn = sqlite3.connect('information.db')

    cursor = conn.cursor()

    cursor.execute('''SELECT *,oid FROM infos''')
    records = cursor.fetchall()
    print(records)

    print_records =""
    for record in records:
        print_records += str((record[0]))+ " , " + str(record[1]) + " , " + str(record[2]) + " , " + str(record[3]) + " , " + str(record[4]) + " , " + str(record[5])+ "\n"
     
    #window for showing records------
    show_win = Toplevel()
    show_win.title("ALL RECORDS")
    show_win.geometry("1800x700")
    show_win.configure(bg='black')

    #label to print records-----
    s_label = Label(show_win, text = print_records, font=("courier", 15))
    s_label.configure(background='black')
    s_label.configure(foreground='white')
    s_label.place(x = 10, y = 20)
    
    show_win.mainloop()
    conn.commit()

    conn.close()
    
#update function ************

def update():

    if sel_id.get() == "":
        messagebox.showerror("INPUT ERROR", "ENTER AN ID TO UPDATE ")
    else:
       global updated
       updated = Tk()
       updated.title("UPDATE A RECORD")
       updated.configure(bg="black")
       updated.geometry("600x650")

       conn = sqlite3.connect('information.db')

       cursor = conn.cursor()


       record_id = sel_id.get()
       cursor.execute('''SELECT * FROM infos WHERE oid =''' + record_id)
       records = cursor.fetchall()

       global f_name_updated
       global l_name_updated
       global address_updated
       global city_updated
       global state_updated
       global p_code_updated

    
    #entry boxes in function ***************
    
       f_name_updated = Entry(updated, width = 30, font=("Courier", 15))
       f_name_updated.place(x = 200, y = 20)

       l_name_updated = Entry(updated, width = 30, font=("Courier", 15))
       l_name_updated.place(x = 200, y = 70)

       address_updated  = Entry(updated, width = 30, font=("Courier", 15))
       address_updated.place(x = 200, y = 120)

       city_updated  = Entry(updated, width = 30, font=("Courier", 15))
       city_updated.place(x = 200, y = 170)

       state_updated  = Entry(updated, width = 30, font=("Courier", 15))
       state_updated.place(x = 200, y = 220)

       p_code_updated  = Entry(updated, width = 30, font=("Courier", 15))
       p_code_updated.place(x = 200, y = 270)

    #labels in function ***************

       f_name_label = Label(updated, text = "FIRST NAME", font=("Courier", 15))
       f_name_label.configure(bg='black')
       f_name_label.configure(foreground='white')
       f_name_label.place(x = 10, y = 20)
       
       l_name_label = Label(updated, text = "LAST NAME", font=("Courier", 15))
       l_name_label.configure(bg='black')
       l_name_label.configure(foreground='white')
       l_name_label.place(x = 10, y = 70)

       address_label = Label(updated, text = "ADDRESS" , font=("Courier", 15))
       address_label.configure(bg='black')
       address_label.configure(foreground='white')
       address_label.place(x = 10, y = 120)

       city_label = Label(updated, text = "CITY", font=("Courier", 15))
       city_label.configure(bg='black')
       city_label.configure(foreground='white')
       city_label.place(x = 10, y = 170)

       state_label = Label(updated, text = "STATE", font=("Courier", 15))
       state_label.configure(bg='black')
       state_label.configure(foreground='white')
       state_label.place(x = 10, y = 220)

       p_code_label = Label(updated, text = "PIN CODE", font=("Courier", 15))
       p_code_label.configure(bg='black')
       p_code_label.configure(foreground='white')
       p_code_label.place(x = 10, y = 270)

       for record in records:
           f_name_updated.insert(0,record[0])
           l_name_updated.insert(0,record[1])
           address_updated.insert(0,record[2])
           city_updated.insert(0,record[3])
           state_updated.insert(0,record[4])
           p_code_updated.insert(0,record[5])

    save_btn=Button(updated , text = "SAVE DATA", command = save, width=30)
    save_btn.grid(columnspan = 3, padx = 20, pady=20, ipadx=30 )
    save_btn.place(x=225,y=400)
    
    updated.mainloop()
#function to delete **********

def delete():

    if sel_id.get() == "":
        messagebox.showerror("INPUT ERROR", "ENTER AN ID TO DELETE ")

    conn = sqlite3.connect('information.db')

    cursor = conn.cursor()
    
    cursor.execute('''DELETE FROM infos WHERE oid = ''' + sel_id.get())
    sel_id.delete(0, END)

    conn.commit()

    conn.close()


#entry boxes ***************

f_name = Entry(window, font=("Courier", 15),width = 30)
f_name.place(x = 200, y=20)

l_name = Entry(window, width = 30, font=("Courier", 15))
l_name.place(x = 200, y=70)

address = Entry(window, width = 30, font=("Courier", 15))
address.place(x = 200, y=120)

city = Entry(window, width = 30, font=("Courier", 15))
city.place(x = 200, y=170)

state = Entry(window, width = 30, font=("Courier", 15))
state.place(x = 200, y=220)

p_code = Entry(window, width = 30, font=("Courier", 15))
p_code.place(x = 200, y=270)

sel_id = Entry(window, width=30 , font=("Courier", 15))
sel_id.place(x = 200, y=320)

#labels ***************

f_name_label = Label(window, text = "FIRST NAME", font=("Courier", 15))
f_name_label.configure(bg='black')
f_name_label.configure(foreground='white')
f_name_label.place(x = 10, y = 20)

l_name_label = Label(window, text = "LAST NAME", font=("Courier", 15))
l_name_label.configure(bg='black')
l_name_label.configure(foreground='white')
l_name_label.place(x = 10, y = 70)

address_label = Label(window, text = "ADDRESS", font=("Courier", 15))
address_label.configure(bg='black')
address_label.configure(foreground='white')
address_label.place(x = 10, y = 120)

city_label = Label(window, text = "CITY", font=("Courier", 15))
city_label.configure(bg='black')
city_label.configure(foreground='white')
city_label.place(x = 10, y = 170)

state_label = Label(window, text = "STATE", font=("Courier", 15))
state_label.configure(bg='black')
state_label.configure(foreground='white')
state_label.place(x = 10, y = 220)

p_code_label = Label(window, text = "PIN CODE", font=("Courier", 15))
p_code_label.configure(bg='black')
p_code_label.configure(foreground='white')
p_code_label.place(x = 10, y = 270)

sel_label = Label(window, text = "SELECT ID", font=("Courier", 15))
sel_label.configure(bg='black')
sel_label.configure(foregroun='white')
sel_label.place(x = 10, y = 320)

#submit button **********

s_btn = Button(window, text = "SUBMIT", command = submit, width=30)
s_btn.grid(columnspan = 3, padx = 20, pady=20, ipadx=30)
s_btn.place(x=225,y=425)

#show data button ***********

show_btn=Button(window , text = "SHOW DATA", command=show, width=30)
show_btn.grid(columnspan = 3, padx = 20, pady=20, ipadx=30)
show_btn.place(x=225,y=475)

#delete button ***********

del_btn=Button(window , text = "DELETE DATA", command=delete, width=30)
del_btn.grid(columnspan = 3, padx = 20, pady=20, ipadx=30)
del_btn.place(x=225,y=525)

#update button ***********

up_btn=Button(window , text = "UPDATE DATA", command = update, width=30)
up_btn.grid(columnspan = 3, padx = 20, pady=20, ipadx=30)
up_btn.place(x=225,y=575)

conn.commit()

conn.close()

window.mainloop()