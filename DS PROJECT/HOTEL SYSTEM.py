from tkinter import *
from tkinter import ttk
from tkinter import messagebox


# --------- M A I N     P A N E L ---------------
def Imp_Note():
    screen11=Toplevel()
    screen11.geometry('800x500+390+120')
    screen11.title("IMPORTANT NOTE")
    screen11.configure(bg="white")
    screen11.resizable(0, 0)
    photo = PhotoImage(file="IMPNOTE.png")
    label = Label(screen11, image=photo)
    label.pack()

    photo1 = PhotoImage(file="Imp.png")
    label1 = Label(screen11, image=photo1, bg="yellow")
    label1.place(x=325, y=70)

    photo5 = PhotoImage(file="back-arrow.png")
    pht3 = photo5.subsample(2,2)
    Button(screen11, bg="black", image=pht3, command=screen11.destroy).place(x=9, y=459)
    Label(text="").pack()

    photo15 = PhotoImage(file="forward-arrow.png")
    pht13 = photo15.subsample(14,18)
    Button(screen11, bg="black", image=pht13, command=reception_desk).place(x=748, y=458)
    Label(text="").pack()

    screen11.mainloop()










def reception_desk():
    screen1=Toplevel()

    screen1.geometry('800x500+390+120')
    screen1.title("RECEPTION DESK")
    screen1.configure(bg="white")
    screen1.resizable(0,0)
    photo = PhotoImage(file="d1b032bf-334d-438b-89dd-d74df04276fd.png")
    label = Label(screen1, image=photo)
    label.pack()
    photo1 = PhotoImage(file="Capture.png")
    label1 = Label(screen1,image=photo1,bg="yellow")
    label1.place(x=325,y=80)


    photo2 = PhotoImage(file="Capturep.PNG")
    pht = photo2.subsample(2,2)
    Button(screen1,bg="yellow" ,image=pht,command=admin).place(x=40, y=210)
    Label(text="").pack()

    photo3 = PhotoImage(file="CaptureSII.PNG")
    pht1 = photo3.subsample(2, 2)
    Button(screen1, bg="yellow", image=pht1,command=guest_login).place(x=240, y=210)
    Label(text="").pack()


    photo4 = PhotoImage(file="Capture2w324.PNG")
    pht2 = photo4.subsample(2, 2)
    Button(screen1, bg="yellow", image=pht2,command=signup_screen).place(x=440, y=210)
    Label(text="").pack()

    photo6 = PhotoImage(file="Capture124 (3).png")
    pht4 = photo6.subsample(2,2)
    Button(screen1, bg="yellow", image=pht4, command=contact_us).place(x=640, y=210)
    Label(text="").pack()

    photo5 = PhotoImage(file="back-arrow.png")
    pht3 = photo5.subsample(2,2)
    Button(screen1, bg="black", image=pht3,command=screen1.destroy).place(x=9, y=459)
    Label(text="").pack()


    screen1.mainloop()










#------------------ A D M I N    W O R K S  ---------------------

# --- ADMIN LOGIN FORM ---
def admin():

    global Adname
    global PASS
    screen4 = Toplevel()

    screen4.geometry('800x500+390+120')
    screen4.title("ADMIN")
    screen4.configure(bg='white')
    screen4.resizable(0, 0)

    photo1 = PhotoImage(file="admin games.png")
    label = Label(screen4,image=photo1)
    label.pack()

    photo2 = PhotoImage(file="tempsnipadm.png")
    label1 = Label(screen4, image=photo2, bg="yellow")
    label1.place(x=325, y=80)

    Adname = StringVar()
    txt_Adname = Entry(screen4, width=18, textvar=Adname, bg='white', font=('Bradley Hand ITC', 29, 'bold'))
    txt_Adname.place(x=355, y=210)
    PASS = StringVar()
    txt_PASS = Entry(screen4, width=18, textvar=PASS, bg='white', show="*",font=('Bradley Hand ITC',29, 'bold'))
    txt_PASS.place(x=355, y=351)
    photo6 = PhotoImage(file="tempsniplog.png")
    pht4 = photo6.subsample(1, 1)
    Button(screen4, bg="black", image=pht4, command=ad_id_pass).place(x=185, y=438)
    Label(text="").pack()

    photo3 = PhotoImage(file="back-arrow.png")
    pht6 = photo3.subsample(2,2)
    Button(screen4, bg="black", image=pht6, command=screen4.destroy).place(x=9, y=459)
    Label(text="").pack()

    screen4.mainloop()

def ad_id_pass():
    id = Adname.get()
    ps = PASS.get()

    if id ==  "OAZ" and ps == "123":
        print("ADMIN ACCESS......")
        print ("__________________")
        print()
        adminpanel_screen()

def adminpanel_screen():

            screen12 = Toplevel()

            screen12.geometry('800x500+390+120')
            screen12.title("ADMIN PANEL")
            screen12.configure(bg='white')
            screen12.resizable(0, 0)

            photo1 = PhotoImage(file="d1b032bf-334d-438b-89dd-d74df04276fd.png")
            label = Label(screen12, image=photo1)
            label.pack()

            photo2 = PhotoImage(file="tempsnipADP.png")
            label1 = Label(screen12, image=photo2, bg="yellow")
            label1.place(x=325, y=80)

            photo4 = PhotoImage(file="DETAILS MEM.png")
            pht8 = photo4.subsample(1, 1)
            Button(screen12, bg="black", image=pht8, command=member_details).place(x=140, y=170)
            Label(text="").pack()

            photo6 = PhotoImage(file="bOOKING.png")
            pht18 = photo6.subsample(1, 1)
            Button(screen12, bg="black", image=pht18, command=booking_details).place(x=140, y=250)
            Label(text="").pack()

            photo16 = PhotoImage(file="hwG.png")
            pht28 = photo16.subsample(1, 1)
            Button(screen12, bg="black", image=pht28, command=Searching_details).place(x=140, y=330)
            Label(text="").pack()



            photo3000 = PhotoImage(file="back-arrow.png")
            pht1012 = photo3000.subsample(2, 2)
            Button(screen12, bg="black", image=pht1012, command=screen12.destroy).place(x=9, y=459)
            Label(text="").pack()




            screen12.mainloop()




# --- GUEST NAMES DETAILS ---
def member_details():
    screen6 = Toplevel()
    screen6.geometry('800x500+390+120')
    screen6.configure(bg='white')
    screen6.resizable(0,0)

    photo1 = PhotoImage(file="d1b032bf-334d-438b-89dd-d74df04276fd.png")
    label = Label(screen6, image=photo1)
    label.pack()

    photo2 = PhotoImage(file="tempsnipmem.png")
    label1 = Label(screen6, image=photo2, bg="yellow")
    label1.place(x=325, y=80)

    global dltmem
    dltmem = StringVar()
    txt_dltmem = Entry(screen6, width=18, textvar=dltmem, bg='white', font=('Bradley Hand ITC', 16, 'bold'))
    txt_dltmem.place(x=200, y=165)




    photo9 = PhotoImage(file="tempsnipSHW.png")
    pht9 = photo9.subsample(1, 1)
    Button(screen6, bg="black", image=pht9, command=sort_p).place(x=617, y=200)
    Label(text="").pack()

    photo15 = PhotoImage(file="tempsnipdlt.png")
    pht15 = photo15.subsample(1, 1)
    Button(screen6, bg="black", image=pht15, command=deleteuser).place(x=617, y=300)
    Label(text="").pack()





    photo3 = PhotoImage(file="back-arrow.png")
    pht7 = photo3.subsample(2,2)
    Button(screen6, bg="black", image=pht7, command=screen6.destroy).place(x=9, y=459)
    Label(text="").pack()
    global list1
    list1 = Listbox(screen6, height=12, width=65, bg='white', font=('constantia', 12, 'bold'))
    list1.place(x=9, y=208)

    screen6.mainloop()

# --- LINKED LIST & INSERTION SORT ---
class node:
    def __init__(self, data):
        self.data = data
        self.link = None

class linklist:
    def __init__(self):
        self.head = None

    def insert(self,data):
        newNode=node(data)
        if self.head:
            current=self.head
            while current.link:
                current=current.link
            current.link=newNode
        else:
            self.head=newNode


    def print(self):
        node=self.head
        while node!=None:
            print(node.data,end="")
            node=node.link
        print("",end=" ")

def insertionSort(head):
        if head == None:
            return None
        # Make the first node the start of the sorted list.
        sortedList = head
        head = head.link
        sortedList.link = None
        while head != None:
            current = head
            head = head.link
            if current.data < sortedList.data:
                # Advance the nodes
                current.link = sortedList
                sortedList = current
            else:
                # Search list for correct position of current.
                search = sortedList
                while search.link != None and current.data > search.link.data:
                    search = search.link
                # current goes after search.
                current.link = search.link
                search.link = current
        return sortedList

def printList(head):
    node = head
    while node != None:
        list1.insert(END,node.data)
        node = node.link

def sort_p():
    list1.delete(0,END)
    ll = linklist()
    f = open('Registered Users', 'r')
    ff = f.readlines()
    for i in ff:
        ll.insert(i)

    result = insertionSort(ll.head)
    printList(result)


def deleteuser():
    sdlt = dltmem.get()
    with open("Registered Users", "r") as f:
        lines = f.readlines()
    with open("Registered Users", "w") as f:
        for line in lines:
            if line.split(',')[0] != sdlt:
                f.write(line)




# --- GUEST BOOKING DETAILS ---
def booking_details():
    screen7 = Toplevel()
    screen7.geometry('800x500+390+120')
    screen7.configure(bg='white')
    screen7.resizable(0,0)

    photo1 = PhotoImage(file="d1b032bf-334d-438b-89dd-d74df04276fd.png")
    label = Label(screen7, image=photo1)
    label.pack()

    photo2 = PhotoImage(file="tempsnipbkd.png")
    label1 = Label(screen7, image=photo2, bg="yellow")
    label1.place(x=325, y=80)

    photo3 = PhotoImage(file="back-arrow.png")
    pht10 = photo3.subsample(2,2)
    Button(screen7, bg="black", image=pht10, command=screen7.destroy).place(x=9, y=459)
    Label(text="").pack()

    photo9 = PhotoImage(file="tempsnipSHW.png")
    pht9 = photo9.subsample(1, 1)
    Button(screen7, bg="black", image=pht9, command=qsort_rb).place(x=617, y=200)
    Label(text="").pack()

    photo15 = PhotoImage(file="tempsnipdlt.png")
    pht15 = photo15.subsample(1, 1)
    Button(screen7, bg="black", image=pht15, command=deletebook).place(x=617, y=300)
    Label(text="").pack()

    global dltbook
    dltbook = StringVar()
    txt_dltbook = Entry(screen7, width=18, textvar=dltbook, bg='white', font=('Bradley Hand ITC', 16, 'bold'))
    txt_dltbook.place(x=200, y=165)

    global list2
    list2 = Listbox(screen7, height=12, width=65, bg='white', font=('constantia', 12, 'bold'))
    list2.place(x=9, y=208)

    screen7.mainloop()


def quicksort(Booking_list):
   quicksort1(Booking_list,0,len(Booking_list)-1)

def quicksort1(Booking_list,first,last):
   if first < last:

       splitpoint = spaces(Booking_list,first,last)

       quicksort1(Booking_list,first,splitpoint-1)
       quicksort1(Booking_list,splitpoint+1,last)


def spaces(Booking_list,first,last):
   pivotvalue = Booking_list[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and Booking_list[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while Booking_list[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = Booking_list[leftmark]
           Booking_list[leftmark] = Booking_list[rightmark]
           Booking_list[rightmark] = temp

   temp = Booking_list[first]
   Booking_list[first] = Booking_list[rightmark]
   Booking_list[rightmark] = temp


   return rightmark

def qsort_rb():
    list = []
    ff = open('ROOMBOOKINGS', 'r')
    f = ff.readlines()
    for i in f:
        list.append(i)
    b = len(list)

    quicksort(list)
    list2.delete(0, END)
    for i in range(0,len(list)):
        list2.insert(END, list[i])




def deletebook():
    bdlt = dltbook.get()
    with open("ROOMBOOKINGS", "r") as f:
        lines = f.readlines()
    with open("ROOMBOOKINGS", "w") as f:
        for line in lines:
            if line.split(',')[0] != bdlt:
                f.write(line)


# --- HOTEL WISE SEARCH ---
def Searching_details():
        screen10 = Toplevel()
        screen10.geometry('800x500+390+120')
        screen10.configure(bg='white')
        screen10.resizable(0, 0)

        photo1 = PhotoImage(file="d1b032bf-334d-438b-89dd-d74df04276fd.png")
        label = Label(screen10, image=photo1)
        label.pack()
        global search
        search = StringVar()

        choose_search = ttk.Combobox(screen10, width=14, textvariable=search, font=('Bradley Hand ITC', 14,))
        choose_search['values'] = ('PC', 'CROWNS INN', 'DAYS INN', 'AVARI', 'SARENA', 'SAFARI', 'KHYYAM')
        choose_search.place(x=220, y=155)




        photo92 = PhotoImage(file="tempsnipSEARCHHH.png")
        pht90 = photo92.subsample(1, 1)
        label1 = Label(screen10, image=pht90, bg="black")
        label1.place(x=410, y=146)


        photo2 = PhotoImage(file="tempsniphtb.png")
        label1 = Label(screen10, image=photo2, bg="yellow")
        label1.place(x=325, y=60)

        photo3 = PhotoImage(file="back-arrow.png")
        pht10 = photo3.subsample(2, 2)
        Button(screen10, bg="black", image=pht10, command=screen10.destroy).place(x=9, y=459)
        Label(text="").pack()

        photo9 = PhotoImage(file="tempsnipSHW.png")
        pht9 = photo9.subsample(1, 1)
        Button(screen10, bg="black", image=pht9, command=search_s).place(x=617, y=300)
        Label(text="").pack()

        global list3
        list3 = Listbox(screen10, height=12, width=65, bg='white', font=('constantia', 12, 'bold'))
        list3.place(x=9, y=208)

        screen10.mainloop()

def search_s():
    srch = search.get()
    list3.delete(0,END)

    with open('ROOMBOOKINGS') as reg_users:
        for users in reg_users:
            if users.split(',')[2] == srch:
                list3.insert(END,users)






      #-----------------------E N D       O F     A D M I N     W O R K S--------------------




                   #-----------------S T A R T       O F      G U E S T       W O R K S-----------------


# --- GUEST SIGN UP FORM ---
def signup_screen():
    global name
    global con
    global coun
    global password
    global NicPass
    global city
    screen2=Toplevel()
    screen2.geometry('800x500+390+120')
    screen2.title("GUEST SIGN UP DESK")
    screen2.configure(bg="white")
    screen2.resizable(0,0)
    photo = PhotoImage(file="signup screen.PNG")
    label = Label(screen2,image=photo)

    photo2 = PhotoImage(file="Capture1234.PNG")
    label1 = Label(screen2, image=photo2, bg="yellow")
    label1.place(x=325, y=80)

    name = StringVar()
    txt_name = Entry(screen2,width=18, textvar=name, bg='white', font=('constantia', 12, 'bold'))
    txt_name.place(x=180, y=180)

    con = StringVar()
    txt_con = Entry(screen2,width=18, textvar=con, bg='white', font=('constantia', 12, 'bold'))
    txt_con.place(x=180, y=268)

    coun = StringVar()
    txt_coun = Entry(screen2,width=18, textvar=coun, bg='white', font=('constantia', 12, 'bold'))
    txt_coun.place(x=180, y=357)

    password = StringVar()
    txt_password = Entry(screen2,width=18, textvar=password, bg='white', font=('constantia', 12, 'bold'))
    txt_password.place(x=618, y=180)

    NicPass = StringVar()
    txt_NicPass = Entry(screen2,width=18, textvar=NicPass, bg='white', font=('constantia', 12, 'bold'))
    txt_NicPass.place(x=618, y=268)

    city = StringVar()
    txt_city = Entry(screen2,width=18, textvar=city, bg='white', font=('constantia', 12, 'bold'))
    txt_city.place(x=618, y=357)

    photo5 = PhotoImage(file="Capture0.PNG")
    pht3 = photo5.subsample(1, 1)
    Button(screen2, bg="black", image=pht3, command=registration_textfiling).place(x=180, y=420)
    Label(text="").pack()

    photo6 = PhotoImage(file="back-arrow.png")
    pht4 = photo6.subsample(2,2)
    Button(screen2, bg="black", image=pht4, command=screen2.destroy).place(x=9, y=459)
    Label(text="").pack()





    label.pack()

    screen2.mainloop()

def registration_textfiling():
    naam = name.get()
    fone = con.get()
    mulk = coun.get()
    pas  = password.get()
    pehchan = NicPass.get()
    shehar = city.get()






    if (naam == '' or  fone == '' or mulk == '' or  pas ==  '' or  pehchan == '' or  shehar == '' '\n'):
        exit()
    else:
        RegGu = open("Registered Users", "a")

        RegGu.writelines(naam + ',' + fone + ',' + mulk + ',' + pas + ',' + pehchan + ',' + shehar + '\n')
        RegGu.close()
        print("GUEST REGISTERED......")
        print("________________________")
        print()
        guest_login()







#--- GUEST LOGIN FORM ---
def guest_login():


    global Guname
    global GuPASS

    screen8 = Toplevel()
    screen8.geometry('800x500+390+120')
    screen8.configure(bg='white')
    screen8.resizable(0,0)

    photo1 = PhotoImage(file="Guestentry.png")
    label = Label(screen8, image=photo1)
    label.pack()

    photo2 = PhotoImage(file="tempsnipgsl.png")
    label1 = Label(screen8, image=photo2, bg="yellow")
    label1.place(x=325, y=80)


    photo3 = PhotoImage(file="back-arrow.png")
    pht10 = photo3.subsample(2, 2)
    Button(screen8, bg="black", image=pht10, command=screen8.destroy).place(x=9, y=459)
    Label(text="").pack()

    Guname = StringVar()
    txt_Guname = Entry(screen8, width=18, textvar=Guname, bg='white', font=('Bradley Hand ITC', 29, 'bold'))
    txt_Guname.place(x=355, y=210)

    GuPASS = StringVar()
    txt_GuPASS = Entry(screen8, width=18, textvar=GuPASS, bg='white',show="*", font=('Bradley Hand ITC', 29, 'bold'))
    txt_GuPASS.place(x=355, y=322)

    photo6 = PhotoImage(file="tempsniplog.png")
    pht4 = photo6.subsample(1, 1)
    Button(screen8, bg="black", image=pht4, command=guest_login_check).place(x=180, y=415)
    Label(text="").pack()




    screen8.mainloop()

#LINEAR SEARCHING 
def guest_login_check():
    global nam_info
    global pas_info
    nam_info = Guname.get()
    pas_info = GuPASS.get()
    with open('Registered Users')as RegGu:
        for users in RegGu:
            if users.split(",")[0] == nam_info:
                if users.split(",")[3] == pas_info:
                    print("GUEST LOGIN......")
                    print("________________________")
                    print()
                    guest_booking_panel()

                else:

                    break

















# --- HOTEL BOOKING ---
def guest_booking_panel():
    global NMH
    global HRT
    global HDW
    global HMD
    global txt_BL

    screen9 = Toplevel()
    screen9.geometry('800x500+390+120')
    screen9.configure(bg='white')
    screen9.resizable(0,0)

    photo1 = PhotoImage(file="Work From HOme.png")
    label = Label(screen9, image=photo1)
    label.pack()

    NMH = StringVar()

    choose_NMH = ttk.Combobox(screen9, width=14, textvariable=NMH,font=('Bradley Hand ITC', 14,))
    choose_NMH['values'] = ('PC', 'CROWNS INN', 'DAYS INN', 'AVARI', 'SARENA', 'SAFARI','KHYYAM')
    choose_NMH.place(x=240, y=200)

    HRT = StringVar()

    choose_HRT = ttk.Combobox(screen9, width=14, textvariable=HRT, font=('Bradley Hand ITC', 14,))
    choose_HRT['values'] = ('SIMPLE', 'LUXIORIOUS')
    choose_HRT.place(x=623, y=200)



    HDW = StringVar()
    txt_HDW = Entry(screen9, width=14, textvar=HDW, bg='white', font=('Bradley Hand ITC', 14, 'bold'))
    txt_HDW.place(x=623, y=278)

    HMD = StringVar()
    txt_HMD = Entry(screen9, width=14, textvar=HMD, bg='white', font=('Bradley Hand ITC', 14, 'bold'))
    txt_HMD.place(x=240, y=277)


    txt_BL = Entry(screen9, width=14,bg='white', font=('Bradley Hand ITC', 16, 'bold'))
    txt_BL.place(x=450, y=349)






    photo21 = PhotoImage(file="tempsnipbila.png")
    pht22 = photo21.subsample(1, 1)
    Button(screen9, bg="black", image=pht22, command=guestloginWorks).place(x=200, y=340)
    Label(text="").pack()













    photo2 = PhotoImage(file="tempsniphtv.png")
    label1 = Label(screen9, image=photo2, bg="yellow")
    label1.place(x=325, y=80)




    photo003 = PhotoImage(file="back-arrow.png")
    pht180 = photo003.subsample(2,2)
    Button(screen9, bg="black", image=pht180, command=screen9.destroy).place(x=9, y=459)


    Label(text="").pack()


    screen9.mainloop()

def guestloginWorks():
    global naaam_info
    global paaass_info
    global NMH
    global HRT
    global HDW
    global HMD
    global B




    naaam_info = Guname.get()
    paaass_info = GuPASS.get()
    HN_info = NMH.get()
    HR_info = HRT.get()
    HD_info = HDW.get()
    FD_info = HMD.get()

    Pc_S = 3200
    Pc_L = 4500
    Cr_S = 3000
    Cr_L = 4200
    Di_S = 4000
    Di_L = 5200
    Av_S = 4200
    Av_L = 5400
    Sa_S = 3400
    Sa_L = 4500
    Si_S = 4100
    Si_L = 5300
    Kh_S = 3300
    Kh_L = 4500


    if HN_info == "PC" and  HR_info == 'SIMPLE':
       B =  Pc_S * int(FD_info)





    if HN_info == "PC" and HR_info == 'LUXIORIOUS':
        B = Pc_L * int(FD_info)



    if HN_info == "CROWNS INN" and HR_info == 'SIMPLE':
            B = Cr_S * int(FD_info)




    if HN_info == "CROWNS INN" and HR_info == 'LUXIORIOUS':
                B = Cr_L * int(FD_info)



    if HN_info == "DAYS INN" and HR_info == 'SIMPLE':
                    B = Di_S * int(FD_info)



    if HN_info == "DAYS INN" and HR_info == 'LUXIORIOUS':
                        B = Di_L * int(FD_info)



    if HN_info == "AVARI" and HR_info == 'SIMPLE':
                            B = Av_S * int(FD_info)


    if HN_info == "AVARI" and HR_info == 'LUXIORIOUS':
                                B = Av_L * int(FD_info)


    if HN_info == "SARENA" and HR_info == 'SIMPLE':
                                    B = Sa_S * int(FD_info)



    if HN_info == "SARENA" and HR_info == 'LUXIORIOUS':
                                        B = Sa_L * int(FD_info)



    if HN_info == "SAFARI" and HR_info == 'SIMPLE':
                                            B = Si_S * int(FD_info)


    if HN_info == "SAFARI" and HR_info == 'LUXIORIOUS':
                                                B = Si_L * int(FD_info)


    if HN_info == "KHYYAM" and HR_info == 'SIMPLE':
                                                    B = Kh_S * int(FD_info)


    if HN_info == "KHYYAM" and HR_info == 'LUXIORIOUS':
                                                        B = Kh_L * int(FD_info)

    txt_BL.insert(END,B)







    LogGu = open("ROOMBOOKINGS", "a")

    LogGu.writelines(naaam_info+ ','   +  paaass_info + ','+ HN_info + ',' + HR_info + ',' + HD_info + ',' + FD_info + ',' + str(B) + '\n')
    LogGu.close()





    # ---------- E N D    O F     G U E S T     W O R K S-----------

























 # ------------- F O R M      O F       C O N T A C T    U S ------------------

def contact_us():
    screen3 = Toplevel()

    screen3.geometry('800x500+390+120')
    screen3.title("RECEPTION DESK")
    screen3.configure(bg="white")
    screen3.resizable(0, 0)
    photo1 = PhotoImage(file="conuz.PNG")
    label = Label(screen3, image=photo1)
    label.pack()



    photo6 = PhotoImage(file="back-arrow.png")
    pht4 = photo6.subsample(2, 2)
    Button(screen3, bg="black", image=pht4, command=screen3.destroy).place(x=9, y=459)
    Label(text="").pack()



    photo2 = PhotoImage(file="tempsnip2.png")
    label1 = Label(screen3, image=photo2, bg="yellow")
    label1.place(x=323, y=80)


    screen3.mainloop()


                      # ----------------- M A I N S C R E E N ---------------

def main_screen():
    screen=Tk()
    screen.geometry("800x500+390+120")
    screen.title("APPLICATION BY DANIAL HAMMAD MAHAD")
    screen.configure(bg="yellow")
    screen.resizable(0,0)
    photo = PhotoImage(file="Mainimage.png")

    label = Label(screen, image=photo)
    label.pack()
    photo1 = PhotoImage(file="FRWD.png")
    Button(screen, image=photo1,bg="yellow",command=Imp_Note).place(x=470,y=390)

    photo2 = PhotoImage(file="EXT.png")
    Button(screen, image=photo2, bg="yellow", command=screen.destroy).place(x=55, y=390)
    screen.mainloop()
main_screen()
