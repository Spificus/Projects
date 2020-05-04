from bookrecs import friends, recommend, report
from breezypythongui import *

'''I declare that the following source code was written solely by me.
I understand that copying any source code, in whole or in part,
constitutes cheating, and that I will receive a zero on this project
if I am found in violation of this policy.'''

def genfriends(person,nfriends):
    fstring = ''
    fgroup =  friends(person,nfriends)
    for i in fgroup:
        fstring += i
        fstring +='\n'
    return fstring

def genrec(person,nfriends):
    rstring = ''
    rgroup = recommend(person,nfriends)
    for i in rgroup:
        rstring += f'{i[0]}, {i[1]}'
        rstring += '\n'
    return rstring

class Bookrecommendation(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title = "Book Recommendations", width = 300, height = 50)

        self.addButton(text = "Friends", row = 0,column = 0, command = self.Friends)
        self.addButton(text = "Recommend", row = 0,column = 1, command = self.Recommend)
        self.addButton(text= "Report", row = 0, column = 2, command = self.ReportHandler)

    def ReportHandler(self):
        genreport = report()
        self.messageBox(title = 'Report', message = genreport, width= 70, height= 40)


    def Friends(self):
        self.respondF = respondFriend(self,'Friends')
        if self.respondF.modified():
            self.Reader = self.respondF.Reader.getText()
            self.numfriends = self.respondF.numfriends.getNumber()
            try:
                self.messageBox(title = "friends of " +self.Reader, message = genfriends(self.Reader, self.numfriends))
            except:
                self.messageBox(title="ERROR", message="No such reader")
                return False

    def Recommend(self):
        self.respondR = respondRec(self,'Recommend')
        if self.respondR.modified():
            self.Reader = self.respondR.Reader.getText()
            self.numfriends = self.respondR.numfriends.getNumber()
            try:
                self.messageBox(title = "Recommendations for " + self.Reader, message = genrec(self.Reader, self.numfriends), width=60,height=25)
            except:
                self.messageBox(title="ERROR", message="No such reader")
                return False


class respondFriend(EasyDialog):
    def __init__(self,parent,title):
        EasyDialog.__init__(self, parent,title)
    def body(self,parent):
        self.addLabel(parent,text="Reader:",row=0,column=0)
        self.addLabel(parent,text="# of friends:",row=1,column=0)
        self.Reader = self.addTextField(parent,"",row=0,column=1)
        self.numfriends = self.addIntegerField(parent,"2",row=1,column=1)
    def validate(self):
        Reader = self.Reader.getValue()
        numfriends = self.numfriends.getNumber()
        if Reader == "" and numfriends <= 0:
            self.messageBox(title="ERROR", message="Invalid inputs")
            return False
        if Reader == "":
            self.messageBox(title="ERROR", message="No such reader")
            return False
        if numfriends <= 0 or numfriends == "":
            self.messageBox(title="ERROR", message="# of friends must be positive")
            return False
        else:
            return True
    def apply(self):
        self.setModified()

class respondRec(EasyDialog):
    def __init__(self,parent,title):
        EasyDialog.__init__(self, parent,title)
    def body(self,parent):
        self.addLabel(parent,text="Reader:",row=0,column=0)
        self.addLabel(parent,text="# of friends:",row=1,column=0)
        self.Reader = self.addTextField(parent,"",row=0,column=1)
        self.numfriends = self.addIntegerField(parent,"",row=1,column=1)
    def validate(self):
        Reader = self.Reader.getValue()
        numfriends = self.numfriends.getNumber()
        if Reader == "" and numfriends <= 0:
            self.messageBox(title="ERROR", message="Invalid inputs")
            return False
        if Reader == "":
            self.messageBox(title="ERROR", message="No such reader")
            return False
        if numfriends <= 0 or numfriends == "":
            self.messageBox(title="ERROR", message="# of friends must be positive")
            return False
        else:
            return True
    def apply(self):
        self.setModified()

def main():
    """Instantiate and pop up the window."""
    Bookrecommendation().mainloop()

if __name__ == "__main__":
    main()