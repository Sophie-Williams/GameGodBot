import os
import sys
from PIL import Image

class Clue:
    name=None
    cost=0
    DAV=False
    cluecounter=0
    clues=[]
    def __init__(self,name,cost,DAV,path):
        self.name=name
        self.cost=cost
        self.DAV=DAV
        self.getclues(path)
    def getclues(self, path):
        self.clues=[]
        filenames=os.listdir(path)
        #print (filenames)
        for filename in filenames:
            self.clues.append(''.join([path,'\\',filename]))
        #print(self.clues)
        
    def removeclue(self,path):
        if path in self.clues:
            self.cluecounter=self.clues.index(path)
            self.clues.remove(path)
            if self.cluecounter>=len(self.clues):
                self.cluecounter = 0
    
    def viewclue(self,DAV):
        if self.clues==[]:
            return None
        elif DAV == True:
            returnpath=self.clues[0]
            self.clues.remove(returnpath)

            return returnpath
        else:
            tempcounter=self.cluecounter
            if self.cluecounter+1==len(self.clues):
                self.cluecounter=0
            else:
                self.cluecounter += 1
            return self.clues[tempcounter]
            

class Player:
    name=None
    pw=None
    dp=0
    
    def __init__(self,name,pw,dp):
        self.name=name
        self.pw=pw
        self.setdp(dp)
        
    def setdp(self,dp):
        self.dp=dp
    
    def setpw(self,pw):
        self.pw=pw
    
#Setting variables
ROES=True #return on empty search
TAV=True #Take after view
DAV=False #Delete after view

locations=os.listdir()
locations=locations[2:]
cluelist=[]
cost=1
cwd=os.getcwd()
for location in locations:
#    while True:
#        cost=input("How many dp points should exploring "+location+" cost?" )
#        if cost.isdigit():
#                break
#        else:
#            print("please enter a valid integer.\n")
                
    path=''.join([cwd,'\\',location])
    #print (path)
    clue=Clue(location,cost,DAV,path)
    #clue.getclues(path)
    cluelist.append(clue)


def clear():
    print ('\n' * 100)

#Set up characters
while True:
    try:
        dp=int(input("How many DP should each player have? :"))
        break
    except:
        print("please enter an integer.")

clear()
players=[]
setupPlayers=True
while setupPlayers:
    
    name=input("Hi There! What is your character name? :")
    
    while True:
        pw = input("please set a simple password for your character (less than 4 digits number) :")
        if pw.isdigit() and len(pw)<=4 and len(pw)>0:
            break
        else:
            print("please enter an integer with 1-4 digits")
    player=Player(name,pw,dp)
    players.append(player)
    
    while True:
        confirm=input("Your character have been successfully set up! would you like to add another player? [Y/N] :")
        if confirm.lower()=="y":
            clear()
            break
        elif confirm.lower() =="n":
            setupPlayers=False
            clear()
            break
        else:
            print('Please only enter "Y" for Yes and "N" for No. ')
    

#Game Start
while True:
    while True:
        print ('0  End Game')
        for i in range(1,len(players)+1):
            print(str(i)+'  '+players[i-1].name)
        try:
            index=int(input('Hi, Which one is your character? please enter the corresponding number. 1~n. Enter 0 to end the game :'))
        except ValueError:
            print("Please enter a valid number...")
            continue
        if index==0:
            exitDecision=input('Are you sure to exit the game? All data will be lost!! [Y-exit Anykey-cancel] :')
            if exitDecision.lower() == "y":
                sys.exit()
            else:
                continue
        if index<=len(players) and index>0:
            pw=input('Please enter your password :')
            if players[index-1].pw==pw:
                clear()
                player=players[index-1]
                #player and pw confirmed
                while True:
                    print ('0  End your search')
                    for i in range(1,len(cluelist)+1):
                        print (str(i)+'  '+cluelist[i-1].name+', cost='+str(cluelist[i-1].cost)+' dp.')
                    try:
                        searchplace=int(input('You have '+str(player.dp)+'dp, where would you like to search? enter by its index number or enter 0 to end your search :'))
                    except ValueError:
                        print("Please enter a valid number...")
                        continue
                    if searchplace >=0 and searchplace<len(cluelist):
                        if searchplace == 0:
                            break
                        else:
                            tempclue=cluelist[searchplace-1]
                            player.dp=player.dp-tempclue.cost
                            imagepath=tempclue.viewclue(False)
                            if imagepath == None:
                                clear()
                                print ("Sorry, the place has been searched.")
                                #if return on empty search is set, return 1 dp points
                                if ROES == True:
                                    player.dp = player.dp+1
                            else:
                                image= Image.open(imagepath)
                                image.show()
                                if DAV==False and TAV == True:
                                    while True:
                                        #whether to take the clue after view
                                        tavDecision=input('would you like to take this clue? [Y/N] :')
                                        if tavDecision.lower() == "y":
                                            cluelist[searchplace-1].removeclue(imagepath)
                                            clear()
                                            break
                                        elif tavDecision.lower() == "n":
                                            clear()
                                            break
                                        else:
                                            clear()
                                            print('Please only enter "Y" for Yes and "N" for No.')
                    else:
                        print("You have entered an invalid input, please choose from the listed items.")
            else:
                print('You have entered the wrong pw please try again!')
        else:
            print ('You have entered an invalid input, please try again!')
    
            
                    
                        
        
    



i=cluelist[0]
#for i in oneclue.clues:
print (i.name , i.index,i.cost, i.clues)
for j in i.clues:
    print(j)




    
    
    
