# Libraries Importations
import customtkinter as ctk
import tkinter as tk
from customtkinter import *
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image,ImageTk
from ttkthemes import ThemedStyle
import pickle
import numpy as np


# Appearance setter
ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("dark-blue")   
appWidth,appHeight=1066,668


# Main Application
class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("GUI Application") 
        self.geometry(f"{appWidth}x{appHeight}+200+0") 
        self.protocol('WM_DELETE_WINDOW',self.close_app)        
        self.style=ThemedStyle()
        self.style.theme_use('breeze')
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.st=ttk.Style()
        self.title("PORTABILITY DETECTOR") 
        self.width=self.winfo_screenwidth()
        self.height=self.winfo_screenheight()  
        self.photo=Image.open('images/logo_w3.png')
        self.photo=self.photo.resize((230,200))
        self.photo=ImageTk.PhotoImage(self.photo)
        self.iconphoto(False,self.photo)



        with open('model.pkl', 'rb') as file:
            self.model = pickle.load(file)
        
            
        
        self.tk_img=Image.open('images/bga.png')
        self.tk_img=self.tk_img.resize((self.width+50,self.height))
        self.tk_img=ImageTk.PhotoImage(self.tk_img)

        self.main_app=Canvas(self,borderwidth=0)
        self.main_app.create_image(0, 0, image=self.tk_img, anchor="nw")
        self.main_app.pack(side=LEFT,expand=True,fill=BOTH)


        self.f1=CTkFrame(self.main_app,fg_color='black',height=50,corner_radius=0,border_width=0)
        self.f1.pack(fill=X)
        

        self.clear_btn=CTkButton(self.f1,text='CLEAR ENTRIES',fg_color='orange',text_color='white',text_font='Tahoma 12 bold',command=self.clear_app)
        self.clear_btn.place(relx=0.2,rely=0.2)

        self.cls_btn=CTkButton(self.f1,text='CLOSE APP',fg_color='red',text_color='white',text_font='Tahoma 12 bold', command=self.close_app)
        self.cls_btn.place(relx=0.6,rely=0.2)

        self.main_app.create_image(15, 50, image=self.photo, anchor="nw")

        self.f2=CTkFrame(self.main_app,fg_color='white',height=500,corner_radius=5,width=500,relief=RAISED)
        self.f2.pack(pady=80,ipady=10,ipadx=28)

        # PH Label
        self.ph = ctk.CTkLabel(self.f2,text="PH Value",fg_color='white',text_font=('Tahoma','14','bold'),text_color='black')
        self.ph.pack(anchor=W,pady=5)
        # PH Entry Field
        self.ph_entry = ctk.CTkEntry(self.f2,placeholder_text="Enter PH Value",width=350,corner_radius=4,border_width=1.2,text_font=('Tahoma','12'))
        self.ph_entry.pack(pady=5)
        self.ph_entry.bind('<Leave>',self.leave_ph)
        # PH Label
        self.hardness = ctk.CTkLabel(self.f2,text="Hardness Value",fg_color='white',text_font=('Tahoma','14','bold'),text_color='black')
        self.hardness.pack(anchor=W,pady=5,padx=20)
        # Hardness Entry Field
        self.hardness_entry = ctk.CTkEntry(self.f2,placeholder_text="Enter Hardness",width=350,corner_radius=4,border_width=1.2,text_font=('Tahoma','12'))
        self.hardness_entry.pack(pady=5)
        self.hardness_entry.bind('<Leave>',self.leave_hardness)

        # Conductivity Label
        self.conductivity = ctk.CTkLabel(self.f2,text="Conductivity Value",fg_color='white',text_font=('Tahoma','14','bold'),text_color='black')
        self.conductivity.pack(anchor=W,pady=5,padx=20)
        # Conductivity Entry Field
        self.conductivity_entry = ctk.CTkEntry(self.f2,placeholder_text="Enter Conductivity Value",width=350,corner_radius=4,border_width=1.2,text_font=('Tahoma','12'))
        self.conductivity_entry.pack(pady=5)
        self.conductivity_entry.bind('<Leave>',self.leave_conductivity)
        # Turbidity Label
        self.turbidity = ctk.CTkLabel(self.f2,text="Turbidity Value",fg_color='white',text_font=('Tahoma','14','bold'),text_color='black')
        self.turbidity.pack(anchor=W,pady=5,padx=20)
        # Turbidity Entry Field
        self.turbidity_entry = ctk.CTkEntry(self.f2,placeholder_text="Enter Turbidity",width=350,corner_radius=4,border_width=1.2,text_font=('Tahoma','12'))
        self.turbidity_entry.pack(pady=5)
        self.turbidity_entry.bind('<Leave>',self.leave_turbidity)

        # coliform Label
        self.coliform = ctk.CTkLabel(self.f2,text="Total Coliform",fg_color='white',text_font=('Tahoma','14','bold'),text_color='black')
        self.coliform.pack(anchor=W,pady=5,padx=20)
        # coliform Entry Field
        self.tc_entry = ctk.CTkEntry(self.f2,placeholder_text="Enter Total Coliform",width=350,corner_radius=4,border_width=1.2,text_font=('Tahoma','12'))
        self.tc_entry.pack(pady=5)
        self.tc_entry.bind('<Leave>',self.leave_coliform)

 
        self.btn=CTkButton(self.f2,fg_color='#3E4095',hover_color='orange',text_color='white',text_font=('Tahoma','12','bold'),cursor='hand2', text='CHECK WATER',corner_radius=0,command=self.predict)
        self.btn.pack(fill=X,pady=10,ipadx=10,ipady=5,padx=20)

    



    # Functions used in App    
    def close_app(self):
        rsp=messagebox.askyesno('CLOSE APPLICATION','Do you want to exit App?')
        if rsp>0:
            self.destroy()
        else:
            pass
    def leave_ph(self,event):
        self.ph_entry.focus()
    def leave_hardness(self,event):
        self.hardness_entry.focus()
    def leave_conductivity(self,event):
        self.conductivity_entry.focus()
    def leave_turbidity(self,event):
        self.turbidity_entry.focus()
    def leave_coliform(self,event):
        self.tc_entry.focus()

    def predict(self):
        try:
            self.ph_data=self.ph_entry.get()
            self.hardness_data=self.hardness_entry.get()
            self.conductivity_data=self.conductivity_entry.get()
            self.turbidity_data=self.turbidity_entry.get()
            self.tc_data=self.tc_entry.get()

            if self.ph_data=='' or self.hardness_data=='' or self.conductivity_data=='' or self.turbidity_data=='' or self.tc_data=='':
                messagebox.showerror('Please provide all inputs','All values are required')
                
            else:
                self.values=[float(self.ph_data),float(self.hardness_data),float(self.conductivity_data),float(self.turbidity_data),float(self.tc_data)]
                self.prediction = list(self.model.predict(np.array([self.values])))
                
                self.m_pred()
                self.d_ph.config(text=str(self.ph_data))
                self.d_hardness.config(text=str(self.hardness_data))
                self.d_conductivity.config(text=str(self.conductivity_data))
                self.d_turbidity.config(text=str(self.turbidity_data))
                self.d_tc.config(text=str(self.tc_data))
                self.result=int(self.prediction[0])
                
                self.f_h=[]
                if self.result==1:
                    if (float(self.ph_data)>=6.5 and float(self.ph_data)<=8.5) and (float(self.hardness_data)>=0.0 and float(self.hardness_data)<=150.0) and (float(self.conductivity_data)>=0.0 and float(self.conductivity_data)<=1000) and (float(self.turbidity_data)>=0.0 and float(self.turbidity_data)<=5) and (float(self.tc_data)==0.0):
                        self.d_status.config(text='Portable (All criterias are within limit)')
                        self.f_h.append('None')
                        self.d_vio.config(text=str(self.f_h))
                    else:
                        if not(float(self.ph_data)>=6.5 and float(self.ph_data)<=8.5):
                            self.f_h.append('PH')
                        if not (float(self.hardness_data)>=0.0 and float(self.hardness_data)<=150.0):
                            self.f_h.append('Total Hardness')
                        if not (float(self.conductivity_data)>=0.0 and float(self.conductivity_data)<=1000):
                            self.f_h.append('Conductivity')
                        if not (float(self.turbidity_data)>=0.0 and float(self.turbidity_data)<=5):
                            self.f_h.append('Turbidity')
                        if not(float(self.tc_data)==0.0):
                            self.f_h.append('Total Coliform')
                        self.d_status.config(text='Not Portable (Some criterias are outside limits)')
                        self.d_vio.config(text=str(self.f_h))


                            
                    
                else:
                    if not(float(self.ph_data)>=6.5 and float(self.ph_data)<=8.5):
                        self.f_h.append('PH')
                    if not (float(self.hardness_data)>=0.0 and float(self.hardness_data)<=150.0):
                        self.f_h.append('Total Hardness')
                    if not (float(self.conductivity_data)>=0.0 and float(self.conductivity_data)<=1000):
                        self.f_h.append('Conductivity')
                    if not (float(self.turbidity_data)>=0.0 and float(self.turbidity_data)<=5):
                        self.f_h.append('Turbidity')
                    if not(float(self.tc_data)==0.0):
                        self.f_h.append('Total Coliform')
                    self.d_status.config(text='Not Portable (Some criterias are outside limits)')
                    self.d_vio.config(text=str(self.f_h))
                    
        except Exception as e:
            messagebox.showerror('Error from input','Check your Input data')



    
    def m_pred(self):
        self.d_menu=CTkFrame(self,fg_color='white',corner_radius=0,border_width=1.3,border_color='orange')
        self.d_menu.place(relx=0.18,rely=0.2,height=430,width=770)
        self.display=CTkLabel(self.d_menu,fg_color='white',text='RESULT DISPLAY',text_color='black',text_font='Tahoma 16 bold')
        self.display.pack(fill=X,padx=10,pady=20)
        self.close_btn=CTkButton(self.d_menu,fg_color='#3E4095',hover_color='blue',text_color='white',text_font=('Tahoma','12','bold'),cursor='hand2', text='CLOSE PREDICTION',corner_radius=0,command=self.destroy_prediction)

        self.m1=Frame(self.d_menu,bg='white')
        self.m1.pack()
        self.d1=CTkLabel(self.m1,fg_color='white',text='PH:',text_color='black',text_font='Tahoma 12')
        self.d1.grid(row=0,column=0,padx=10,pady=4,sticky=NW)
        self.d_ph=CTkLabel(self.m1,fg_color='white',text='',text_color='black',text_font='Tahoma 12')
        self.d_ph.grid(row=0,column=1,padx=0,pady=4,sticky=NW)

        self.d2=CTkLabel(self.m1,fg_color='white',text='HARDNESS:',text_color='black',text_font='Tahoma 12')
        self.d2.grid(row=1,column=0,padx=10,pady=4,sticky=NW)
        self.d_hardness=CTkLabel(self.m1,fg_color='white',text='',text_color='black',text_font='Tahoma 12')
        self.d_hardness.grid(row=1,column=1,padx=0,pady=4,sticky=NW)

        self.d3=CTkLabel(self.m1,fg_color='white',text='CONDUCTIVITY:',text_color='black',text_font='Tahoma 12')
        self.d3.grid(row=2,column=0,padx=10,pady=4,sticky=NW)
        self.d_conductivity=CTkLabel(self.m1,fg_color='white',text='',text_color='black',text_font='Tahoma 12')
        self.d_conductivity.grid(row=2,column=1,padx=0,pady=4,sticky=NW)

        self.d4=CTkLabel(self.m1,fg_color='white',text='TURBIDITY:',text_color='black',text_font='Tahoma 12')
        self.d4.grid(row=3,column=0,padx=10,pady=4,sticky=NW)
        self.d_turbidity=CTkLabel(self.m1,fg_color='white',text='',text_color='black',text_font='Tahoma 12')
        self.d_turbidity.grid(row=3,column=1,padx=0,pady=4,sticky=NW)

        self.d5=CTkLabel(self.m1,fg_color='white',text='TOTAL COLIFORM:',text_color='black',text_font='Tahoma 12')
        self.d5.grid(row=4,column=0,padx=10,pady=4,sticky=NW)
        self.d_tc=CTkLabel(self.m1,fg_color='white',text='',text_color='black',text_font='Tahoma 12')
        self.d_tc.grid(row=4,column=1,padx=0,pady=4,sticky=NW)

        self.d6=CTkLabel(self.m1,fg_color='white',text='WATER STATUS:',text_color='black',text_font='Tahoma 12')
        self.d6.grid(row=5,column=0,padx=10,pady=4,sticky=NW)
        self.d_status=CTkLabel(self.m1,fg_color='white',text='',text_color='black',text_font='Tahoma 11 bold')
        self.d_status.grid(row=5,column=1,padx=0,pady=4,sticky=NW)
        
        self.d7=CTkLabel(self.m1,fg_color='white',text='CRITERIAS OUTSIDE LIMITS:',text_color='black',text_font='Tahoma 12')
        self.d7.grid(row=6,column=0,padx=10,pady=4,sticky=NW)
        self.d_vio=CTkLabel(self.m1,fg_color='white',text='',text_color='black',text_font='Tahoma 9 bold')
        self.d_vio.grid(row=6,column=1,padx=0,pady=4,sticky=NW)
        


        self.close_btn.pack(ipadx=10,ipady=5,pady=10)

    def destroy_prediction(self):
        self.d_menu.destroy()
        

    def clear_app(self):
        self.ph_entry.delete('0', 'end') 
        self.hardness_entry.delete('0', 'end') 
        self.conductivity_entry.delete('0', 'end') 
        self.turbidity_entry.delete('0', 'end') 
        self.tc_entry.delete('0', 'end') 
        

    

 
if __name__ == "__main__":
    app = App()
    app.mainloop() 

