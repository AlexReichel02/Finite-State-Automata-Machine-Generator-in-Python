  
import sys
import tkinter as tk

class FSA:
    def __init__(self):
        self.states =[]
        self.alphabet = []
        self.startState = ""
        self.acceptStates = []
        self.transition = {}

    def parseString(self,inputString):
        allWords = contents.split(';')
        print("\n")
        numStates = int(allWords[0])
        print("Number of states: ", numStates)
        print("\n")
        alph = allWords[1]
        print("Alphabet: " ,alph)
        print("\n")
        stateTransitions = allWords[2]
        print("State transitions: " ,stateTransitions)
        print("\n")
        start=allWords[3]
        print("Start State: ",start)
        print("\n")
        acceptState = allWords[4]
        print("AcceptState: ",acceptState)
        print("\n")

        alphabet = []
        startState = ""
        acceptStates = []
        transition = {}
        states = []

        for i in range(numStates):
            states.append(i)

        print("States: ",states)
        self.states = states

       
        alphabet = alph.split(',')
        self.alphabet = alphabet
       

        startState=start
        
        self.startState = startState

        acceptStates = acceptState.split(',')
        
        self.acceptStates = acceptStates
    
    

        transitions = stateTransitions.split(',')
        size = len(transitions)
        for j in range(size):
                 parsedTran= ''.join(filter(str.isalnum,transitions[j]))
                 
                 transition[(parsedTran[0],parsedTran[2])] = parsedTran[1]
                 
        self.transition = transition
        print(self.transition)
        
    

        
    def display(self):
        print(self.alphabet)
        print(self.startState) 
        print(self.acceptStates)
        print(self.transition)

    def drawCircle(self,canvas,x1,y1,x2,y2):
        cir1 = canvas.create_oval(x1,y1,x2,y2)
        cir2 = canvas.create_oval(x1+1,y1+1,x2-1,y2-1, fill="white")
        canvas.pack()

    def drawAcceptCirc(self,canvas,x1,y1,x2,y2):
        cir1 = canvas.create_oval(x1,y1,x2,y2)
        
        cir2 = canvas.create_oval(x1+4,y1+4,x2-4,y2-4, fill="green")
        canvas.pack()

    def drawFSA(self):

        
        root = tk.Tk()
        canvas = tk.Canvas(root, width=600, height=1000, borderwidth=0, highlightthickness=0, bg="white")
        canvas.grid()

        x1 = 80
        y1 = 50
        dia = 40
        y2 = 70
        y3=70
       
        for state in self.states:
            
            inc =0
            if str(state) in self.acceptStates:
                y6=0
                self.drawAcceptCirc(canvas,x1,y1,x1+dia,y1+dia)
                for tran in self.transition:
                    
                    curr = self.transition[(tran[0], tran[1])]

                    if curr is None:
                        print("Non existent State")
                    else:
                    
                        otherDiff = int(tran[0])-int(curr)
                        diff = int(curr) - int(tran[0])
              

                        if curr == tran[0] and curr == str(state):
                        
                            print("Going to same state",curr, " = " , tran[0])
                        
                            canvas.create_line(115, y1+inc+5, 170, y1+inc+15,120,y1+inc+25, width = 2, smooth=True, arrow=tk.LAST)
                            canvas.create_text(150, y1+20, text=str(tran[1]))
                            inc += 150

                        
                        if (diff == 1):
                        
                            print("Going to Different State",curr, " = " , tran[0])
                            canvas.create_line(100, 90+y6, 100, 200+y6, width = 2, arrow=tk.LAST)
                            canvas.create_text(110, 145+y6, text=str(tran[1]))
                            y6 += 150


                        if(otherDiff > 1):
                            canvas.create_line(80, (70+y6), 80, (140+y6) / otherDiff, width = 2, arrow=tk.LAST)
                            canvas.create_text(65, y6+10, text=str(tran[1]))
                          

                                                        
            else:
                
                y5 =0
                self.drawCircle(canvas,x1,y1,x1+dia,y1+dia)
               
                for tran in self.transition:
                    
                    curr = self.transition[(tran[0], tran[1])]

                    if curr is None:
                        print("Non valid state")
                    else:
                    
                        otherDiff = int(tran[0])-int(curr)
                        diff = int(curr) - int(tran[0])
              

                        if curr == tran[0] and curr == str(state):
                        
                            print("Going to same state",curr, " = " , tran[0])
                        
                            canvas.create_line(115, y1+inc+5, 170, y1+inc+15,120,y1+inc+25, width = 2, smooth=True, arrow=tk.LAST)
                            canvas.create_text(150, y1+20, text=str(tran[1]))
                            inc += 150

                        
                        if (diff == 1):
                        
                            print("Going to Different State",curr, " = " , tran[0])
                            canvas.create_line(100, 90+y5, 100, 200+y5, width = 2, arrow=tk.LAST)
                            canvas.create_text(110, 145+y5, text=str(tran[1]))
                            y5 += 150   


                        if(otherDiff > 1):
                            canvas.create_line(80, (70+y5), 80, (140+y5) / otherDiff, width = 2, arrow=tk.LAST)
                            canvas.create_text(65, y5+10, text=str(tran[1]))


                        if(diff > 1):
                            canvas.create_line(120, y5-70, 130, (y5*diff) / 1.35, width = 2, arrow=tk.LAST)
                            canvas.create_text(130, y5+10, text=str(tran[1]))
                            
                             
            
                
            canvas.create_text(x1+20, y2, text=str(state))
            y1 += 150
            y2 += 150
            



        root.wm_title("FSA Drawing Representation")
        root.mainloop()

        

    def fillDict(self):
        for state in self.states:
            for alp in self.alphabet:

                try:
                    curr = self.transition[(str(state), alp)]

                
                except KeyError as ke:
                    self.transition[(str(state), alp)] = None

        print(self.transition)



    def testString(self,inputString):
         stringSize = len(inputString)
        
         self.fillDict()
         current_state = self.startState
        
         i = 0
         for char in inputString:
            i +=1
            if char not in self.alphabet:
                 print("Rejected incorrect alphabet used")
                 break;

            
            current_state = self.transition[(current_state, char)]

            print("\n")
            print("char is currently: ",char)
            
            print("char destination is state: ",current_state)
            

      
            if current_state is None :
                print("Reject")
                break
            
            else:
                
                if (current_state in self.acceptStates):
                    print("char is in Accept state")
                    if(i == stringSize):
                             print("\n")
                             print("Full String Accepted")
                
                else:
                    print("char is not in Accept state")
                    if(i == stringSize):
                            print("\n")
                            print("Full String Rejected")
        

n = len(sys.argv)
print("\nName of Python script:", sys.argv[0])
 
print("\nArguments passed:", end = " ")
for i in range(1, n):
    print(sys.argv[i], end = " ")
     

print("\n")

with open(sys.argv[0]) as f:
    contents = f.read()
    print(contents)
   
   
with open('fsa.txt') as f:
    contents = f.read()
    print(contents)



    Legalstring = "xxxxyxxxyxxzxxxa" 
    illegalString = "xxxxxyxxxygxzxx"

    fsa = FSA()
    fsa.parseString(contents)
    fsa.testString(Legalstring)
    fsa.testString(illegalString)
    fsa.drawFSA()


    
    



   
    
            
                        

    
    

    

    
