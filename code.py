from tkinter import *
from PIL import ImageTk , Image
from tkinter import ttk
from tkinter import messagebox 
import tkinter


import string


def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line)
    inFile.close()
    return wordlist


wordlist=load_words("artist_description.txt")

class addfiles(object):
    def __int__(self,filename):
        self.filename=filename
    
    def addthings(self,filename,dic):
        """
        Parameters
        ----------
        filename : string
            name of the file
        dic : dictionary
            the dictionary which we have to add

        Returns
        -------
        it will add the thingsidctionary in respective file

        """
        op=open(str(filename),"a")
        for x in dic:
            op.write("/n"+str(x)+":"+str(dic[x])+".")
        return(op.close())
        
    def dictdescription(self,deslist):
        """
        Parameters
        ----------
        deslist : list
            list of description(output of description function)

        Returns
        the dictionary of given list

        """
        dic={}
        for x in deslist.split("."):
            li=x.split(":")
            dic[li[0]]=li[1]
        return(dic)



class artist(addfiles):
    def __init__(self,wordlist):
        self.wordlist=wordlist
        
    def description(self,artist_name):
        """
        Parameters
        ----------
        artist_name : string
            name of artist

        Returns
        -------
        it will return the description of the given artist

        """
        answer=[]
        for x in self.wordlist:
            wlist=x.split(".")
            name=wlist[0].split(":")
            if name[1].lower()==artist_name.lower():
                answer.append(x)
        if len(answer)!=0:
            return("".join(answer))
        else:
            return("false")

    def deleteartist(self,artistname):
        wo=[]
        inFile=open("artist_description.txt","r") 
        for line in inFile:
            if artistname in line:
                line.replace(line,"")
            else:
                wo.append(line)
        inFile.close 
        f=open("artist_description.txt","r+")
        f.truncate()
        f.close
        f=open("artist_description.txt","a")
        for x in wo:
            f.write(x)
        return((wo))



    
    def get_artist_birthplace(self,artistname):
        l=self.description(artistname)
        dic=self.dictdescription(l)
        return(dic["birthplace"])
    
    def get_age(self,artistname):
        l=self.description(artistname)
        dic=self.dictdescription(l)
        return(dic["age"])
    
    def get_nationallity(self,artistname):
        l=self.description(artistname)
        dic=self.dictdescription(l)
        return(dic["nationallity"])
    
    def get_famous_pieces(self,artistname):
        l=self.description(artistname)
        dic=self.dictdescription(l)
        return(dic["famous pieces"])
    
    def get_style_of_art(self,artistname):
        l=self.description(artistname)
        dic=self.dictdescription(l)
        return(dic["style of art"])
    
        
class details(addfiles):
    def __init__(self,wordlist):
         self.wordlist=wordlist
         
    def piecedescription(self,piece):
        """
        Parameters
        ----------
        piece : string
            name of piece

        Returns
        -------
        whole description 

        """
        answer=[]
        for x in self.wordlist:
            wlist=x.split("...")
            name=wlist[0].split(":")
            if name[0].lower()==piece.lower():
                answer.append(x)
        return("".join(answer))
     
        
    def dictdescription(self,deslist):
        """
        Parameters
        ----------
        deslist : list
            list of description(output of description function)

        Returns
        the dictionary of given list

        """
        dic={}
        for x in deslist.split("..."):
            li=x.split(":")
            dic[li[0]]=li[1]
        return(dic)

    def started(self,piece):
        l=self.description(piece)
        dic=self.dictdescription(l)
        return(dic["started"])


class event(addfiles):
    def __init__(self,wordlist):
        self.wordlist=wordlist

    def deleteevent(self,date):
        wo=[]
        inFile=open("event.txt","r") 
        for line in inFile:
            if date in line:
                line.replace(line,"")
            else:
                wo.append(line)
        inFile.close 
        f=open("event.txt","r+")
        f.truncate()
        f.close
        f=open("event.txt","a")
        for x in wo:
            f.write(x)
        return((wo))


    def get_dates(self):
        a=[]
        for x in self.wordlist:
            y =x.split(".")
            b=y[0].split(":")
            a.append(b[1])
        return(a)
        
    def datedata(self,date):
        """
        Parameters
        ----------
        date : date in string form(day-month-year)

        Returns
        return(details of that date)

        """
        answer=[]
        for x in self.wordlist:
            wlist=x.split(".")
            indate=wlist[0].split(":")
            if indate[1]==date:
                answer.append(x)
        if len(answer)!=0:
            return("".join(answer))
        else:
            return ("false")
    
    def get_response(self,date):
        l=self.datedata(date)
        dic=self.dictdescription(l)
        return(dic["response"])
    
    def no_costumers(self,date):
        l=self.datedata(date)
        dic=self.dictdescription(l)
        return(dic["no costumers"])
    
    def get_sold(self,date):
        l=self.datedata(date)
        dic=self.dictdescription(l)
        return(dic["sold"])
    
    def get_number_of_pieces(self,date):
        l=self.datedata(date)
        dic=self.dictdescription(l)
        return(dic["number of pieces"])

#    artist page
#                  starts from 
#                              here
#
# 
#                                   ohkkkkkkkkkkk
def Add(self):
    top =Toplevel()
    top.title("add Artist")
    top.geometry("1000x800")
    top.configure(background="grey89")
    label=Label(top, text="new Artist", bg="grey91",relief=RIDGE, bd=10 , fg="blue4",font="Times 22 bold",padx=200,pady=20)
    label.place(x=50,y=0,width=900)
    frame1=Frame(top,bg="grey86",borderwidth=4,relief=RIDGE)
    frame1.place(x=200,y=140,width=600,height=500)
        
        
    labelan=Label(frame1,text="artistname",bg="grey88",fg="black",font=("none 10",15))
    labelan.place(x=20,y=10)
    name=Entry(frame1,width=25,fg="blue",font=("none 10",15))
    name.place(x=300,y=10)


    labelp=Label(frame1,text="nationallity",bg="grey88",fg="black",font=("none 10",15))
    labelp.place(x=20,y=93)
    n=Entry(frame1,width=25,fg="blue",font=("none 10",15))
    n.place(x=300,y=93)


    labelage=Label(frame1,text="age",bg="grey88",fg="black",font=("none 10",15))
    labelage.place(x=20,y=176)
    age=Entry(frame1,width=25,fg="blue",font=("none 10",15))
    age.place(x=300,y=176)


    labelbirthp=Label(frame1,text="birthplace",bg="grey88",fg="black",font=("none 10",15))
    labelbirthp.place(x=20,y=259)
    birthp=Entry(frame1,width=25,fg="blue",font=("none 10",15))
    birthp.place(x=300,y=259)

    labelan=Label(frame1,text="style of art",bg="grey88",fg="black",font=("none 10",15))
    labelan.place(x=20,y=342)
    sta=Entry(frame1,width=25,fg="blue",font=("none 10",15))
    sta.place(x=300,y=342)

    labelfp=Label(frame1,text="famous piece",bg="grey88",fg="black",font=("none 10",15))
    labelfp.place(x=20,y=425)
    fp=Entry(frame1,width=25,fg="blue",font=("none 10",15))
    fp.place(x=300,y=425)


        #ending things
    addbutton=Button(top, text="add",command=lambda:appendartist(Tk) ,bg="lightyellow2",relief=RIDGE, bd=6, fg="green", font="none 10",padx=10,pady=1)
    addbutton.place(x=250,y=650)
    quitbutton=Button(top, text="quit",command=top.destroy ,bg="lightyellow2",relief=RIDGE, bd=6, fg="red", font="none 10",padx=10,pady=1)
    quitbutton.place(x=720,y=650)

    def appendartist(self):
        if (name.get()!="") and (n.get()!="") and (age.get()!="") and (birthp.get()!="") and (sta.get()!="") and (fp.get()!=""):
            with open("artist_description.txt","a") as f:
                f.write("artist:"+name.get()+".")
                name.delete(0,"end")
                f.write("nationallity:"+n.get()+".")
                n.delete(0,"end")
                f.write("age:"+age.get()+".")
                age.delete(0,"end")
                f.write("birthplace:"+birthp.get()+".")
                birthp.delete(0,"end")
                f.write("style of art:"+sta.get()+".")
                sta.delete(0,"end")
                f.write("famous pieces:"+fp.get()+"\n")
                fp.delete(0,"end")
                f.close
        else:
            messagebox.showinfo("data info","data is incomplete\nPlease complete the data")




    
def artistpage(root):
    root = Toplevel()
    root.title("Artist")
    root.geometry("1000x800")
    root.configure(background="grey74")
                
    flabel=Label(root, text="Artists", bg="silver",relief=RIDGE, bd=10 , fg="blue4",font="Times 22 bold",padx=200,pady=20)
    flabel.place(x=50,y=0,width=900)
    addbutton=Button(root, text="Add new atist",command=lambda:Add(Tk) ,bg="lightyellow2",relief=RIDGE, bd=6, fg="black", font="none 10",padx=1,pady=1)
    addbutton.place(x=50,y=100)

    

    """containg artists
        things like pics details and so on"""
    frame=Frame(root,bg="silver",borderwidth=4,relief=RIDGE)
    frame.place(x=100,y=140,width=800,height=500)

    frame1=Frame(frame,bg="silver",borderwidth=4,relief=RIDGE)
    frame1.place(x=10,y=10,width=200,height=200)
            
    image1=Image.open("artist/picasso.PNG")
    image1=image1.resize((200,200),Image.ANTIALIAS)
    photo=ImageTk.PhotoImage(image1)
    label=Label(frame1,image=photo)
    label.place(x=0,y=0,width=190,height=190)
#    photo= PhotoImage(file="C:/Users/Computer/AppData/Local/Programs/Python/Python39/Scripts/pfproject/artist/Shahzia Sikander.PNG")
#    label= Label(root, image=photo)
#    label.grid(row=0,column=1)


    frame2=Frame(frame,bg="silver",borderwidth=4,relief=RIDGE)
    frame2.place(x=10,y=250,width=200,height=200)
    image2=Image.open("artist/Shahzia Sikander.PNG")
    image2=image2.resize((200,200),Image.ANTIALIAS)
    photo=ImageTk.PhotoImage(image2)
    label=Label(frame2,image=photo)
    label.place(x=0,y=0,width=190,height=190)

    wordlist=load_words("artist_description.txt")
    at=artist(wordlist)
    y1=50
    for artistname in ["picasso","Shahzia Sikander"]:
        label0=Label(frame, text="name:  "+artistname,relief=RIDGE, bd=2,font=("none 10",10))
        label0.place(x=400,y=y1)
        nation="nation:  "+at.get_nationallity(artistname)
        y1+=25
        label1=Label(frame, text=nation,relief=RIDGE, bd=2,font=("none 10",10))
        label1.place(x=400,y=y1)
        age="age:  "+at.get_age(artistname)
        y1+=25
        label2=Label(frame, text=age,relief=RIDGE, bd=2,font=("none 10",10))
        label2.place(x=400,y=y1)
        birthplace="birthplace:  "+at.get_artist_birthplace(artistname)
        y1+=25
        label3=Label(frame, text=birthplace,relief=RIDGE, bd=2,font=("none 10",10))
        label3.place(x=400,y=y1)
        style_of_art="style of art:  "+at.get_style_of_art(artistname)
        y1+=25
        label4=Label(frame, text=style_of_art,relief=RIDGE, bd=2,font=("none 10",10))
        label4.place(x=400,y=y1)
        famous="famous:  "+at.get_famous_pieces(artistname)
        y1+=25
        label5=Label(frame, text=famous,relief=RIDGE, bd=2,font=("none 10",10))
        label5.place(x=400,y=y1)
        y1+=125

    slabel=Label(root,text="Search artist:",bg="grey74")
    slabel.place(x=680,y=100)
    search=Entry(root,font=10)
    search.place(x=750,y=100,width=100)
    addbutton=Button(root, text="-->",command=lambda:searchb(Tk),bg="lightyellow2",relief=RIDGE, bd=1, fg="black", font="none 10")
    addbutton.place(x=860,y=100,height=20)


    def searchb(self):
        entry=search.get()
        root1=Tk()
        root1.title("search artist")
        root1.geometry("700x500")
        root1.configure(background="grey74")
        wordlist=load_words("artist_description.txt")
        at=artist(wordlist)
        if len(entry)>0 and (at.description(entry)!="false"):
            artistname=entry
            f=Label(root1, text="Artist you searched for", bg="silver",relief=RIDGE, bd=10 , fg="blue4",font="Times 22 bold",padx=200,pady=20)
            f.place(x=50,y=0,width=500)
            label0=Label(root1, text="name:  "+artistname,relief=RIDGE, bd=2)
            y1=200
            label0.place(x=400,y=y1)
            nation="nation:  "+at.get_nationallity(artistname)
            y1+=25
            label1=Label(root1, text=nation,relief=RIDGE, bd=2)
            label1.place(x=400,y=y1)
            age="age:  "+at.get_age(artistname)
            y1+=25
            label2=Label(root1, text=age,relief=RIDGE, bd=2)
            label2.place(x=400,y=y1)
            birthplace="birthplace:  "+at.get_artist_birthplace(artistname)
            y1+=25
            label3=Label(root1, text=birthplace,relief=RIDGE, bd=2)
            label3.place(x=400,y=y1)
            style_of_art="style of art:  "+at.get_style_of_art(artistname)
            y1+=25
            label4=Label(root1, text=style_of_art,relief=RIDGE, bd=2)
            label4.place(x=400,y=y1)
            famous="famous:  "+at.get_famous_pieces(artistname)
            y1+=25
            label5=Label(root1, text=famous,relief=RIDGE, bd=2)
            label5.place(x=400,y=y1)
            framer=Frame(root1,bg="grey86",borderwidth=4,relief=RIDGE)
            framer.place(x=10,y=100,width=300,height=300)
            deletebutton=Button(root1, text="delete",command=lambda:dele(),bg="lightyellow2",relief=RIDGE, bd=6, fg="red", font="none 10",padx=10,pady=1)
            deletebutton.place(x=400,y=400)
            updatebutton=Button(root1, text="update",command=lambda:update() ,bg="lightyellow2",relief=RIDGE, bd=6, fg="red", font="none 10",padx=10,pady=1)
            updatebutton.place(x=500,y=400)
            try:
                image1=Image.open("C:/Users/Computer/AppData/Local/Programs/Python/Python39/Scripts/pfproject/artist/"+entry+".PNG")
                image1=image1.resize((200,200),Image.ANTIALIAS)
                photo=ImageTk.PhotoImage(image1)
                label=tkinter.Label(framer,image=photo)
                label.place(x=0,y=0,width=190,height=190)
            except:
                Label(framer,text="no image found").place(x=10,y=90)
        else:
            f=Label(root1, text="sorry,no such artist found here", bg="silver",relief=RIDGE, bd=10 , fg="blue4",font="Times 22 bold",padx=200,pady=20)
            f.place(x=50,y=100,width=500)
            
        def dele():
            wordlist=load_words("artist_description.txt")
            at=artist(wordlist)
            at.deleteartist(artistname)
            root1.destroy()

        def update():
                top =Toplevel()
                artistname=entry
                top.title("update")
                top.geometry("1000x800")
                top.configure(background="grey89")
                label=Label(top, text="new Artist", bg="grey91",relief=RIDGE, bd=10 , fg="blue4",font="Times 22 bold",padx=200,pady=20)
                label.place(x=50,y=0,width=900)
                frame1=Frame(top,bg="grey86",borderwidth=4,relief=RIDGE)
                frame1.place(x=200,y=140,width=600,height=500)
                wordlist=load_words("artist_description.txt")
                at=artist(wordlist)
                    
                    
                labelan=Label(frame1,text="artistname",bg="grey88",fg="black",font=("none 10",15))
                labelan.place(x=20,y=10)
                name=Entry(frame1,width=25,fg="blue",font=("none 10",15))
                name.insert(0,artistname)
                name.place(x=300,y=10)


                labelp=Label(frame1,text="nationallity",bg="grey88",fg="black",font=("none 10",15))
                labelp.place(x=20,y=93)
                n=Entry(frame1,width=25,fg="blue",font=("none 10",15))
                n.insert(0,at.get_nationallity(artistname))
                n.place(x=300,y=93)


                labelage=Label(frame1,text="age",bg="grey88",fg="black",font=("none 10",15))
                labelage.place(x=20,y=176)
                age=Entry(frame1,width=25,fg="blue",font=("none 10",15))
                age.insert(0,at.get_age(artistname))
                age.place(x=300,y=176)


                labelbirthp=Label(frame1,text="birthplace",bg="grey88",fg="black",font=("none 10",15))
                labelbirthp.place(x=20,y=259)
                birthp=Entry(frame1,width=25,fg="blue",font=("none 10",15))
                birthp.insert(0,at.get_artist_birthplace(artistname))
                birthp.place(x=300,y=259)

                labelan=Label(frame1,text="style of art",bg="grey88",fg="black",font=("none 10",15))
                labelan.place(x=20,y=342)
                sta=Entry(frame1,width=25,fg="blue",font=("none 10",15))
                sta.insert(0,at.get_style_of_art(artistname))
                sta.place(x=300,y=342)

                labelfp=Label(frame1,text="famous piece",bg="grey88",fg="black",font=("none 10",15))
                labelfp.place(x=20,y=425)
                fp=Entry(frame1,width=25,fg="blue",font=("none 10",15))
                fp.insert(0,at.get_famous_pieces(artistname))
                fp.place(x=300,y=425)
                addbutton=Button(top, text="add",command=lambda:appendartist(Tk) ,bg="lightyellow2",relief=RIDGE, bd=6, fg="green", font="none 10",padx=10,pady=1)
                addbutton.place(x=250,y=650)
                
                def appendartist(self):
                    with open("artist_description.txt","a") as f:
                        f.write("artist:"+name.get()+".")
                        name.delete(0,"end")
                        f.write("nationallity:"+n.get()+".")
                        n.delete(0,"end")
                        f.write("age:"+age.get()+".")
                        age.delete(0,"end")
                        f.write("birthplace:"+birthp.get()+".")
                        birthp.delete(0,"end")
                        f.write("style of art:"+sta.get()+".")
                        sta.delete(0,"end")
                        f.write("famous pieces:"+fp.get()+"\n")
                        fp.delete(0,"end")
                        f.close
                    top.destroy()

    root.mainloop() 
        

def tkevents(self):
    root = Tk()
    root.title("events")
    root.geometry("1100x800")
    root.configure(background="grey74")
                
    flabel=Label(root, text="events", bg="silver",relief=RIDGE, bd=10 , fg="blue4",font="Times 22 bold",padx=200,pady=20)
    flabel.place(x=50,y=0,width=900)
    frame=Frame(root,bg="grey89",borderwidth=4,relief=RIDGE)
    frame.place(x=70,y=120,height=450,width=400)

    labelno=Label(frame,text="date",bg="grey88",fg="black",font=("none 10",12))
    labelno.place(x=20,y=18,width=100,height=25)
    labeld=Label(frame,text="date should be in day-month-year\n 00-00-0000",bg="grey88",fg="black",font=("none 10",9))
    labeld.place(x=22,y=50)
    date=Entry(frame,width=20,fg="blue",font=("none 10",15))
    date.place(x=157,y=18)

    labelr=Label(frame,text="response",bg="grey88",fg="black",font=("none 10",12))
    labelr.place(x=20,y=108,width=100,height=25)
    r=Entry(frame,width=20,fg="blue",font=("none 10",15))
    r.place(x=157,y=108)

    labelc=Label(frame,text="no. of costumers",bg="grey88",fg="black",font=("none 10",10))
    labelc.place(x=20,y=198,width=100,height=25)
    c=Entry(frame,width=20,fg="blue",font=("none 10",15))
    c.place(x=157,y=198)

    labels=Label(frame,text="sold",bg="grey88",fg="black",font=("none 10",12))
    labels.place(x=20,y=288,width=100,height=25)
    s=Entry(frame,width=20,fg="blue",font=("none 10",15))
    s.place(x=157,y=288)

    labelno=Label(frame,text="number of pieces ",bg="grey88",fg="black",font=("none 10",10))
    labelno.place(x=20,y=378,width=100,height=25)
    no=Entry(frame,width=20,fg="blue",font=("none 10",15))
    no.place(x=157,y=378)

    quitbutton=Button(root, text="quit",command=root.destroy ,bg="lightyellow2",relief=RIDGE, bd=6, fg="red", font="none 10",padx=10,pady=1)
    quitbutton.place(x=400,y=600,width=80,height=25)
    addbutton=Button(root, text="Add new event",command=lambda:appendevents(Tk) ,bg="lightyellow2",relief=RIDGE, bd=6, fg="black", font="none 10",padx=1,pady=1)
    addbutton.place(x=70,y=600,width=100,height=25)
    def appendevents(self):
        with open("event.txt","a") as f:
            f.write("date:"+date.get()+".")
            date.delete(0,"end")
            f.write("no costumers:"+c.get()+".")
            c.delete(0,"end")
            f.write("number of pieces:"+no.get()+".")
            no.delete(0,"end")
            f.write("sold:"+s.get()+".")
            s.delete(0,"end")
            f.write("response:"+r.get()+"\n")
            r.delete(0,"end")
            f.close
    
    frame2=Frame(root,bg="grey84",borderwidth=4,relief=RIDGE,)
    frame2.place(x=500,y=150,width=550,height=500)
    slabel=Label(root,text="Search event \nby date:",bg="grey74")
    slabel.place(x=670,y=100)
    search=Entry(root,font=10)
    search.place(x=750,y=100,width=100)
    addbutton=Button(root, text="-->",command=lambda:searche(Tk),bg="lightyellow2",relief=RIDGE, bd=1, fg="black", font="none 10")
    addbutton.place(x=860,y=100,height=20)
    label0=Label(frame2,text="date")
    label0.place(x=10,y=10)
    

    scroll=ttk.Scrollbar(frame2,orient=VERTICAL)
    scroll.pack(side=RIGHT,fill=Y)


    label1=Label(frame2,text="no.of custumers")
    label1.place(x=100,y=10)
    label2=Label(frame2,text="number of pieces")
    label2.place(x=230,y=10)
    label3=Label(frame2,text="sold")
    label3.place(x=380,y=10)
    label4=Label(frame2,text="response")
    label4.place(x=450,y=10)
    a=load_words("event.txt")
    av=event(a)
    dates=av.get_dates()
    ya=40
    for x in dates:
        Label(frame2,text=x).place(x=10,y=ya)
        Label(frame2,text=av.no_costumers(x)).place(x=100,y=ya)
        Label(frame2,text=av.get_number_of_pieces(x)).place(x=230,y=ya)
        Label(frame2,text=av.get_sold(x)).place(x=380,y=ya)
        Label(frame2,text=av.get_response(x)).place(x=450,y=ya)
        ya+=40


    def searche(self):
        entry=search.get()
        root1=Tk()
        root1.title("search event")
        root1.geometry("700x500")
        root1.configure(background="grey74")
        wordlist=load_words("event.txt")
        ev=event(wordlist)
        if len(entry)>0 and (ev.datedata(entry))!="false":
            f=Label(root1, text="event you searched for", bg="silver",relief=RIDGE, bd=10 , fg="blue4",font="Times 22 bold",padx=200,pady=20)
            f.place(x=50,y=0,width=500)
            label0=Label(root1, text="date:  "+entry,relief=RIDGE,font=("none 10",15), bd=2)
            y1=100
            label0.place(x=50,y=y1)
            nation="response:  "+ev.get_response(entry)
            y1+=80
            label1=Label(root1,font=("none 10",15), text=nation,relief=RIDGE, bd=2)
            label1.place(x=50,y=y1)
            age="no. costumers:  "+ev.no_costumers(entry)
            y1+=80
            label2=Label(root1, font=("none 10",15),text=age,relief=RIDGE, bd=2)
            label2.place(x=50,y=y1)
            birthplace="sold:  "+ev.get_sold(entry)
            y1+=80
            label3=Label(root1, font=("none 10",15),text=birthplace,relief=RIDGE, bd=2)
            label3.place(x=50,y=y1)
            style_of_art="number of pieces:  "+ev.get_number_of_pieces(entry)
            y1+=80
            label4=Label(root1,font=("none 10",15), text=style_of_art,relief=RIDGE, bd=2)
            label4.place(x=50,y=y1)
            button=Button(root1,text="update",relief=RIDGE,command=lambda:update(Tk),font=("none 10",15)).place(x=500,y=300,width=100,height=50)
            button=Button(root1,text="delete",relief=RIDGE,command=lambda:delete(Tk),font=("none 10",15)).place(x=500,y=400,width=100,height=50)
        else:
            f=Label(root1, text="no such event is registered yet", bg="silver",relief=RIDGE, bd=10 , fg="blue4",font="Times 22 bold",padx=200,pady=20)
            f.place(x=50,y=100,width=500)

        def delete(self):
            entry=search.get()
            wordlist=load_words("event.txt")
            ev=event(wordlist)
            ev.deleteevent(entry)
            root1.destroy()
    
    def update(self):
        root2 = Tk()
        entry=search.get()
        root2.title("events update")
        root2.geometry("500x650")
        root2.configure(background="grey74")
        a=load_words("event.txt")
        ev=event(a)
                    
        flabel=Label(root2, text="event update", bg="silver",relief=RIDGE, bd=10 , fg="blue4",font="Times 22 bold",padx=200,pady=20)
        flabel.place(x=50,y=0,width=500)
        frame=Frame(root2,bg="grey89",borderwidth=4,relief=RIDGE)
        frame.place(x=70,y=120,height=450,width=400)

        labelno=Label(frame,text="date",bg="grey88",fg="black",font=("none 10",12))
        labelno.place(x=20,y=18,width=100,height=25)
        labeld=Label(frame,text="date should be in day-month-year\n 00-00-0000",bg="grey88",fg="black",font=("none 10",9))
        labeld.place(x=22,y=50)
        da=Entry(frame,width=20,fg="blue",font=("none 10",10))
        da.insert(0,entry)
        da.place(x=157,y=18)

        labelr=Label(frame,text="response",bg="grey88",fg="black",font=("none 10",12))
        labelr.place(x=20,y=108,width=100,height=25)
        res=Entry(frame,width=20,fg="blue",font=("none 10",10))
        res.insert(0,ev.get_response(entry))
        res.place(x=157,y=108)

        labelc=Label(frame,text="no. of costumers",bg="grey88",fg="black",font=("none 10",10))
        labelc.place(x=20,y=198,width=100,height=25)
        cos=Entry(frame,width=20,fg="blue",font=("none 10",10))
        cos.insert(0,ev.no_costumers(entry))
        cos.place(x=157,y=198)

        labels=Label(frame,text="sold",bg="grey88",fg="black",font=("none 10",12))
        labels.place(x=20,y=288,width=100,height=25)
        st=Entry(frame,width=20,fg="blue",font=("none 10",10))
        st.insert(0,ev.get_sold(entry))
        st.place(x=157,y=288)

        labelno=Label(frame,text="number of pieces ",bg="grey88",fg="black",font=("none 10",10))
        labelno.place(x=20,y=378,width=100,height=25)
        no=Entry(frame,width=20,fg="blue",font=("none 10",10))
        no.insert(0,ev.get_number_of_pieces(entry))
        no.place(x=157,y=378)

        button0=Button(root2, text="Add event",command=lambda:upevent(Tk) ,bg="lightyellow2",relief=RIDGE, bd=6, fg="black", font="none 10",padx=1,pady=1)
        button0.place(x=70,y=600,width=100,height=25)
    
    
        def upevent(self):
            entry=da.get()
            wordlist=load_words("event.txt")
            ev=event(wordlist)
            a=da.get()
            b=cos.get()
            co=no.get()
            d=st.get()
            e=res.get()
            ev=event(wordlist)
            ev.deleteevent(entry)

            with open("event.txt","a") as f:
                f.write("date:"+a+".")
                f.write("no costumers:"+b+".")
                f.write("number of pieces:"+co+".")
                f.write("sold:"+d+".")
                f.write("response:"+e)
                f.close

            root2.destroy()



class mainpage():
    def __init__(self,root):
        self.root=root
        self.root.title("Art Gallery managment")
        self.root.geometry("1000x800")
        self.root.configure(background="grey74")
        frame1=Frame(self.root,bg="grey86",borderwidth=8,relief=RIDGE)
        frame1.place(x=100,y=140,width=800,height=500)
        #all the buttons 
        buttonartist=Button(frame1, text="Artist",command=lambda:artistpage(Tk),bg="lightblue1",relief=RIDGE, bd=10, fg="black", padx=50,pady=20,font=("none 10",15))
        buttonevent=Button(frame1, text="event",bg="lightblue1",command=lambda:tkevents(Tk),relief=RIDGE, bd=10 , fg="black",padx=50,pady=20,font=("none 10",15))


    #all the labels
        Label(root, text="Art Gallery ", bg="Royalblue1",relief=RIDGE, bd=10 , fg="blue4",font="Times 22 bold",padx=200,pady=20).place(x=50,y=0,width=900)
        Label(frame1, text="Welcome ", bg="SteelBlue1", fg="blue4",relief=RIDGE,bd=8,font="none 16 italic underline",padx=100,pady=20).place(x=200,y=0)


        #details of the buttons
        Label(frame1 , text="it will contain \nthe detail of artist",relief=RIDGE,font=("none 10",12),bd=5).place(x=450,y=150,width=200,height=100)
        Label(frame1 , text="contain the information of \n number of costumers,\nthe pieces,sold, \n response events etc",font=("none 10",12),relief=RIDGE,bd=5).place(x=400,y=325,width=300,height=80)


        #buttons on the grid
        buttonartist.place(x=100,y=130,width=200,height=100)
        buttonevent.place(x=100,y=300,width=200,height=100)

class login():
    def __init__(self,root):
        self.root=root
        self.root.title("Art Gallery managment")
        self.root.geometry("1000x800")
        self.root.configure(background="grey74")
        Label(self.root, text="enter login and password please", bg="white",relief=RIDGE, bd=10 , fg="blue4",font="Times 22 bold",padx=200,pady=20).place(x=50,y=0,width=900)
        frameu=Frame(root,borderwidth=4,relief=RIDGE)
        frameu.place(x=130,y=150,width=700,height=200)
        Label(frameu, text="enter username", bg="grey79", fg="black",relief=RIDGE,bd=5,font=("none 16 italic underline",15)).place(x=10,y=40,width=200,height=100)
        framee=Frame(frameu,borderwidth=4,relief=RIDGE)
        framee.place(x=300,y=70,width=300,height=50)
        self.entryuser=Entry(framee,width=20,fg="black",font=("none 10",25))
        self.entryuser.place(x=0,y=0,width=290)

        framep=Frame(root,borderwidth=4,relief=RIDGE)
        framep.place(x=130,y=380,width=700,height=200)
        Label(framep, text="enter password", bg="grey79", fg="black",relief=RIDGE,bd=5,font=("none 16 italic underline",15)).place(x=10,y=40,width=200,height=100)
        framepe=Frame(framep,borderwidth=4,relief=RIDGE)
        framepe.place(x=300,y=70,width=300,height=50)
        self.entrylogin=Entry(framepe,width=20,fg="black",font=("none 10",25))
        self.entrylogin.place(x=0,y=0,width=290)
        button=Button(root,text="enter",bg="lightyellow2",command=lambda:self.next(),relief=RIDGE, bd=6, fg="black", font="none 10",padx=10,pady=1).place(x=750,y=600,width=100,height=50)
        quitbutton=Button(root, text="quit",command=root.destroy ,bg="lightyellow2",relief=RIDGE, bd=6, fg="red", font="none 10",padx=10,pady=1)
        quitbutton.place(x=150,y=600,width=100,height=50)

    def next(self):
        user=self.entryuser.get()
        password=self.entrylogin.get()
        if user=="abcd" and password=="1234":
           self. root.destroy()
           top=Tk()
           mainpage(top)
        else:
            messagebox.showinfo("data info","you entered the wrong password")


    
    


if __name__ =='__main__':
    root1=Tk()
    login(root1)
    root1.mainloop()

