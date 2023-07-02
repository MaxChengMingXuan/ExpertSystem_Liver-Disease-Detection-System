from argparse import OPTIONAL
from tkinter import *
import tkinter
from tkinter import messagebox
from tkinter import font

answer = 2

root = Tk()  # create root window
root.title("Early Detection of Liver Disease")  # title of the GUI window
root.maxsize(1920, 1080)  # specify the max size the window can expand to
root.config(bg="skyblue")  # specify background color

# Create Frame widget
left_frame = Frame(root, width=900, height=700)
left_frame.grid(row=0, column=0, padx=10, pady=5)

right_frame = Frame(root, width=200, height=700)
right_frame.grid(row=0, column=1, padx=10, pady=5)

# # Create frame within left_frame
dialog = Frame(left_frame, width=800, height=400, bg="azure")
dialog.grid(row=2, column=0, padx=5, pady=5)

buttonFrame = Frame(left_frame, width=900, height=200, bg="azure")
buttonFrame.grid(row=3, column=0, padx=5, pady=5, sticky='nsew')

# # Create frame within right_frame
edialog = Frame(right_frame, width=300, height=300, bg="azure")
edialog.grid(row=2, column=0, padx=5, pady=5)

ebuttonFrame = Frame(right_frame, width=400, height=150, bg="azure")
ebuttonFrame.grid(row=3, column=0, padx=5, pady=5, sticky='nsew')

# # Create label above the tool_bar
Label(left_frame, text="Early Detection of Liver Disease System",justify= RIGHT).grid(row=1, column=0, padx=5, pady=12)
Label(right_frame, text="Explaination",justify= RIGHT).grid(row=1, column=0, padx=5, pady=12)

#text widget
mainText = Text(dialog,font=('Roboto',17,'bold'),wrap = WORD)
Fact = "Welcome to Early Detection of Liver Disease System.\n Press Start button to use the system."
mainText.place(relx=0.5,rely=0.5,width=750,height=350,anchor=CENTER)

mainText.insert(END,Fact)
mainText.config(state=DISABLED)

eText = Text(edialog,font=('Arial',12),wrap = WORD)
eFact = "Explaination"
eText.place(relx=0.5,rely=0.5, height=250, width=270,anchor=CENTER)

eText.insert(END,eFact)
eText.config(state=DISABLED)

#Button Font Config
myFont = font.Font(size=20)

#Button Group 1
yesButton = Button(buttonFrame, text="Yes",font=myFont,padx=105, fg="black", bg="#f8f9fa",command = lambda:yes())
yesButton.place(relx=0.33,rely=0.3,anchor=CENTER)
noButton = Button(buttonFrame, text="No",font=myFont,padx=105, fg="black", bg="#f8f9fa",command = lambda:no())
noButton.place(relx=0.66,rely=0.3,anchor=CENTER)
noButton.config(state=DISABLED)
yesButton.config(state=DISABLED)


startButton = Button(buttonFrame, text="Start",font=myFont,padx=60,pady=5, fg="black", bg="#f8f9fa",command = lambda:Start())
startButton.place(relx=0.25,rely=0.7,anchor=CENTER)
resetButton = Button(buttonFrame, text="Reset",font=myFont,padx=60,pady=5, fg="black", bg="#f8f9fa",command = lambda:reStart())
resetButton.place(relx=0.5,rely=0.7,anchor=CENTER)
resetButton.config(state=DISABLED)

exitButton = Button(buttonFrame, text="Exit",font=myFont,padx=60,pady=5, fg="black", bg="#f8f9fa",command = lambda:exit())
exitButton.place(relx=0.75,rely=0.7,anchor=CENTER)

#Button Group 2
whyButton = Button(ebuttonFrame, text="Why?",font=myFont,padx=20,pady=5, fg="black", bg="#f8f9fa",command = lambda:why())
whyButton.place(relx=0.3,rely=0.5,anchor=CENTER)
howButton = Button(ebuttonFrame, text="How?",font=myFont,padx=20,pady=5, fg="black", bg="#f8f9fa",command = lambda:how())
howButton.place(relx=0.7,rely=0.5,anchor=CENTER)

whyButton.config(state=DISABLED)
howButton.config(state=DISABLED)

def toggle_buttons(button, state):
        button.config(state=state)

#Function Group
med= False
maj= False
min= False
famHis= False
chemical= False 
aflatoxin= False 
cirrhosis= False
alcoholic= False
oldAge= False
male= False
paleStool= False 
jaundice= False 
abPain= False 
darkUrine= False
fatigue= False 
vomit= False
rash= False
fever= False 
weightLoss= False
malaise= False 
anorexia= False 
itch= False
answer = 2
num = 0
print(num)

def Start():
    toggle_buttons(startButton, DISABLED)
    toggle_buttons(resetButton, NORMAL)

    global answer
    global num
    print("starting...")
    mainText.config(state=NORMAL)
    mainText.delete('1.0', END)
    num=0
    answer=2
    rule()
    mainText.config(state=DISABLED)
    toggle_buttons(howButton, DISABLED)
    toggle_buttons(whyButton, NORMAL)
    toggle_buttons(yesButton, NORMAL)
    toggle_buttons(noButton, NORMAL)

def reStart():
    toggle_buttons(startButton, NORMAL)
    toggle_buttons(resetButton, DISABLED)
    mainText.config(state=NORMAL)
    mainText.delete('1.0', END)
    mainText.insert(END, "Welcome to Early Detection of Liver Disease System.\n Press Start button to use the system.")
    mainText.config(state=DISABLED)

    eText.config(state=NORMAL)
    eText.delete('1.0', END)
    eText.insert(END, " ")
    eText.config(state=DISABLED)
    toggle_buttons(howButton, DISABLED)
    toggle_buttons(whyButton, DISABLED)

def dis(text):
    print("displaying")
    mainText.config(state=NORMAL)
    mainText.delete('1.0', END)
    mainText.insert(END, text)
    mainText.config(state=DISABLED)

def hwdis(text):
    print("displaying")
    eText.config(state=NORMAL)
    eText.delete('1.0', END)
    eText.insert(END, text)
    eText.config(state=DISABLED)

def how():
    print("how")
    hwdis(h)

def why():
    print("why")
    hwdis(w)

def yes():
    print("yes")
    global answer
    answer=1
    rule()

def no():
    print("no")
    global answer
    answer=0
    rule()

def exit():
    if messagebox.askyesno("Exit", "Do you wish to exit the system?"):
        root.destroy()

    

def rule():
    print("In rule")
    global answer
    global num
    global famHis, chemical, aflatoxin, cirrhosis, alcoholic, oldAge, male 
    global paleStool, jaundice, abPain, darkUrine
    global fatigue, vomit, rash, fever, weightLoss, malaise, anorexia, itch
    global w
    if num == 0:
        d="Does your family member have a previous history of liver disease?"
        w="The system is trying to prove medical history of liver disease if your family members have the history of liver disease."
        
        dis(d)
        if answer==0:
            famHis=False
            num=num+1
            answer=2
            rule()
        elif answer==1:
            famHis=True
            num=7
            answer=2
            rule()
    if num==1:
        
        d="Have you been exposed to certain chemicals or toxins?"
        w="Since you answered no to previous question, the system has recorded " +str(famHis)+" in family history. Now, the system is trying to prove if you exposed to chemicals (breathe in or consumed)"
        
        dis(d)
        if answer==0:
            chemical=False
            num=num+1
            answer=2
            rule()
        elif answer==1:
            chemical=True
            num=7
            answer=2
            rule()
    if num==2:
        d="Have you consumed any moldy food? (example:moldy peasnuts, moldy corns, moldy nuts, contaminated milk or cheese)"
        w="Since you answered no to previous question, the system has recorded " +str(chemical)+" in explosure to chemical. Now, the system is trying to prove if you consumed any moldy food that might contain aflatoxin."
        dis(d)
        if answer==0:
            aflatoxin=False
            num=num+1
            answer=2
            rule()
        elif answer==1:
            aflatoxin=True
            num=7
            answer=2
            rule()
    if num==3:
        d="Do you have a previous history of cirrhosis (hardening of the liver)?"
        w="Since you answered no to previous question, the system has recorded " +str(aflatoxin)+" in consume moldy food. Now, the system is trying to prove if you exposed to chemicals (breathe in or consumed)"
        dis(d)
        if answer==0:
            cirrhosis=False
            num=num+1
            answer=2
            rule()
        elif answer==1:
            cirrhosis=True
            num=7
            answer=2
            rule()

    if num==4:
        d="Are you a heavy alcohol drinker? (Drinking 15 or more drinks per week)"
        w="Since you answered no to previous question, the system has recorded " +str(cirrhosis)+" in history of cirrhosis. Now, the system is trying to prove if you drink alcohol heavily."
        dis(d)
        if answer==0:
            alcoholic=False
            num=num+1
            answer=2
            rule()
        elif answer==1:
            alcoholic=True
            num=7
            answer=2
            rule()
    if num==5:
        d="Are you over the age of 60?"
        w="Since you answered no to previous question, the system has recorded " +str(alcoholic)+" in alcoholic. Now, the system is trying to prove if you are older than 60 years old"
        dis(d)
        if answer==0:
            oldAge=False
            num=num+1
            answer=2
            rule()
        elif answer==1:
            oldAge=True
            num=7
            answer=2
            rule()
    if num==6:
        d="Is your gender male?"
        w="Since you answered no to previous question, the system has recorded " +str(oldAge)+" in older than 60 years old. Now, the system is trying to prove if your gender is male."
        dis(d)
        if answer==0:
            male=False
            num=num+1
            answer=2
            rule()
        elif answer==1:
            male=True
            num=7
            answer=2
            rule()
    if num==7:
        d="Does your stool look pale/white/grey in colour?"
        w="The system is trying to prove the major symptom of liver disease if your stool looks pale in colour."
        dis(d)
        if answer==0:
            paleStool=False
            num=num+1
            answer=2
            rule()
        elif answer==1:
            paleStool=True
            result() 
            

            
    if num==8:
        d="Do the whites of your eyes/ the inside of your mouth look yellow?(Jaundice)"
        w="Since you answered no to previous question, the system has recorded " +str(paleStool)+" in pale stool symptom. Now, the system is trying to prove if you have the symptom of jaundice."
        dis(d)
        if answer==0:
            jaundice=False
            num=num+1
            answer=2
            rule()
        elif answer==1:
            jaundice=True
            result() 
    if num==9:
        d="Do you experience abdominal/stomach pain?"
        w="Since you answered no to previous question, the system has recorded " +str(jaundice)+" in jaundice symptom. Now, the system is trying to prove if you have the symptom of abdominal pain."
        dis(d)
        if answer==0:
            abPain=False
            num=num+1
            answer=2
            rule()
        elif answer==1:
            abPain=True
            result() 
    if num==10:
        d="Do your urine is in dark brown colour?"
        w="Since you answered no to previous question, the system has recorded " +str(abPain)+" in abdominal pain symptom. Now, the system is trying to prove if you have the symptom of dark urine."
        dis(d)
        if answer==0:
            darkUrine=False
            num=num+1
            answer=2
            rule()
        elif answer==1:
            darkUrine=True
            result() 
    if num==11:
        d="Do you feel fatigue? (extremely tired)"
        w="The system is trying to prove the minor symptom of liver disease if you have the feeling of fatigue."
        
        dis(d)
        if answer==0:
            fatigue=False
            num=num+1
            answer=2
            rule()
            
        elif answer==1:
            fatigue=True
            answer=2
            result()
    if num==12:
        d="Have you been vomiting?"
        w="Since you answered no to previous question, the system has recorded " +str(fatigue)+" in fatigue symptom. Now, the system is trying to prove if you have the symptom of vomitting."
        dis(d)
        if answer==0:
            vomit=False
            num=num+1
            answer=2
            rule()
        elif answer==1:
            vomit=True
            answer=2
            result()
    if num==13:
        d="Do you have rash on any part of your body?"
        w="Since you answered no to previous question, the system has recorded " +str(vomit)+" in vomit symptom. Now, the system is trying to prove if you have the symptom of rash."
        dis(d)
        if answer==0:
            rash=False
            num=num+1
            answer=2
            rule()
        elif answer==1:
            rash=True
            answer=2
            result()
    if num==14:
        d="Do you have fever?"
        w="Since you answered no to previous question, the system has recorded " +str(rash)+" in rash symptom. Now, the system is trying to prove if you have the symptom of fever."
        dis(d)
        if answer==0:
            fever=False
            num=num+1
            answer=2
            rule()
            
        elif answer==1:
            fever=True
            answer=2
            result()
    if num==15:
        d="Do you experience sudden weight loss recently?"
        w="Since you answered no to previous question, the system has recorded " +str(fever)+" in fever symptom. Now, the system is trying to prove if you have the symptom of weight loss."
        dis(d)
        if answer==0:
            weightLoss=False
            num=num+1
            answer=2
            rule()
            
        elif answer==1:
            weightLoss=True
            answer=2
            result()
    if num==16:
        d="Do you have an overall feeling of discomfort? (malaise)"
        w="Since you answered no to previous question, the system has recorded " +str(weightLoss)+" in weight loss symptom. Now, the system is trying to prove if you have the symptom of malaise."
        dis(d)
        if answer==0:
            malaise=False
            num=num+1
            answer=2
            rule()
            
        elif answer==1:
            malaise=True
            answer=2
            result()
    if num==17:
        d="Do you have trouble eating normally? (eating disorder)"
        w="Since you answered no to previous question, the system has recorded " +str(malaise)+" in malaise symptom. Now, the system is trying to prove if you have the symptom of eating disorder."
        dis(d)
        if answer==0:
            anorexia=False
            num=num+1
            answer=2
            rule()
            
        elif answer==1:
            anorexia=True
            answer=2
            result()
    if num==18:
        d="Do you experience itching in any part of your body?"
        w="Since you answered no to previous question, the system has recorded " +str(anorexia)+" in abdominal pain symptom. Now, the system is trying to prove if you have the symptom of eating disorder."
        dis(d)
        if answer==0:
            itch=False
            num=num+1
            answer=2
            result()
        elif answer==1:
            itch=True
            answer=2
            result()
        
def result():
    toggle_buttons(howButton, NORMAL)
    toggle_buttons(yesButton, DISABLED)
    toggle_buttons(noButton, DISABLED)
    toggle_buttons(whyButton, DISABLED)

    global h
    if famHis== True or chemical==True or aflatoxin== True or cirrhosis== True or alcoholic== True or oldAge==True or male == True:
        med =True
    elif famHis== False or chemical==False or aflatoxin== False or cirrhosis== False or alcoholic== False or oldAge==False or male == False:
        med =False
    if paleStool== True or jaundice ==True or abPain == True or darkUrine == True:
        maj = True
    elif paleStool== False or jaundice ==False or abPain == False or darkUrine == False:
        maj = False
    if fatigue== True or vomit ==True or rash == True or fever == True or weightLoss == True or malaise ==True or anorexia ==True or itch ==True:
        min = True
    elif fatigue== False or vomit ==False or rash == False or fever == False or weightLoss == False or malaise ==False or anorexia ==False or itch ==False:
        min = False
        
    if maj==True and med==True:
        d='Very high risk of suspected liver disease infection'
        h='The system has detected:\nThe result of medical history of liver disease is '+str(med)+"\n\nThe major symptom of liver disease is "+ str(maj)+"\n\nWe extremely recommend you to consult with your doctor as soon as posible."
        dis(d)
        print('very high Risk')

    elif maj==True and med==False:
        d='High risk of suspected liver disease infection'
        h='The system has detected:\nThe result of medical history of liver disease is '+str(med)+"\n\nThe major symptom of liver disease is "+ str(maj)+"\n\nWe highly recommend you to consult with your doctor for further investigation."
        dis(d)
        print('high risk')

    elif min==True and med==True:
        d='Medium risk of suspected liver disease infection'
        h='The system has detected:\nThe result of medical history of liver disease is '+str(med)+"\n\nThe major symptom of liver disease is "+ str(maj)+"\n\nThe minor symptom of liver disease is "+ str(min)+"\n\nWe recommend you to consult with your doctor for further investigation."
        dis(d)
        print('medium risk')

    elif min==True and med==False:
        d='Low risk of suspected liver disease infection'
        h='The system has detected:\nThe result of medical history of liver disease is '+str(med)+"\n\nThe major symptom of liver disease is "+ str(maj)+"\n\nThe minor symptom of liver disease is "+ str(min)+"\n\nAlthough the result is low risk We still encourage you to make appointment with your doctor for further investigation."
        dis(d)
        print('low risk')

    elif min==False and med==True:
        d='Low risk of suspected liver disease infection'
        h='The system has detected:\nThe result of medical history of liver disease is '+str(med)+"\n\nThe major symptom of liver disease is "+ str(maj)+"\n\nThe minor symptom of liver disease is "+ str(min)+"\n\nAlthough the result is low risk We still encourage you to make appointment with your doctor for further investigation."
        dis(d)
        print('low risk')

    elif maj==False and min==False and med==False:
        d='Very low risk of suspected liver disease infection'
        h='The system has detected:\nThe result of medical history of liver disease is '+str(med)+"\n\nThe major symptom of liver disease is "+ str(maj)+"\n\nThe minor symptom of liver disease is "+ str(min)+"\n\nYou have almost none symptoms of the liver disease, but you are still encourage to perform regular medical checkups to keep aware of your health."
        dis(d)
        print('very low risk')

mainloop()