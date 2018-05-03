from Tkinter import *

frame = Tk()
frame.geometry('1050x580+160+100')
frame.title('AIRLINE DATA SHEET')

# Top frame color
Top = Frame(frame, width=1000, height=100, bg="#808080")
Top.pack(side=TOP)


#MAIN LEFT FRAME
frame1 = Frame(frame, width=1000, height=450, bg="#808080")
frame1.pack(padx = 14,pady = 10,side=LEFT)

# MAIN LABEL
infoLabel = Label(Top, font=('Times New Roman', 30), text="AIRLINE DATA SHEET")
infoLabel.place(x=190,y=16)

# VARIABLES
PlaneNO = StringVar()
PlaneFROM = StringVar()
PlaneTO = StringVar()
PlaneDEPARTURE = StringVar()
PlaneARRIVAL = StringVar()
PlaneDURATION = StringVar()
PlanePRICE = StringVar()

def addPlaneInformation() :
    INFO = open("PlaneInformation.txt", "a+")
    text =str(PlaneNO.get())
    text2 = str(PlaneFROM.get())
    text3 = str(PlaneTO.get())
    text4 = str(PlaneDEPARTURE.get())
    text5 = str(PlaneARRIVAL.get())
    text6 = str(PlaneDURATION.get())
    text7 = str(PlanePRICE.get())

    TEXT = "\n"+text + " " + text2 +" " + text3+ " "+text4+" "+text5+" "+text6+" "+text7
    print TEXT
    INFO.write(TEXT)
    PlaneNO.set("")
    PlaneFROM.set("")
    PlaneTO.set("")
    PlaneDEPARTURE.set("")
    PlaneARRIVAL.set("")
    PlaneDURATION.set("")
    PlanePRICE.set("")
    INFO.close()


def clearPlaneInformation() :
    PlaneNO.set("")
    PlaneFROM.set("")
    PlaneTO.set("")
    PlaneDEPARTURE.set("")
    PlaneARRIVAL.set("")
    PlaneDURATION.set("")
    PlanePRICE.set("")

def findPlaneInformation() :
    planeno = PlaneNO.get()
    INFO = open("PlaneInformation.txt","r")
    lines = INFO.readlines()
    INFO.close()

    for i in lines :
        x = i.split()
        if (x[0] == planeno) :
            PlaneNO.set(planeno)
            PlaneFROM.set(x[1])
            PlaneTO.set(x[2])
            PlaneDEPARTURE.set(x[3]+" "+x[4])
            PlaneARRIVAL.set(x[5]+" "+x[6])
            PlaneDURATION.set(x[7])
            PlanePRICE.set(x[8])

def deletePlaneInformation() :
    Planeno = PlaneNO.get()
    INFO = open("PlaneInformation.txt" ,"r")
    lines = INFO.readlines()
    INFO.close()
    INFO = open("PlaneInformation.txt","w")

    for i in lines :
        x = i.split()
        if ( x[0] != Planeno) :
            INFO.write(i)


    PlaneNO.set("")
    INFO.close()

#frame 1 GUI TODO : TO ADD NEW Plane TO THE SYSTEM
PlaneNoLabel = Label(frame1, font=('aerial',20,'bold'),text='Plane No. : ',bg = "#FF4500")
PlaneNoLabel.place(x=110,y=30)
PlaneNoText = Entry(frame1, font=('aerial',20,'bold'),textvariable=PlaneNO,width=29,justify='right')
PlaneNoText.place(x=265,y=30)

PlaneFromLabel = Label(frame1, font=('aerial',20,'bold'),text='From : ',bg="#FF4500")
PlaneFromLabel.place(x=110,y=80)
PlaneFromText = Entry(frame1, font=('aerial',20,'bold'),textvariable=PlaneFROM,width=10,justify='right')
PlaneFromText.place(x=265,y=80)

PlaneToLabel = Label(frame1, font=('aerial',20, 'bold'),text='To : ',bg = "#FF4500")
PlaneToLabel.place(x=425,y=80)
PlaneToText = Entry(frame1, font=('aerial',20,'bold'),textvariable=PlaneTO,width= 9,justify='right')
PlaneToText.place(x=544,y=80)

PlaneDepartureLabel = Label(frame1, font=('aerial',20,'bold'),text='Departure :',bg = "#FF4500")
PlaneDepartureLabel.place(x=110,y=130)
PlaneDepartureText = Entry(frame1, font=('aerial',20,'bold'),textvariable=PlaneDEPARTURE,width=10,justify='right')
PlaneDepartureText.place(x=265,y=130)

PlaneArrivalLabel = Label(frame1,font=('aerial',20,'bold'),text='Arrival : ',bg = "#FF4500")
PlaneArrivalLabel.place(x=425,y=130)
PlaneArrivalText = Entry(frame1, font=('aerial',20,'bold'),textvariable=PlaneARRIVAL,width=9,justify='right')
PlaneArrivalText.place(x=544,y=130)

PlaneDurationLabel = Label(frame1, font=('aerial',20, 'bold'),text='Duration : ',bg = "#FF4500")
PlaneDurationLabel.place(x=110,y=180)
PlaneDurationText = Entry(frame1, font=('aerial',20,'bold'),textvariable=PlaneDURATION,width = 29,justify='right')
PlaneDurationText.place(x=265,y=180)

PlanePriceLabel = Label(frame1, font=('aerial',20,'bold'),text='Price(Rs) : ',bg = "#FF4500")
PlanePriceLabel.place(x=110,y=230)
PlanePriceText = Entry(frame1, font=('aerial',20,'bold'),textvariable=PlanePRICE,width=29,justify='right')
PlanePriceText.place(x=265,y=230)


AddPlaneButton = Button(frame1,fg='black',font=('aerial',20,'bold'),height=1,width=11,text='Add Airline',command = addPlaneInformation,bg="#FFD700")
AddPlaneButton.place(x=265,y=280)

DeleteButton = Button(frame1,fg='black',font=('aerial',20,'bold'),height=1,width=11,text='Delete',command = deletePlaneInformation ,bg = "#FFD700")
DeleteButton.place(x=495,y=280)


CLearButton = Button(frame1,fg='black',font=('aerial',20,'bold'),height=1,width=11,text='Clear',command = clearPlaneInformation ,bg = "#FFD700")
CLearButton.place(x=695,y=280)


FindButton = Button(frame1,fg='black',font=('aerial',20,'bold'),height=1,width=11,text='Find',command = findPlaneInformation ,bg = "#FFD700")
FindButton.place(x=495,y=380)
frame.mainloop()