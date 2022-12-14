from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import tkinter as tk
import tkinter
import ast
import sqlite3
import webbrowser

#########################################################################################
# DATABASE CREATION

conn = sqlite3.connect('dataVase.db')
c = conn.cursor()

''' RUN THIS CODE IF dataVase.db DOES NOT EXIST
c.execute("""CREATE TABLE history(
        first_name text,
        last_name text,
        address text,
        main_region text,
        region_number text,
        site_number text,
        species text,
        amount text
        )""")
'''

#########################################################################################
# MENU SCREEN (w/ LOGIN, REGISTER)

def login():
    verify_username = login_username.get()
    verify_password = login_password.get()
    
    credentials = "Credentials"
    
    file = open(credentials, 'r')
    d = file.read()
    r = ast.literal_eval(d)
    file.close()
    
    if verify_username in r.keys() and verify_password == r[verify_username]:
        main_menu()
    else:
        messagebox.showerror('Invalid','Invalid Username or Password')
    
def register_user():
    
    username_info = register_username.get()
    password_info = register_password.get()
    
    credentials = "Credentials"
    
    try:
        file = open(credentials, 'r+')
        d = file.read()
        r = ast.literal_eval(d)
        
        dict2 = {username_info:password_info}
        r.update(dict2)
        file.truncate(0)
        file.close()
        
        file = open(credentials, 'w')
        w = file.write(str(r))
        
        messagebox.showinfo('Add Record', 'Successfully registered! You may now close the register window and proceed to login.')
    except:
        file = open(credentials, 'w')
        info = str({'Username':'Password'})
        file.write(info)
        file.close()
    
def register():
    
    global register_screen
    global frame_register
    
    register_screen = Toplevel(mainsc) 
    register_screen.title("Register")
    register_screen.geometry("600x400")
    
    frame_register = Frame(register_screen, relief='sunken', bg="light gray")
    frame_register.pack(fill = BOTH, expand = TRUE, padx = 5, pady= 5)
    
    register_bg = tk.PhotoImage(file="bg.png")
    label_register_bg = tk.Label(frame_register, image = register_bg)
    label_register_bg.image = register_bg
    label_register_bg.pack(fill="both", expand=True)
    
    global register_username
    global register_password
    register_username = StringVar()
    register_password = StringVar()
    
    Label(frame_register, text="Email or Username").place(x=240,y=100)
    Entry(frame_register, width=20, textvariable = register_username).place(x=230,y=125)
    Label(frame_register, text="Password").place(x=265,y=155)
    Entry(frame_register, width=20, textvariable = register_password).place(x=230,y=180)
    Button(frame_register, text="Register", command=register_user).place(x=268,y=205)
    
    
def secret_button():
    webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    
def team_credits():
    creditsteam = Toplevel()
    creditsteam.title("The team who made it possible!")
    creditsteam.geometry("793x387")
    
    frame_creditsteam = Frame(creditsteam, relief='sunken', bg="light gray")
    frame_creditsteam.pack(fill = BOTH, expand = TRUE, padx = 5, pady= 5)
    
    creditsteam_bg = tk.PhotoImage(file="credits.png")
    label_creditsteam_bg = tk.Label(frame_creditsteam, image = creditsteam_bg)
    label_creditsteam_bg.image = creditsteam_bg
    label_creditsteam_bg.pack(fill="both", expand=True)
    
    Button(frame_creditsteam, text="Click me for a secret!", command=secret_button).place(x=328,y=250)

def main_screen():  
    global mainsc
    
    mainsc = Tk()
    mainsc.title("DataVase! Where we find vase for our mother nature!")
    mainsc.geometry("600x400")
    mainsc.eval('tk::PlaceWindow . Center')

    frame_mainsc = Frame(mainsc, relief='sunken', bg="light gray")
    frame_mainsc.pack(fill = BOTH, expand = TRUE, padx = 5, pady= 5)
    
    background_mainsc = PhotoImage(file="bg.png")
    bg_mainsc = Canvas(frame_mainsc, width=600, height=400)
    bg_mainsc.pack(fill = "both", expand=True)
    bg_mainsc.create_image(0,0, image=background_mainsc, anchor="nw")
    
    global login_username
    global login_password
    login_username = StringVar()
    login_password = StringVar()
    
    Label(bg_mainsc, text="Email or Username").place(x=240,y=100)
    Entry(bg_mainsc, width=20, textvariable = login_username).place(x=230,y=125)
    Label(bg_mainsc, text="Password").place(x=265,y=155)
    Entry(bg_mainsc, width=20, textvariable = login_password).place(x=230,y=180)
    Button(bg_mainsc, text="Login", command = login).place(x=274,y=205)

    Label(bg_mainsc, text="No account yet? Register now!").place(x=210,y=250)
    Button(bg_mainsc, text="Register", command=register).place(x=268,y=275)
    
    Button(bg_mainsc, text="Credits", command=team_credits).place(x=5,y=359)
    
    #TO SKIP MAIN MENU LOGIN, PUT COMMAND TO NEXT LINE >>  Button(bg_mainsc, text="SKIP SINCE INPROGRESS", command=main_menu()).place(x=270,y=300)   
    
    mainsc.mainloop() 
    
#########################################################################################
# MAIN MENU FUNCTIONS

###### CREATE 

def submit():
    global data_mainregions
    global data_regions
    global data_sites
    global data_treeplants
    global data_numbertreeplants
    
    data_fname = f_name.get()
    data_lname = l_name.get()
    data_address = address.get()
    
    data_mainregions = mainregionsclicked.get()
    data_regions = regionsclicked.get()
    data_sites = sitesclicked.get()
    data_treeplants = treeplantsclicked.get()
    data_numbertreeplants = numbertreeplantsclicked.get()
    
    ''' FOR TESTING IF VARIABLES ARE BEING REFERENCED
    print(data_fname)
    print(data_lname)
    print(data_address)
    print(data_mainregions)
    print(data_regions)
    print(data_sites)
    print(data_treeplants)
    print(data_numbertreeplants)
    '''

    conn = sqlite3.connect("dataVase.db")
    c = conn.cursor()
    
    c.execute("INSERT INTO history VALUES (:first_name, :last_name, :address, :main_region, :region_number, :site_number, :species, :amount)",
    {
                'first_name': data_fname,
                'last_name': data_lname,
                'address': data_address,
                'main_region': data_mainregions,
                'region_number': data_regions,
                'site_number': data_sites,
                'species': data_treeplants,
                'amount': data_numbertreeplants
    })
    
    conn.commit()
    conn.close()
    
    messagebox.showinfo('Add Record', 'Successfully added record! You may now close the window.')
    
def addProject():
    
# INITIALIZATION OF GLOBAL VARIABLES
    global f_name
    global l_name
    global address
    global mainregionsclicked
    global regionsclicked
    global sitesclicked
    global treeplantsclicked
    global numbertreeplantsclicked
    
    addProjectsc = Toplevel()
    addProjectsc.geometry("600x400")
    
    frame_addProjectsc = Frame(addProjectsc, relief='sunken', bg="light gray")
    frame_addProjectsc.pack(fill = BOTH, expand = TRUE, padx = 5, pady= 5)
    
    addProjectsc_bg = tk.PhotoImage(file="bg.png")
    label_addProjectsc_bg = tk.Label(frame_addProjectsc, image = addProjectsc_bg)
    label_addProjectsc_bg.image = addProjectsc_bg
    label_addProjectsc_bg.pack(fill="both", expand=True)
    label_addProjectsc_bg.pack_propagate(False)

# PERSONAL DETAILS
    Label(frame_addProjectsc, text="Input personal details:").place(x=232,y=20)

    f_name = Entry(frame_addProjectsc, width=30, justify='center')
    f_name.place(x=200,y=50)
    f_name.insert(0,"First Name")
    
    l_name = Entry(frame_addProjectsc, width=30, justify='center')
    l_name.place(x=200,y=75)
    l_name.insert(0,"Last Name")
    
    address = Entry(frame_addProjectsc, width=30, justify='center')
    address.place(x=200,y=100)
    address.insert(0,"Address")

# LOCATION DETAILS
    Label(frame_addProjectsc, text="Input location of project:").place(x=226,y=140)
    
    Label(frame_addProjectsc, text="Main Region").place(x=162,y=170)
    mainregions = ["Luzon", "Visayas", "Mindanao"]
    mainregionsclicked = StringVar()
    mainregionsclicked.set(mainregions[0])
    drop_mainregions = OptionMenu(frame_addProjectsc, mainregionsclicked, *mainregions).place(x=160,y=195)
    
    Label(frame_addProjectsc, text="Region #").place(x=269,y=170)
    regions = ["REGION I", "REGION II", "REGION III", "REGION IV", "REGION V", 
               "REGION VI", "REGION VII", "REGION VIII", "REGION IX", "REGION X", 
               "REGION XI", "REGION XII",]
    regionsclicked = StringVar()
    regionsclicked.set(regions[0])
    drop_regions = OptionMenu(frame_addProjectsc, regionsclicked, *regions).place(x=247, y=195)
    
    Label(frame_addProjectsc, text="Site #").place(x=372,y=170)
    sites = ["#1", "#2", "#3", "#4", "#5"]
    sitesclicked = StringVar()
    sitesclicked.set(sites[0])
    drop_sites = OptionMenu(frame_addProjectsc, sitesclicked, *sites).place(x=360,y=195)

# PLANT DETAILS
    Label(frame_addProjectsc, text="Plant Details:").place(x=256,y=240)
    
    Label(frame_addProjectsc, text="Species").place(x=235, y=270)
    treeplants = ["Gmelina", "Mahogany", "Narra", "Molave", "Yakal", "Toog", "Apitong", "Variety"]
    treeplantsclicked = StringVar()
    treeplantsclicked.set(treeplants[0])
    drop_treeplants = OptionMenu(frame_addProjectsc, treeplantsclicked, *treeplants).place(x=210, y=295)
    
    Label(frame_addProjectsc, text="Amount").place(x=320, y=270)
    numbertreeplants = [1, 5, 10, 15, 20, 25, 30, 35]
    numbertreeplantsclicked = StringVar()
    numbertreeplantsclicked.set(numbertreeplants[0])
    drop_numbertreeplants = OptionMenu(frame_addProjectsc, numbertreeplantsclicked, *numbertreeplants).place(x=320, y=295)

    Button(frame_addProjectsc, text="Submit Form", command=submit).place(x=253, y=340)


###### READ

def query():
    conn = sqlite3.connect('dataVase.db')
    c = conn.cursor()
    
    c.execute("SELECT *, oid FROM  history")
    
    records = c.fetchall()
    print_records = ''
    for record in records:
        print_records += str(record) + "\n"
    
    query_label = Label(frame_mainmenusc, text=print_records)
    query_label.place(x=310,y=120) 
    
    conn.commit()
    conn.close()

###### UPDATE

def save():
    
    updatedata_fname = update_f_name.get()
    updatedata_lname = update_l_name.get()
    updatedata_address = update_address.get()
    updatedata_mainregionsclicked = update_mainregionsclicked.get()
    updatedata_regionsclicked = update_regionsclicked.get()
    updatedata_sitesclicked = update_sitesclicked.get()
    updatedata_treeplantsclicked = update_treeplantsclicked.get()
    updatedata_numbertreeplantsclicked = update_numbertreeplantsclicked.get()
    
    conn = sqlite3.connect('dataVase.db')
    c = conn.cursor()
    
    c.execute("""UPDATE history SET
              first_name = :first,
              last_name = :last,
              address = :address,
              main_region = :main_region,
              region_number = :region_number,
              site_number = :site_number,
              species = :species,
              amount = :amount
              
              WHERE oid = :oid""",
              {
                  'first': updatedata_fname,
                  'last': updatedata_lname, 
                  'address': updatedata_address,
                  'main_region': updatedata_mainregionsclicked,
                  'region_number': updatedata_regionsclicked,
                  'site_number': updatedata_sitesclicked,
                  'species': updatedata_treeplantsclicked,
                  'amount': updatedata_numbertreeplantsclicked,
                  
                  'oid': record_id
                  })
    
    conn.commit()
    conn.close()
    
    messagebox.showinfo('Update Record', 'Successfully updated record! You may now close the window.')
    
def update():
    
    global updatesc
    
    updatesc = Toplevel()
    updatesc.geometry("600x400")
    
    frame_updatesc = Frame(updatesc, relief='sunken', bg="light gray")
    frame_updatesc.pack(fill = BOTH, expand = TRUE, padx = 5, pady= 5)
    
    updatesc_bg = tk.PhotoImage(file="bg.png")
    label_updatesc_bg = tk.Label(frame_updatesc, image = updatesc_bg)
    label_updatesc_bg.image = updatesc_bg
    label_updatesc_bg.pack(fill="both", expand=True)
    label_updatesc_bg.pack_propagate(False)

# INSERTING DETAILS FROM DATABASE
    conn = sqlite3.connect('dataVase.db')
    c = conn.cursor()
    
# INITIALIZATION OF GLOBAL VARIABLES
    global update_f_name
    global update_l_name
    global update_address
    global update_mainregionsclicked
    global update_regionsclicked
    global update_sitesclicked
    global update_treeplantsclicked
    global update_numbertreeplantsclicked
    
# USER DETAILS
    Label(frame_updatesc, text="Update personal details:").place(x=227,y=20)

    update_f_name = Entry(frame_updatesc, width=30, justify='center')
    update_f_name.place(x=200,y=50)
    
    update_l_name = Entry(frame_updatesc, width=30, justify='center')
    update_l_name.place(x=200,y=75)
    
    update_address = Entry(frame_updatesc, width=30, justify='center')
    update_address.place(x=200,y=100)
    
# LOCATION DETAILS    
    Label(frame_updatesc, text="Update location of project:").place(x=220,y=140)
    
    Label(frame_updatesc, text="Main Region").place(x=162,y=170)
    update_mainregions = ["Luzon", "Visayas", "Mindanao"]
    update_mainregionsclicked = StringVar()
    update_drop_mainregions = OptionMenu(frame_updatesc, update_mainregionsclicked, *update_mainregions).place(x=160,y=195)
    
    Label(frame_updatesc, text="Region #").place(x=269,y=170)
    update_regions = ["REGION I", "REGION II", "REGION III", "REGION IV", "REGION V", 
               "REGION VI", "REGION VII", "REGION VIII", "REGION IX", "REGION X", 
               "REGION XI", "REGION XII",]
    update_regionsclicked = StringVar()
    update_drop_regions = OptionMenu(frame_updatesc, update_regionsclicked, *update_regions).place(x=247, y=195)
    
    Label(frame_updatesc, text="Site #").place(x=372,y=170)
    update_sites = ["#1", "#2", "#3", "#4", "#5"]
    update_sitesclicked = StringVar()
    update_drop_sites = OptionMenu(frame_updatesc, update_sitesclicked, *update_sites).place(x=360,y=195)

# PLANT DETAILS
    Label(frame_updatesc, text="Plant Details:").place(x=256,y=240)
    
    Label(frame_updatesc, text="Species").place(x=235, y=270)
    update_treeplants = ["Gmelina", "Mahogany", "Narra", "Molave", "Yakal", "Toog", "Apitong", "Variety"]
    update_treeplantsclicked = StringVar()
    update_drop_treeplants = OptionMenu(frame_updatesc, update_treeplantsclicked, *update_treeplants).place(x=210, y=295)
    
    Label(frame_updatesc, text="Amount").place(x=320, y=270)
    update_numbertreeplants = [1, 5, 10, 15, 20, 25, 30, 35]
    update_numbertreeplantsclicked = StringVar()
    update_drop_numbertreeplants = OptionMenu(frame_updatesc, update_numbertreeplantsclicked, *update_numbertreeplants).place(x=320, y=295)

    Button(frame_updatesc, text="Submit Form", command=save).place(x=253, y=340)
    
# INSERTING DETAILS

    global record_id
    
    record_id = update_box.get()
    c.execute("SELECT * FROM history WHERE oid = " + record_id)
    records = c.fetchall()
    
    for record in records:
        update_f_name.insert(0, record[0])
        update_l_name.insert(0, record[1])
        update_address.insert(0, record[2])
        update_mainregionsclicked.set(record[3])
        update_regionsclicked.set(record[4])
        update_sitesclicked.set(record[5])
        update_treeplantsclicked.set(record[6])
        update_numbertreeplantsclicked.set(record[7])
        
    conn.commit()
    conn.close()



###### DELETE

def delete():
    conn = sqlite3.connect('dataVase.db')
    c = conn.cursor()
    
    delete_id = delete_box.get()
    c.execute("DELETE FROM history WHERE oid="+ delete_id)
    
    conn.commit()
    conn.close()

    messagebox.showinfo('Delete Record', 'Successfully deleted record!')

#########################################################################################
# MAIN MENU

def main_menu():
    
    global label_mainmenu_bg
    global frame_mainmenusc
    global update_box
    global delete_box
    
    mainmenusc = Toplevel()
    mainmenusc.geometry("800x600")    
    
    frame_mainmenusc = Frame(mainmenusc, relief='sunken', bg="light gray")
    frame_mainmenusc.pack(fill = BOTH, expand = TRUE, padx = 5, pady= 5)
    frame_mainmenusc.pack_propagate(False)
    
    mainmenu_bg = tk.PhotoImage(file="bg1.png")
    label_mainmenu_bg = tk.Label(frame_mainmenusc, image = mainmenu_bg)
    label_mainmenu_bg.image = mainmenu_bg
    label_mainmenu_bg.pack(fill="both", expand=True)
    label_mainmenu_bg.pack_propagate(False)
    
    Label(frame_mainmenusc, text="Add Project").place(x=95,y=360)
    Button(frame_mainmenusc, text="ADD", command=addProject).place(x=112,y=385)
    
    Label(frame_mainmenusc, text="Update Project").place(x=88,y=420)
    Button(frame_mainmenusc, text="UPDATE", command=update).place(x=130,y=445)
    update_box = Entry(frame_mainmenusc, width=5, justify='center')
    update_box.place(x=80,y=449)
    update_box.insert(0, 'OID')
    
    Label(frame_mainmenusc, text="Delete Project").place(x=91,y=480) 
    Button(frame_mainmenusc, text="DELETE", command=delete).place(x=130,y=505)
    delete_box = Entry(frame_mainmenusc, width=5, justify='center')
    delete_box.place(x=80,y=509)
    delete_box.insert(0, 'OID')
    
    Label(frame_mainmenusc, text="Records:").place(x=490,y=50)
    Label(frame_mainmenusc, text="First Name : Last Name : Address : Main Region : Region # : Site # : Species : Amount : OID").place(x=276,y=80)
    Button(frame_mainmenusc, text="Refresh List", command=query).place(x=480,y=520)


#########################################################################################
# CLOSING DATABASE

conn.commit()
conn.close()

#########################################################################################

# DRIVER CODE

main_screen()
