from tkinter import*
import tkinter.messagebox
import tkinter.simpledialog

prozor=Tk()



prozor.title("Boj Boja")

gornji_okvir=Frame(prozor)
gornji_okvir.pack(fill=BOTH)

naslovnaTiketa=Label(gornji_okvir,text="BOJ BOJA",font=("Helvetica","24","bold"), bg="yellow",fg="Orange")
naslovnaTiketa.pack(fill=BOTH,expand=True)





def dugme1_crveno(event) :
        #BooleanVar.get()
         #pozadina="bg"["red","blue"]
         #if pozadina "red"> pozadina "blue":
            # pozadina"red"    
  
        dugme1["bg"]="red"
        #dugme1.bind("<Button-3>",dugme1_plavo)=False
            
                    
def dugme2_crveno (event) :
     dugme2["bg"]="red"
     
def dugme3_crveno (event) :
     dugme3["bg"]="red"

def dugme4_crveno (event) :
      dugme4["bg"]="red"

def dugme5_crveno (event) :
      dugme5["bg"]="red"

def dugme6_crveno (event) :
      dugme6["bg"]="red"

def dugme7_crveno (event) :
      dugme7["bg"]="red"
          
def dugme8_crveno (event) :
      dugme8["bg"]="red"

def dugme9_crveno (event) :
      dugme9["bg"]="red"

def dugme1_plavo(event) :
      dugme1["bg"]="blue"
      
def dugme2_plavo (event) :
     dugme2["bg"]="blue"
     
def dugme3_plavo (event) :
     dugme3["bg"]="blue"

def dugme4_plavo (event) :
      dugme4["bg"]="blue"

def dugme5_plavo (event) :
      dugme5["bg"]="blue"

def dugme6_plavo (event) :
      dugme6["bg"]="blue"

def dugme7_plavo (event) :
      dugme7["bg"]="blue"
          
def dugme8_plavo (event) :
      dugme8["bg"]="blue"

def dugme9_plavo (event) :
      dugme9["bg"]="blue"

levi_okvir=Frame(prozor)
levi_okvir.pack(side=LEFT)

def Ime_igrac1(event):
    ime1=tkinter.simpledialog.askstring("ime1","Kako Vam je ime?")
    izlaz1="%s"%(ime1)
    igrac1_et=Label(levi_okvir,text=izlaz1,font=("Helvetica","24","bold"),bg="red",fg="yellow")
    igrac1_et.pack()
    return

def Ime_igrac2(event):

    ime2=tkinter.simpledialog.askstring("ime2","Kako Vam je ime?")
    izlaz2="%s"%(ime2)
    igrac2_et=Label(levi_okvir,text=izlaz2,font=("Helvetica","24","bold"),bg="blue",fg="yellow")
    igrac2_et.pack()
    return
def pobednik_crveni(event):
     
#Pobeda crvenog igraca

    if  dugme1["bg"]=="red" and dugme2["bg"]=="red" and  dugme3["bg"]=="red":
          tkinter.messagebox.showinfo("Pobeda","Crveni je pobednik")
        
          
    elif dugme4["bg"]=="red" and dugme5["bg"]=="red" and  dugme6["bg"]=="red":
          tkinter.messagebox.showinfo("Pobeda","Crveni je pobednik")
          
    elif dugme7["bg"]=="red" and dugme8["bg"]=="red" and  dugme9["bg"]=="red":
          tkinter.messagebox.showinfo("Pobeda","Crveni je pobednik")
         

    elif dugme1["bg"]=="red" and dugme5["bg"]=="red" and  dugme9["bg"]=="red":
          tkinter.messagebox.showinfo("Pobeda","Crveni je pobednik")

    elif dugme3["bg"]=="red" and dugme5["bg"]=="red" and  dugme7["bg"]=="red":
          tkinter.messagebox.showinfo("Pobeda","Crveni je pobednik")  

    elif dugme1["bg"]=="red" and dugme4["bg"]=="red" and  dugme7["bg"]=="red":
          tkinter.messagebox.showinfo("Pobeda","Crveni je pobednik")  

    elif dugme2["bg"]=="red" and dugme5["bg"]=="red" and  dugme8["bg"]=="red":
          tkinter.messagebox.showinfo("Pobeda","Crveni je pobednik")
          
    elif dugme3["bg"]=="red" and dugme6["bg"]=="red" and  dugme9["bg"]=="red":
          
          tkinter.messagebox.showinfo("Pobeda","Crveni je pobednik")  
          #izlaz3="%s je pobednik".%(ime1)
      #,** bg=="red",fg="yellow",font=("Helvetica","24","bold"))

          #pobeda plavog igraca

    if  dugme1["bg"]=="blue" and dugme2["bg"]=="blue" and  dugme3["bg"]=="blue":
          tkinter.messagebox.showinfo("Pobeda","Plavi je pobednik")
        
          
    elif dugme4["bg"]=="blue" and dugme5["bg"]=="blue" and  dugme6["bg"]=="blue":
          tkinter.messagebox.showinfo("Pobeda","Plavi je pobednik")
          
    elif dugme7["bg"]=="blue" and dugme8["bg"]=="blue" and  dugme9["bg"]=="blue":
          tkinter.messagebox.showinfo("Pobeda","Plavi je pobednik")
         

    elif dugme1["bg"]=="blue" and dugme5["bg"]=="blue" and  dugme9["bg"]=="blue":
          tkinter.messagebox.showinfo("Pobeda","Plavi je pobednik")

    elif dugme3["bg"]=="blue" and dugme5["bg"]=="blue" and  dugme7["bg"]=="blue":
          tkinter.messagebox.showinfo("Pobeda","Plavi je pobednik")  

    elif dugme1["bg"]=="blue" and dugme4["bg"]=="blue" and  dugme7["bg"]=="blue":
          tkinter.messagebox.showinfo("Pobeda","Plavi je pobednik")  

    elif dugme2["bg"]=="blue" and dugme5["bg"]=="blue" and  dugme8["bg"]=="blue":
          tkinter.messagebox.showinfo("Pobeda","Plavi je pobednik")
          
    elif dugme3["bg"]=="blue" and dugme6["bg"]=="blue" and  dugme9["bg"]=="blue":
          tkinter.messagebox.showinfo("Pobeda","Plavi je pobednik")  

desni_okvir=Frame(prozor)
desni_okvir.pack(side=RIGHT)

pozadinskaEtiketa_desno=Label(desni_okvir,bg="yellow")
pozadinskaEtiketa_desno.pack()

pozadinskaEtiketa2_desno=Label(desni_okvir,bg="yellow")
pozadinskaEtiketa2_desno.pack()

pozadinskaEtiketa3_desno=Label(desni_okvir,bg="yellow")
pozadinskaEtiketa3_desno.pack()

dugmad=StringVar()


dugme1=Button(pozadinskaEtiketa_desno,text="Dugme1",height=2,width=5,cursor="spraycan",command =lambda:pobednik_crveni(dugme1))
dugme1.bind("<Button-1>",dugme1_crveno)
dugme1.bind("<Button-3>",dugme1_plavo)

dugme1.pack(side=LEFT)

dugme2=Button(pozadinskaEtiketa_desno,text="Dugme2",height=2,width=5,cursor="spraycan",command =lambda:pobednik_crveni(dugme2))
dugme2.bind("<Button-1>",dugme2_crveno)
dugme2.bind("<Button-3>",dugme2_plavo)
#dugme2.bind(pobednik_crveni)
dugme2.pack(side=LEFT)

dugme3=Button(pozadinskaEtiketa_desno,text="Dugme3",height=2,width=5,cursor="spraycan",command =lambda:pobednik_crveni(dugme3))
dugme3.bind("<Button-1>",dugme3_crveno)
dugme3.bind("<Button-3>",dugme3_plavo)
#dugme3.bind(pobednik_crveni)
dugme3.pack(side=LEFT)

dugme4=Button(pozadinskaEtiketa2_desno,text="Dugme4",height=2,width=5,cursor="spraycan",command =lambda:pobednik_crveni(dugme4))
dugme4.bind("<Button-1>",dugme4_crveno)
dugme4.bind("<Button-3>",dugme4_plavo)
dugme4.pack(side=LEFT)

dugme5=Button(pozadinskaEtiketa2_desno,text="Dugme5",height=2,width=5,cursor="spraycan",command= lambda:pobednik_crveni(dugme5))
dugme5.bind("<Button-1>",dugme5_crveno)
dugme5.bind("<Button-3>",dugme5_plavo)
dugme5.pack(side=LEFT)

dugme6=Button(pozadinskaEtiketa2_desno,text="Dugme6",height=2,width=5,cursor="spraycan",command= lambda:pobednik_crveni(dugme6))
dugme6.bind("<Button-1>",dugme6_crveno)
dugme6.bind("<Button-3>",dugme6_plavo)
dugme6.pack(side=LEFT)

dugme7=Button(pozadinskaEtiketa3_desno,text="Dugme7",height=2,width=5,cursor="spraycan",command= lambda:pobednik_crveni(dugme7))
dugme7.bind("<Button-1>",dugme7_crveno)
dugme7.bind("<Button-3>",dugme7_plavo)
dugme7.pack(side=LEFT)

dugme8=Button(pozadinskaEtiketa3_desno,text="Dugme8",height=2,width=5,cursor="spraycan",command= lambda:pobednik_crveni(dugme8))
dugme8.bind("<Button-1>",dugme8_crveno)
dugme8.bind("<Button-3>",dugme8_plavo)
dugme8.pack(side=LEFT)

dugme9=Button(pozadinskaEtiketa3_desno,text="Dugme9",height=2,width=5,cursor="spraycan",command= lambda:pobednik_crveni(dugme9))
dugme9.bind("<Button-1>",dugme9_crveno)
dugme9.bind("<Button-3>",dugme9_plavo)
dugme9.pack(side=LEFT)

#igrac1_et=Label(levi_okvir,text="Igrac 1:"+ str(),font=("Helvetica","24","bold"),bg="red",fg="yellow",width=10)

#igrac1_et.pack(fill=X)



#igrac2_et=Label(levi_okvir,text="Igrac2",font=("Helvetica","24","bold"),bg="blue",fg="yellow")
#igrac2_et.pack(fill=X)

        

#Unos_Imena1=Entry(prozor)
#UnosImena1.grid(row=0,column=1,sticky=E)
#Unos_Imena1.pack(side=LEFT)
def Zapocni_novu_igru(event):
       
       dugme1["bg"]="white"
       dugme2["bg"]="white"
       dugme3["bg"]="white"
       dugme4["bg"]="white"
       dugme5["bg"]="white"
       dugme6["bg"]="white"
       dugme7["bg"]="white"
       dugme8["bg"]="white"
       dugme9["bg"]="white"

Nova_igra=Button(desni_okvir,text="Nova igra",font=("Times","16"))
Nova_igra.bind("<Button-1>",Zapocni_novu_igru)
Nova_igra.pack(side=TOP,fill=BOTH)


Dugme_unosa1=Button(levi_okvir,heigh=1,width=3,text="Ime1",cursor="plus",bg="red",fg="yellow")
Dugme_unosa1.bind("<Button-1>",Ime_igrac1)
Dugme_unosa1.pack(anchor=W)

Dugme_unosa2=Button(levi_okvir,height=1,width=3,text="Ime2",cursor="plus",bg="blue",fg="yellow")
Dugme_unosa2.bind("<Button-1>",Ime_igrac2)
Dugme_unosa2.pack(anchor=W)

prozor.mainloop()
