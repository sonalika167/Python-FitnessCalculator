from tkinter import*
import sys
from tkinter import messagebox
import sqlite3

x=sqlite3.connect("fc.db")
c=x.cursor()

class welcome():

    def __init__(self, master):
        self.master=master
        self.master.geometry("500x500+500+180")
        self.master.resizable(0,0)
        self.master.title("Welcome")
        self.master.configure(background="#e6ffcc")
        photo=PhotoImage(file='hrt.gif')
        self.limage=Label(self.master, image=photo,width=500, height=500)
        self.limage.image=photo
        self.limage.place(x=0, y=0)
        self.title=Label(self.master, text="Welcome to Fitness Calculator", font=("Matura MT Script Capitals", 22), bg="black", fg="white").place(x=45, y=19)
        self.bmi=Button(self.master, text="Calculate BMI", bg="#cc6600",fg="white", font=("Berlin Sans FB",13), command=self.gotobmi, width=20).place(x=160, y=80)#bmibtn
        pic=PhotoImage(file='infos.gif')
        self.infobmi=Button(self.master, image=pic, width=27, height=27, bg="black", bd=0, command=self.bmiinfo)#infobmi
        self.infobmi.image=pic
        self.infobmi.place(x=365, y=80)
        self.vo2=Button(self.master, text="Calculate VO2 MAX", bg="#cc6600",fg="white", font=("Berlin Sans FB",13), command=self.gotovo2, width=20).place(x=160, y=130)#vo2btn
        self.infovo2=Button(self.master, image=pic, width=27, height=27, bg="black", bd=0, command=self.vo2info)#infovo2
        self.infovo2.image=pic
        self.infovo2.place(x=365, y=130)
        self.vo2=Button(self.master, text="Calculate BMR", bg="#cc6600",fg="white", font=("Berlin Sans FB",13), command=self.gotobmr, width=20).place(x=160, y=180)#bmrbutton
        self.inforeport=Button(self.master, image=pic, width=27, height=27, bg="black", bd=0, command=self.bmrinfo)#infobmr
        self.inforeport.image=pic
        self.inforeport.place(x=365, y=180)
        self.report=Button(self.master, text="Generate Report", bg="#cc6600",fg="white", font=("Berlin Sans FB",13), command=self.gotoreport, width=20).place(x=160, y=230)#reportbtn
        self.inforeport=Button(self.master, image=pic, width=27, height=27, bg="black", bd=0, command=self.reportinfo)#inforeport
        self.inforeport.image=pic
        self.inforeport.place(x=365, y=230)
        self.bmr=Button(self.master, text="Calculate BFC", bg="#cc6600",fg="white", font=("Berlin Sans FB",13), command=self.gotobfc, width=20).place(x=160, y=280)#bfcbtn
        self.infobmr=Button(self.master, image=pic, width=27, height=27, bg="black", bd=0, command=self.bfcinfo)#infobfc
        self.infobmr.image=pic
        self.infobmr.place(x=365, y=280)
        self.cal=Button(self.master, text="Calorie Calculator", bg="#cc6600",fg="white", font=("Berlin Sans FB",13), command=self.gotocalorie, width=20).place(x=160, y=330)#bfcbtn
        self.infocal=Button(self.master, image=pic, width=27, height=27, bg="black", bd=0, command=self.calorieinfo)#infobmi
        self.infocal.image=pic
        self.infocal.place(x=365, y=330)
        self.exit=Button(self.master, text="EXIT", bg="#cc6600",fg="white", font=("Berlin Sans FB",13), command=self.gotoexit, width=20).place(x=160, y=380)

    def bmiinfo(self):
        msg="The body mass index (BMI) or Quetelet index is a value derived from the mass (weight) and height of an individual. The BMI is defined as the body mass divided by the square of the body height, and is universally expressed in units of kg/m2, resulting from mass in kilograms and height in meters.\nThe BMI is an attempt to quantify the amount of tissue mass (muscle, fat, and bone) in an individual, and then categorize that person as underweight, normal weight, overweight, or obese based on that value. "
        messagebox.showinfo("About BMI", msg)

    def vo2info(self):
        msg="VO2 max (also maximal oxygen consumption, maximal oxygen uptake, peak oxygen uptake or maximal aerobic capacity) is the maximum rate of oxygen consumption measured during incremental exercise (exercise of increasing intensity). The name is derived from V - volume, O2 - oxygen, max - maximum. Maximal oxygen consumption reflects the cardiorespiratory fitness of an individual and is an important determinant of their endurance capacity during prolonged exercise."
        messagebox.showinfo("About VO2 MAX", msg)

    def bmrinfo(self):
        msg="The basal metabolic rate (BMR) is the amount of energy needed while resting in a temperate environment when the digestive system is inactive."
        messagebox.showinfo("About BMR", msg)

    def reportinfo(self):
        msg="This module generates a patient report and based on the inputs tells the range in which your vitals lies. This includes Blood pressure, Pulse rate, WBC count, RBC count, Haemoglobin level and cholestrol level."
        messagebox.showinfo("About Report", msg)

    def bfcinfo(self):
        msg="The scientific term for body fat is adipose tissue. Adipose tissue serves a number of important functions. Its primary purpose is to store lipids from which the body creates energy."
        messagebox.showinfo("About BFC", msg)

    def calorieinfo(self):
        msg="The Calorie Calculator can be used to estimate the number of calories a person needs to consume each day. This Calorie Calculator is based on the Mifflin-St Jeor Equation which calculates basal metabolic rate (BMR), and its results are based on an estimated average.t is important to remember that proper diet and exercise is largely accepted as the best way to lose weight."
        messagebox.showinfo("About Calorie Count", msg)

    def gotobmi(self):
        root2=Toplevel(self.master)
        bmigui=bmi(root2)

    def gotovo2(self):
        root3=Toplevel(self.master)
        vo2gui=vo2(root3)

    def gotobmr(self):
        root4=Toplevel(self.master)
        bmrgui=bmr(root4)

    def gotoreport(self):
        root5=Toplevel(self.master)
        reportgui=report(root5)

    def gotobfc(self):
        root6=Toplevel(self.master)
        bfcgui=bfc(root6)

    def gotocalorie(self):
        root7=Toplevel(self.master)
        caloriegui=calorie(root7)

    def gotoexit(self):
        self.master.destroy()

class bmi():
     
    def __init__(self, master):
        self.master=master
        self.master.geometry("500x500+500+180")
        self.height=DoubleVar()
        self.weight=DoubleVar()
        self.choice=IntVar()
        self.master.resizable(0,0)
        self.master.title("Body Mass Index")
        self.master.configure(background="#332324")
        self.title=Label(self.master, text="Body Mass Index Calculator",font=("Britannic Bold",22, "bold"), fg="white", bg="#332324" ).place(x=50, y=18)
        self.lheight=Label(self.master, text="Height ", font=("Franklin Gothic Medium",13,"bold"), fg="white", bg="#332324")
        self.lheight.place(x=75, y=80)
        self.eheight=Entry(self.master, textvariable=self.height, width=20, bg="white")
        self.eheight.delete(0, 'end')
        self.eheight.focus()
        self.eheight.place(x=190,y=82)
        self.metric=Radiobutton(self.master, text="Kg & cm",font=("Franklin Gothic Medium",10,"italic"), variable=self.choice,width=15, value=0, bg="white", fg="black")
        self.metric.place(x=350, y=78)
        self.us=Radiobutton(self.master, text="pound & feets",font=("Franklin Gothic Medium",10,"italic"), variable=self.choice,width=15, value=1, bg="white", fg="black")
        self.us.place(x=350, y=110)
        self.lweight=Label(self.master, text="Weight ", font=("Franklin Gothic Medium",13, "bold"), fg="white", bg="#332324").place(x=75, y=110)
        self.eweight=Entry(self.master, textvariable=self.weight, width=20, bg="white")
        self.eweight.delete(0, 'end')
        self.eweight.focus()
        self.eweight.place(x=190,y=112)
        self.clear=Button(self.master, text="Reset", command=self.clr,font=("Berlin Sans FB",13), fg="#332324", bg="white", width=10).place(x=300, y=160)
        self.calculate=Button(self.master, text="Calculate",font=("Berlin Sans FB",13), command=self.calculatebmi, fg="#332324", bg="white", width=10).place(x=110,y=160)
        self.result=Text(self.master, state=DISABLED, bg="white",font=("Segoe UI Semibold",13))
        self.result.place(x=50, y=210, width=400, height=200)
        self.back=Button(self.master, text="<- Back",font=("Berlin Sans FB",13), command=self.back, fg="#332324", bg="white").place(x=383, y=435)
     
    def calculatebmi(self):
        ch=self.choice.get()
        rheight=self.height.get()
        rweight=self.weight.get()
        if ch==1:
            rweight*=703
            rheight*=12
            rheight*=rheight
            bmi=rweight/rheight
        elif ch==0:
            rheight=rheight/100
            rheight*=rheight
            bmi=rweight/rheight
        if(bmi<18.5):
            msg="\n\nYou are underweight\nTry to consume more calories than you burn\n"

        elif(bmi>=18.5 and bmi<25):
            msg="\n\nYou are Normal\nGoing good. Maintain your diet."
        elif(bmi>=25 and bmi<30):
            msg="\nYou are Overweight\nYou need to cut down your calorie intake and do some physical activity"
        else:
            msg="\n\nYou are Obese\nTry to loose weight and if you can't consult a doctor "
        self.result.config(state=NORMAL)
        self.result.insert(END, "Your BMI is %.2f " % bmi + msg)
        self.result.see("end")
        self.result.config(state=DISABLED)

    def clr(self):
        self.eheight.delete(0, 'end')
        self.eweight.delete(0, 'end')
        self.result.config(state=NORMAL)
        self.result.delete('1.0', END)
        self.result.config(state=DISABLED)
        
    def back(self):
        self.master.destroy();

class vo2():
   def gotoimg(self):
        root3=Toplevel(self.master)
        imggui=seeimg(root3)
        
   def __init__(self, master):
        self.master=master
        self.master.geometry("500x500+500+180")
        self.weight=IntVar()
        self.age=IntVar()
        self.hrate=IntVar()
        self.time=IntVar()
        self.male=IntVar()
        self.master.resizable(0,0)
        self.master.title("VO2")
        self.master.configure(background="#332324")
        self.title=Label(self.master, text="VO2 Max Calculator",font=("Britannic Bold",22, "bold"),fg="white", bg="#332324").place(x=135, y=18)
        self.lweight=Label(self.master, text="Weight(in Kg):",font=("Franklin Gothic Medium",13,"bold"),fg="white", bg="#332324").place(x=80, y=80)
        self.eweight=Entry(self.master, textvariable=self.weight, width=30)
        self.eweight.delete(0, 'end')
        self.eweight.focus()
        self.eweight.place(x=210,y=82)
        self.lage=Label(self.master, text="Age(in Years):",font=("Franklin Gothic Medium",13,"bold"),fg="white", bg="#332324").place(x=80, y=120)
        self.eage=Entry(self.master, textvariable=self.age, width=30)
        self.eage.delete(0, 'end')
        self.eage.focus()
        self.eage.place(x=210,y=120)
        self.lhrate=Label(self.master, text="Heart Rate",font=("Franklin Gothic Medium",13,"bold"),fg="white", bg="#332324").place(x=80, y=160)
        self.ehrate=Entry(self.master, textvariable=self.hrate, width=30)
        self.ehrate.delete(0, 'end')
        self.ehrate.focus()
        self.ehrate.place(x=210,y=160)
        self.ltime=Label(self.master, text="Time(in Min):",font=("Franklin Gothic Medium",13,"bold"),fg="white", bg="#332324").place(x=80, y=200)
        self.etime=Entry(self.master, textvariable=self.time, width=30)
        self.etime.delete(0, 'end')
        self.etime.focus()
        self.etime.place(x=210,y=200)
        self.lbut=Label(self.master, text="Gender:",font=("Franklin Gothic Medium",13,"bold"),fg="white", bg="#332324").place(x=80,y=240)
        self.ebut1=Radiobutton(self.master,text="Male",font=("Franklin Gothic Medium",13,"bold"),bg="white", fg="#332324",value=1, variable=self.male).place(x=210,y=240)
        self.ebut2=Radiobutton(self.master,text="Female",font=("Franklin Gothic Medium",13,"bold"), bg="white",fg="#332324",value=2, variable=self.male).place(x=300,y=240)
        self.calculate=Button(self.master, text="Calculate",font=("Berlin Sans FB",13),bg="white", fg="#332324",command=self.calculatevo2).place(x=70,y=300)
        self.clear=Button(self.master, text="Reset",font=("Berlin Sans FB",13), fg="#332324", bg="white",command=self.clr).place(x=400, y=300)
        self.result=Text(self.master, state=DISABLED,font=("Segoe UI Semibold",13))
        self.result.place(x=50, y=340, width=400, height=120)
        self.back=Button(self.master, text="<- Back",font=("Berlin Sans FB",13),bg="white", fg="#332324",command=self.back).place(x=425, y=465)
        self.seeimg=Button(self.master, text="click here to view standard values", bg="white",fg="#332324", font=("Berlin Sans FB",13),command=self.gotoimg).place(x=100, y=465)

   def calculatevo2(self):
       rweight=self.weight.get()
       rage=self.age.get()
       rhrate=self.hrate.get()
       rtime=self.time.get()
       x=self.male.get()
       if x==1: 
          vo2=132.853 - (0.0769*rweight*2.0462262) - (0.3877 *rage) + (6.315 *1) - (3.2649 *rtime) - (0.1565 *rhrate)
       else:
          vo2=132.853 - (0.0769*rweight*2.0462262) - (0.3877 *rage) + (6.315 *0) - (3.2649 *rtime) - (0.1565 *rhrate)    
       self.result.config(state=NORMAL)
       self.result.insert(END, "    Your vo2 is %.2f "% vo2 )
       self.result.see("end")
       self.result.config(state=DISABLED)

   def clr(self):
        self.eweight.delete(0,'end')
        self.eage.delete(0,'end')
        self.ehrate.delete(0, 'end')
        self.etime.delete(0, 'end')
        self.result.config(state=NORMAL)
        self.result.delete('1.0', END)
        self.result.config(state=DISABLED)

   def back(self):
        self.master.destroy();


class seeimg():
      
   def __init__(self, master):
        self.master=master
        self.master.geometry("500x500+500+180")
        self.master.resizable(0,0)
        self.master.title("Vo2 Values")
        self.master.configure(background="#332324")
        photo=PhotoImage(file='chart.gif')
        self.limage=Label(self.master, image=photo,width=500, height=500,bg="#332324")
        self.limage.image=photo
        self.limage.place(x=10, y=10)

  
        self.back=Button(self.master, text="<- Back",font=("Berlin Sans FB",13),bg="white", fg="#332324",command=self.back).place(x=0, y=5)


   def back(self):
        self.master.destroy();        


class bmr():
        
    def __init__(self, master):
        self.master=master
        self.master.geometry("500x500+500+180")
        self.height=IntVar()
        self.weight=IntVar()
        self.age=IntVar()
        self.gender=IntVar()
        self.master.resizable(0,0)
        self.master.title("Basal Metabolic Rate")
        self.master.configure(background="#332324")        
        self.title=Label(self.master, text="Basal Metabolic Rate Calculator",font=("Britannic Bold",22, "bold"), fg="white", bg="#332324" ).place(x=45, y=18)
        self.lheight=Label(self.master, text="Height (in cm)", font=("Franklin Gothic Medium",13,"bold"), fg="white", bg="#332324").place(x=75, y=80)
        self.eheight=Entry(self.master, textvariable=self.height, width=30)
        self.eheight.delete(0, 'end')
        self.eheight.focus()
        self.eheight.place(x=210,y=82)
        self.lweight=Label(self.master, text="Weight (in kg)", font=("Franklin Gothic Medium",13, "bold"), fg="white", bg="#332324").place(x=75, y=110)
        self.eweight=Entry(self.master, textvariable=self.weight, width=30)
        self.eweight.delete(0, 'end')
        self.eweight.focus()
        self.eweight.place(x=210,y=112)
        self.lage=Label(self.master, text="Age", font=("Franklin Gothic Medium",13, "bold"), fg="white", bg="#332324").place(x=75, y=140)
        self.eage=Entry(self.master, textvariable=self.age, width=30)
        self.eage.delete(0, 'end')
        self.eage.focus()
        self.eage.place(x=210,y=142)
        self.lgender=Label(self.master, text="Gender", font=("Franklin Gothic Medium",13, "bold"), fg="white", bg="#332324").place(x=75, y=170)
        self.male=Radiobutton(self.master, text="Male", variable=self.gender, value=0, font=("Franklin Gothic Medium",10, "bold"), fg="black", bg="white")
        self.male.place(x=210, y=170)
        self.female=Radiobutton(self.master, text="Female", variable=self.gender, value=1, font=("Franklin Gothic Medium",10, "bold"), fg="black", bg="white")
        self.female.place(x=300, y=170)
        self.clear=Button(self.master, text="Reset", command=self.clr,font=("Berlin Sans FB",13), fg="#332324", bg="white", width=10).place(x=300, y=210)
        self.calculate=Button(self.master, text="Calculate",font=("Berlin Sans FB",13), command=self.calculatebmr, fg="#332324", bg="white", width=10).place(x=110,y=210)
        self.result=Text(self.master, state=DISABLED,font=("Segoe UI Semibold",13))
        self.result.place(x=50, y=250, width=400, height=180)
        self.back=Button(self.master, text="<- Back",font=("Berlin Sans FB",13), command=self.back).place(x=383, y=435)
         
    def calculatebmr(self):
        rgender=self.gender.get()
        rheight=self.height.get()
        rage=self.age.get()
        rweight=self.weight.get()
        if rgender == 0:
            bmr = 66 + (6.2 * rweight) + (12.7 * rheight) - (6.76 * rage)    
        else:
            bmr = 655 + (4.35 * rweight) + (4.7 * rheight) - (4.7 * rage)
        msg="calories/day"
        self.result.config(state=NORMAL)
        self.result.insert(END, "Your BMR is %.2f " % bmr + msg)
        self.result.config(state=DISABLED)

    def clr(self):
        self.eheight.delete(0, 'end')
        self.eweight.delete(0, 'end')
        self.eage.delete(0, 'end')
        self.result.config(state=NORMAL)
        self.result.delete('1.0', END)
        self.result.config(state=DISABLED)
        
    def back(self):
        self.master.destroy();



class report():
        
    def __init__(self, master):
        self.master=master
        self.master.geometry("500x500+500+180")
        self.nm=StringVar()
        self.ag=IntVar()
        self.gndr=StringVar(value="Male")
        self.bl=IntVar()
        self.bh=IntVar()
        self.pl=IntVar()
        self.rb=DoubleVar()
        self.wb=DoubleVar()
        self.cl=IntVar()
        self.hmb=DoubleVar()
        self.master.resizable(0,0)
        self.master.title("Report Generator")
        self.master.configure(background="#332324")
        self.title=Label(self.master, text="Report Generator",font=("Britannic Bold",17, "bold"), fg="white", bg="#332324" ).place(x=160, y=9)
        self.lname=Label(self.master, text="Name", font=("Franklin Gothic Medium",12, "bold"), fg="white", bg="#332324").place(x=35, y=60)
        self.ename=Entry(self.master, textvariable=self.nm, width=20, bg="white")
        self.ename.delete(0, 'end')
        self.ename.focus()
        self.ename.place(x=105,y=60)
        self.lage=Label(self.master, text="Age", font=("Franklin Gothic Medium",12, "bold"), fg="white", bg="#332324").place(x=270, y=60)
        self.eage=Entry(self.master, textvariable=self.ag, width=20, bg="white")
        self.eage.delete(0, 'end')
        self.eage.focus()
        self.eage.place(x=325,y=60)
        self.gender=Label(self.master, text="Gender", font=("Franklin Gothic Medium",12, "bold"), fg="white", bg="#332324").place(x=35, y=100)
        self.male=Radiobutton(self.master, text="Male", variable=self.gndr, value="Male", font=("Franklin Gothic Medium",10, "bold"), fg="black", bg="white")
        self.male.place(x=105, y=100)
        self.female=Radiobutton(self.master, text="Female", variable=self.gndr, value="Female", font=("Franklin Gothic Medium",10, "bold"), fg="black", bg="white")
        self.female.place(x=205, y=100)
        self.bplow=Label(self.master, text="BP(low/Systolic)", font=("Franklin Gothic Medium",10, "bold"), fg="white", bg="#332324").place(x=105, y=155)
        self.ebplow=Entry(self.master, textvariable=self.bl, width=20, bg="white")
        self.ebplow.delete(0, 'end')
        self.ebplow.place(x=250,y=155)
        self.lbphigh=Label(self.master, text="BP(high/Diastolic)", font=("Franklin Gothic Medium",10, "bold"), fg="white", bg="#332324").place(x=105, y=185)
        self.ebphigh=Entry(self.master, textvariable=self.bh, width=20, bg="white")
        self.ebphigh.delete(0, 'end')
        self.ebphigh.place(x=250,y=185)
        self.lpulse=Label(self.master, text="Pulse Rate", font=("Franklin Gothic Medium",10, "bold"), fg="white", bg="#332324").place(x=105, y=215)
        self.epulse=Entry(self.master, textvariable=self.pl, width=20, bg="white")
        self.epulse.delete(0, 'end')
        self.epulse.place(x=250,y=215)
        self.lrbc=Label(self.master, text="RBC Count(x10^12/L)", font=("Franklin Gothic Medium",10, "bold"), fg="white", bg="#332324").place(x=105, y=245)
        self.erbc=Entry(self.master, textvariable=self.rb, width=20, bg="white")
        self.erbc.delete(0, 'end')
        self.erbc.place(x=250,y=245)
        self.lcholestrol=Label(self.master, text="Cholestrol(mg/dL)", font=("Franklin Gothic Medium",10, "bold"), fg="white", bg="#332324").place(x=105, y=275)
        self.echolestrol=Entry(self.master, textvariable=self.cl, width=20, bg="white")
        self.echolestrol.delete(0, 'end')
        self.echolestrol.place(x=250,y=275)
        self.lhb=Label(self.master, text="Haemoglobin(g/dL)", font=("Franklin Gothic Medium",10, "bold"), fg="white", bg="#332324").place(x=105, y=305)
        self.ehb=Entry(self.master, textvariable=self.hmb, width=20, bg="white")
        self.ehb.delete(0, 'end')
        self.ehb.place(x=250,y=305)
        self.lwbc=Label(self.master, text="WBC Count(x10^9/L)", font=("Franklin Gothic Medium",10, "bold"), fg="white", bg="#332324").place(x=105, y=335)
        self.ewbc=Entry(self.master, textvariable=self.wb, width=20, bg="white")
        self.ewbc.delete(0, 'end')
        self.ewbc.place(x=250,y=335)
        self.clear=Button(self.master, text="Reset", command=self.clr, font=("Berlin Sans FB",13), fg="#332324", bg="white", width=10).place(x=35, y=380)
        self.generate=Button(self.master, text="Generate Report",font=("Berlin Sans FB",13), command=self.generate, fg="#332324", bg="white", width=15).place(x=190,y=380)
        self.fetch=Button(self.master, text="Fetch record",font=("Berlin Sans FB",13), command=self.fetch, fg="#332324", bg="white", width=15).place(x=190,y=430)
        self.back=Button(self.master, text="<- Back",font=("Berlin Sans FB",13), command=self.back, fg="#332324", bg="white").place(x=383, y=380)

    def fetch(self):
        self.name=""
        self.age=""
        self.bphigh=""
        self.pulse=""
        self.rbc=""
        self.wbc=""
        self.hb=""
        self.cholestrol=""
        root5=Toplevel(self.master)
        generatedgui=reportout(root5, self.name, self.age, self.bphigh, self.pulse, self.rbc, self.cholestrol, self.hb, self.wbc)  
    
    def generate(self):
        if len(self.ebplow.get())==0 or len(self.ebphigh.get())==0 or len(self.echolestrol.get())==0 or len(self.ewbc.get())==0 or len(self.erbc.get())==0 or len(self.epulse.get())==0 or len(self.ehb.get())==0 or len(self.ename.get())==0 or len(self.eage.get())==0 :
            messagebox.showinfo("attention", "you can't leave any field empty")
            root4=Toplevel(self.master)
            reportgui=report(root4)
        oname=self.nm.get()
        obplow=self.bl.get()
        obphigh=self.bh.get()
        if obphigh<=90 or obplow<=60:
            obphigh="Low BP"
        elif obphigh<120 and obplow<80:
            obphigh="Normal BP"
        elif obphigh>=120 or obplow>=80:
            obphigh="High BP"
        oage=self.ag.get()
        opulse=self.pl.get()
        if opulse<=55:
            opulse="Athletic"
        elif opulse<=61:
            opulse="Excellent"
        elif opulse<=69:
            opulse="Above average"
        elif opulse>=70 and opulse<=75:
            opulse="Average"
        elif opulse>75:
            opulse="Below average"
        orbc=self.rb.get()
        if orbc<=2.4:
            orbc="Low count"
        elif orbc>2.4 and orbc<=5.6:
            orbc="Normal count"
        elif orbc>5.6:
            orbc="High count"
        owbc=self.wb.get()
        if owbc<=3.8:
            owbc="Low count"
        elif owbc>3.8 and owbc<=18.6:
            owbc="Normal count"
        elif owbc>18.6:
            owbc="High count"
        ogender=self.gndr.get()
        ocholestrol=self.cl.get()
        ohb=self.hmb.get()
        if ogender=="Male":
            if ohb<=13.5:
                ohb="Low"
            elif ohb >13.5 and ohb<=17.5:
                ohb="Normal"
            elif ohb>17.5:
                ohb="High"
        elif ogender=="Female":
            if ohb<=12.0:
                ohb="Low"
            elif ohb >12.0 and ohb<=15.5:
                ohb="Normal"
            elif ohb>15.5:
                ohb="High"
        if ocholestrol<=200:
            ocholestrol="Normal"
        elif ocholestrol<=239 and ocholestrol>200:
            ocholestrol="Borderline High"
        else:
            ocholestrol="High"
            
        rroot=Toplevel(self.master)
        generatedgui=reportout(rroot,oname, oage, obphigh, opulse, orbc, ocholestrol, ohb, owbc)

        
    def clr(self):
        self.ename.delete(0, 'end')
        self.eage.delete(0, 'end')
        self.ebplow.delete(0, 'end')
        self.ebphigh.delete(0, 'end')
        self.epulse.delete(0, 'end')
        self.erbc.delete(0, 'end')
        self.ewbc.delete(0, 'end')
        self.echolestrol.delete(0, 'end')
        self.ehb.delete(0, 'end')

    def back(self):
        self.master.destroy();

        
class reportout():
    
    def __init__(self, master,name, age, bphigh, pulse, rbc, cholestrol, hb, wbc):
        self.master=master
        self.master.geometry("500x500+500+180")
        self.bphigh=bphigh
        self.pulse=pulse
        self.rbc=rbc
        self.wbc=wbc
        self.cholestrol=cholestrol
        self.hb=hb
        self.name=name
        self.age=age
        self.master.resizable(0,0)
        self.master.title("Report Generator")
        self.master.configure(background="#332324")
        self.title=Label(self.master, text="Generated Report",font=("Britannic Bold",22, "bold"), fg="white", bg="#332324" ).place(x=130, y=15)
        self.note=Label(self.master, text="->Enter name whose record you want to fetch<-", font=("Calibri", 10, "italic"),fg="white", bg="#332324").place(x=125, y=56) 
        self.lname=Label(self.master, text="Name", font=("Franklin Gothic Medium",12, "bold"), fg="white", bg="#332324").place(x=105, y=100)
        self.ename=Text(self.master, width=20, height=1,  bg="white", font=("Segoe UI Semibold", 12))
        self.ename.insert(END, self.name)
        self.ename.place(x=250,y=100) 
        self.lage=Label(self.master, text="Age", font=("Franklin Gothic Medium",12, "bold"), fg="white", bg="#332324").place(x=105, y=140)
        self.eage=Text(self.master, width=20, height=1, bg="white", font=("Segoe UI Semibold", 12))
        self.eage.insert(END, self.age )
        self.eage.place(x=250,y=140)
        self.lbphigh=Label(self.master, text="BP", font=("Franklin Gothic Medium",12, "bold"), fg="white", bg="#332324").place(x=105, y=180)
        self.ebphigh=Text(self.master, width=20, height=1, bg="white", font=("Segoe UI Semibold", 12))
        self.ebphigh.insert(END, self.bphigh )
        self.ebphigh.place(x=250,y=180)
        self.lpulse=Label(self.master, text="Pulse Rate", font=("Franklin Gothic Medium",12, "bold"), fg="white", bg="#332324").place(x=105, y=220)
        self.epulse=Text(self.master, width=20, height=1, bg="white", font=("Segoe UI Semibold", 12))
        self.epulse.insert(END, self.pulse )
        self.epulse.place(x=250,y=220)
        self.lrbc=Label(self.master, text="RBC Count", font=("Franklin Gothic Medium",12, "bold"), fg="white", bg="#332324").place(x=105, y=260)
        self.erbc=Text(self.master, width=20, height=1, bg="white", font=("Segoe UI Semibold", 12))
        self.erbc.insert(END, self.rbc )
        self.erbc.place(x=250,y=260)
        self.lcholestrol=Label(self.master, text="Cholestrol", font=("Franklin Gothic Medium",12, "bold"), fg="white", bg="#332324").place(x=105, y=300)
        self.echolestrol=Text(self.master, width=20, height=1, bg="white", font=("Segoe UI Semibold", 12))
        self.echolestrol.insert(END, self.cholestrol )
        self.echolestrol.place(x=250,y=300)
        self.lhb=Label(self.master, text="Haemoglobin", font=("Franklin Gothic Medium",12, "bold"), fg="white", bg="#332324").place(x=105, y=340)
        self.ehb=Text(self.master, width=20, height=1, bg="white", font=("Segoe UI Semibold", 12))
        self.ehb.insert(END, self.hb )
        self.ehb.place(x=250,y=340)
        self.lwbc=Label(self.master, text="WBC Count", font=("Franklin Gothic Medium",12, "bold"), fg="white", bg="#332324").place(x=105, y=380)
        self.ewbc=Text(self.master, width=20, height=1, bg="white", font=("Segoe UI Semibold", 12))
        self.ewbc.insert(END, self.wbc )
        self.ewbc.place(x=250,y=380)
        self.back=Button(self.master, text="<- Back",font=("Berlin Sans FB",13), command=self.back, fg="#332324", bg="white").place(x=420, y=425)
        self.save=Button(self.master, text="Save to database",font=("Berlin Sans FB",13),width=15, command=self.db, fg="#332324", bg="white")
        self.save.place(x=222, y=425)
        self.see=Button(self.master, text="Fetch record",font=("Berlin Sans FB",13),width=15, command=self.show, fg="#332324", bg="white")
        self.see.place(x=30, y=425)
        
    def show(self):
        self.ip=self.ename.get("1.0",'end-1c')
        y=x.execute('select * from people where name = "%s" ' % (self.ip))
        count=0
        for i in y:
            count+=1
            self.eage.insert(END, i[1])
            self.ebphigh.insert(END, i[2])
            self.epulse.insert(END, i[3])
            self.erbc.insert(END, i[4])
            self.echolestrol.insert(END, i[5])
            self.ehb.insert(END, i[6])
            self.ewbc.insert(END, i[7])
        if(count==0):
            messagebox.showinfo("Alert", "No matching record found")
        self.see.config(state=DISABLED)
        
        
    def db(self):
        x.execute("create table if not exists people(name text, age text, bp text, pulse text, rbc text, cholestrol text, haemoglobin text, wbc text)")
        x.execute("insert into people values(?,?,?,?,?,?,?,?)", (self.name, self.age, self.bphigh, self.pulse, self.rbc, self.cholestrol, self.hb, self.wbc))
        x.commit()
        self.save.config(text="Saved")
        self.save.config(state=DISABLED)
        

    def back(self):
        self.master.destroy();


class bfc():
        
    def __init__(self, master):
        self.master=master
        self.master.geometry("500x500+500+180")
        self.height=IntVar()
        self.weight=IntVar()
        self.age=IntVar()
        self.gender=StringVar(value="Male")
        self.master.resizable(0,0)
        self.master.title("Body Fat Calculator")
        self.master.configure(background="#332324")
        self.title=Label(self.master, text="Body Fat Calculator",font=("Britannic Bold",22, "bold"), fg="white", bg="#332324" ).place(x=120, y=18)
        self.lheight=Label(self.master, text="Height (in cm)", font=("Franklin Gothic Medium",13,"bold"), fg="white", bg="#332324").place(x=75, y=80)
        self.eheight=Entry(self.master, textvariable=self.height, width=30, bg="white")
        self.eheight.delete(0, 'end')
        self.eheight.focus()
        self.eheight.place(x=210,y=82)
        self.lweight=Label(self.master, text="Weight (in kg)", font=("Franklin Gothic Medium",13, "bold"), fg="white", bg="#332324").place(x=75, y=110)
        self.eweight=Entry(self.master, textvariable=self.weight, width=30, bg="white")
        self.eweight.delete(0, 'end')
        self.eweight.focus()
        self.eweight.place(x=210,y=112)
        self.lage=Label(self.master, text="Age", font=("Franklin Gothic Medium",13, "bold"), fg="white", bg="#332324").place(x=75, y=140)
        self.eage=Entry(self.master, textvariable=self.age, width=30, bg="white")
        self.eage.delete(0, 'end')
        self.eage.focus()
        self.eage.place(x=210,y=142)
        self.gender=Label(self.master, text="Gender", font=("Franklin Gothic Medium",13, "bold"), fg="white", bg="#332324").place(x=75, y=170)
        self.male=Radiobutton(self.master, text="Male", variable=self.gender, value="Male", font=("Franklin Gothic Medium",10, "bold"), fg="black", bg="white")
        self.male.place(x=210, y=170)
        self.female=Radiobutton(self.master, text="Female", variable=self.gender, value="Female", font=("Franklin Gothic Medium",10, "bold"), fg="black", bg="white")
        self.female.place(x=310, y=170)
        self.clear=Button(self.master, text="Reset", command=self.clr,font=("Berlin Sans FB",13), fg="#332324", bg="white", width=10).place(x=300, y=230)
        self.calculate=Button(self.master, text="Calculate",font=("Berlin Sans FB",13), command=self.calculatebfc, fg="#332324", bg="white", width=10).place(x=110,y=230)
        self.result=Text(self.master, state=DISABLED, bg="white",font=("Segoe UI Semibold",13))
        self.result.place(x=50, y=280, width=400, height=120)
        self.back=Button(self.master, text="<- Back",font=("Berlin Sans FB",13), command=self.back, fg="#332324", bg="white").place(x=383, y=435)
            
    def calculatebfc(self):
        rheight=self.height.get()
        rheight=rheight/100
        rheight*=rheight
        rweight=self.weight.get()
        rage=self.age.get()
        bmi=rweight/rheight
        bfc = 1.20 * bmi + 0.23 * rage - 16.2
        self.result.config(state=NORMAL)
        self.result.insert(END, "Your Bodt Fat Percentage is %.2f " % bfc)
        self.result.see("end")
        self.result.config(state=DISABLED)

    def clr(self):
        self.eheight.delete(0, 'end')
        self.eweight.delete(0, 'end')
        self.eage.delete(0, 'end')
        self.result.config(state=NORMAL)
        self.result.delete('1.0', END)
        self.result.config(state=DISABLED)
        
    def back(self):
        self.master.destroy();

class calorie():

   def __init__(self, master):
        self.master=master
        self.master.geometry("500x500+500+180")
        self.master.resizable(0,0)
        self.master.title("Calorie")
        self.master.configure(background="#332324")   
        self.age=IntVar()
        self.gender=IntVar()
        self.height=IntVar()
        self.weight=IntVar()
        self.activity=StringVar()
        self.activity.set("Choose")  
        self.title=Label(self.master, text="Calorie Calculator",font=("Britannic Bold",22, "bold"), fg="white", bg="#332324" ).place(x=135, y=18)
        self.lage=Label(self.master, text="Age(in Years):",font=("Franklin Gothic Medium",13,"bold"),fg="white", bg="#332324").place(x=80,y=80)
        self.eage=Entry(self.master, textvariable=self.age, width=30)
        self.eage.delete(0, 'end')
        self.eage.focus()
        self.eage.place(x=210,y=82)
        self.lbut=Label(self.master, text="Gender:",font=("Franklin Gothic Medium",13,"bold"),fg="white", bg="#332324").place(x=80,y=120)
        self.ebut1=Radiobutton(self.master,text="Male",font=("Franklin Gothic Medium",13,"bold"),bg="white", fg="#332324",value=1,variable=self.gender).place(x=210,y=120)
        self.ebut2=Radiobutton(self.master,text="Female",font=("Franklin Gothic Medium",13,"bold"), bg="white",fg="#332324",value=2,variable=self.gender).place(x=300,y=120)
        self.lheight=Label(self.master, text="Height (in cm):", font=("Franklin Gothic Medium",13,"bold"), fg="white", bg="#332324").place(x=80, y=165)
        self.eheight=Entry(self.master, textvariable=self.height, width=30, bg="white")
        self.eheight.delete(0, 'end')
        self.eheight.focus()
        self.eheight.place(x=210,y=165)
        self.lweight=Label(self.master, text="Weight (in kg):", font=("Franklin Gothic Medium",13, "bold"), fg="white", bg="#332324").place(x=80, y=200)
        self.eweight=Entry(self.master, textvariable=self.weight, width=30, bg="white")
        self.eweight.delete(0, 'end')
        self.eweight.focus()
        self.eweight.place(x=210,y=200)
        self.lactivity=Label(self.master, text="Activity:",font=("Franklin Gothic Medium",13,"bold"),fg="white", bg="#332324").place(x=80,y=240)
        self.eactivity=OptionMenu(self.master,self.activity,"Sedentary-Little Or no exercise","Lightiy Active-exercise/sports 1-3times/week", "Moderately Active-exercise/sports 1-3times/week", "Very Active-exercise/sports 1-3times/week","Extra Active-exercise/sports 1-3times/week")
        self.eactivity.place(x=190,y=235)
        self.calculate=Button(self.master, text="Calculate",font=("Berlin Sans FB",13),bg="white", fg="#332324",command=self.calculatecalo).place(x=70,y=300)
        self.clear=Button(self.master, text="Reset",font=("Berlin Sans FB",13), fg="#332324", bg="white",command=self.clr).place(x=400, y=300)
        self.result=Text(self.master, state=DISABLED,font=("Segoe UI Semibold",13))
        self.result.place(x=50, y=340, width=400, height=120)
        self.back=Button(self.master, text="<- Back",font=("Berlin Sans FB",13),bg="white", fg="#332324",command=self.back).place(x=425, y=465)

   def calculatecalo(self):
       rweight=self.weight.get()
       rheight=self.height.get()
       rage=self.age.get()
       x=self.gender.get()
       if x==1 :
         cal=(10 * rweight) + (6.25 * rheight) -( 5 * rage) + 5
       else:
         cal= (10 * rweight) + (6.25 * rheight) -( 5 * rage) - 161     
       self.result.config(state=NORMAL)
       self.result.insert(END, "    Your Calorie Count is %.2f "% cal)
       self.result.see("end")
       self.result.config(state=DISABLED)

   def clr(self):
        self.eage.delete(0,'end')
        self.activity.set('Choose')
        self.eheight.delete(0, 'end')
        self.eweight.delete(0, 'end')
        self.result.config(state=NORMAL)
        self.result.delete('1.0', END)
        self.result.config(state=DISABLED)

   def back(self):
        self.master.destroy();            

def main():
    root=Tk()
    welcomegui=welcome(root)
    root.mainloop()

if __name__=="__main__":
    main();
