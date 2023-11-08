import sys
import pyttsx3
from PyQt5.QtWidgets  import *
from PyQt5 import *
from PyQt5 import QtCore 
from PyQt5.QtCore import Qt 
from PyQt5.QtGui import *
import time
from PyQt5 import QtGui , QtWidgets
import webbrowser
import os
from PyQt5.QtCore import *


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
      # print(voices[1].id)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 170)

def speak(audio):
      engine.say(audio)
      engine.runAndWait()


def pravesh():
     label3.hide, btn.hide(), btn2.hide(), btn3.hide(), btn4.hide(),btn5.hide(),btn6.hide()
     btn7.hide(), btn8.hide(),btn9.hide(),btn10.hide()

     btnp = QPushButton(w)
     btnp.setText('HISTORY OF THE MOVEMENT')
    #btn.move(450,130)
     btnp.setGeometry(370,200,300,50)
     btnp.setStyleSheet('''QPushButton {
    background-color: skyblue;
    color: red;
    border-style: inset;
    padding: 2px;
    font: bold 16px;
    border-color: blue;
    border-width: 6px;
    border-radius: 10px;
}
QPushButton:hover {
    background-color: #FF1493;
    color: Cyan;
    border-width: 4px;
    border-radius: 8px;
}''')
     #btnp.setStyleSheet("font-style:bold;font-size:20px; color:red;background-color:skyblue;")
     btnp.show()
     def non():
           btnp = QLabel(w)
           btnp.setText('HISTORY OF THE MOVEMENT')
    #btn.move(450,130)
           btnp.setGeometry(370,200,300,50)
           btnp.setStyleSheet("font-style:bold;font-size:20px; color:red;background-color:skyblue;")
           btnp.show()
           his()
     btnp.clicked.connect(non)
                  
     btnP2 = QPushButton(w)
     btnP2.setText('Law , promise , motto')
    #btn.move(450,130)
     btnP2.setGeometry(370,260,300,50)
     btnP2.setStyleSheet('''QPushButton {
    background-color: skyblue;
    color: red;
    border-style: inset;
    padding: 2px;
    font: bold 16px;
    border-color: blue;
    border-width: 6px;
    border-radius: 10px;
}
QPushButton:hover {
    background-color: #FF1493;
    color: Cyan;
    border-width: 4px;
    border-radius: 8px;
}''')
     #btnP2.setStyleSheet("font-style:bold;font-size:20px; color:red;background-color:skyblue;")
     btnP2.show()
     def law2():
           btnp.hide(),btnP2.hide(),btnp3.hide(),btnp4.hide(),btnp5.hide(),btnp6.hide()
           law()
     btnP2.clicked.connect(law2)

     btnback = QPushButton(w)
     btnback.setText("GO BACK")
     btnback.setGeometry(435,600,180,50)
     btnback.setStyleSheet('''QPushButton {
    background-color: violet;
    color: white;
    border-style: inset;
    padding: 2px;
    font: bold 16px;
    border-color: blue;
    border-width: 6px;
    border-radius: 10px;
}
QPushButton:hover {
    background-color: Deepblue;
    color: deeppink;
    border-width: 4px;
    border-radius: 8px;
}''')
     btnback.show()
     def backprav():
           btnback.hide()
           print("argv: ", sys.argv)
           print("sys executable: " , sys.executable)
           os.execv(sys.executable,['python'] + sys.argv)
     btnback.clicked.connect(backprav)

     btnp5 = QPushButton(w)
     btnp5.setText("UNIFORM")
     btnp5.setGeometry(370,440,300,50)
     btnp5.setStyleSheet('''QPushButton {
    background-color: skyblue;
    color: red;
    border-style: inset;
    padding: 2px;
    font: bold 16px;
    border-color: blue;
    border-width: 6px;
    border-radius: 10px;
}
QPushButton:hover {
    background-color: #FF1493;
    color: Cyan;
    border-width: 4px;
    border-radius: 8px;
}''')
     #btnp5.setStyleSheet("font-style:bold;font-size:20px; color:red;background-color:skyblue;")
     btnp5.show()
     def uni():
           btnp5.hide()
           labeluni = QLabel(w)
           labeluni.setPixmap(QPixmap('uni3.jpg'))
           labeluni.setGeometry(10,140,300,500)
           labeluni.show()

           labeluni2 = QLabel(w)
           labeluni2.setPixmap(QPixmap('whatuni1.jpg'))
           labeluni2.setGeometry(315,140,353,500)
           labeluni2.show()

           labeluni3 = QLabel(w)
           labeluni3.setPixmap(QPixmap('whatuni2.jpg'))
           labeluni3.setGeometry(650,140,353,500)
           labeluni3.show()

           btnuni1 = QPushButton(w)
           btnuni1.setText("GUIDE UNIFORM")
           btnuni1.setGeometry(435,600,180,50)
           btnuni1.show()
           def guideuni():
                 btnuni1.hide()
                 labeluni.hide(), labeluni2.hide(), labeluni3.hide()
                 labeluni.setPixmap(QPixmap('guide-uniform1.jpg'))
                 labeluni.setGeometry(10,140,440,600)
                 labeluni.show()

                 labeluni2.setPixmap(QPixmap('guideuniform2.jpg'))
                 labeluni2.setGeometry(435,140,500,354)
                 labeluni2.show()

                 labeluni3.setPixmap(QPixmap('guideuniform3.jpg'))
                 labeluni3.setGeometry(435,495,500,354)
                 labeluni3.show()
                
           btnuni1.clicked.connect(guideuni)
           btnuni = QPushButton(w)
           btnuni.setText("GO BACK")
           btnuni.setGeometry(900,50,120,20)
           def backuni():
                btnuni.hide(),labeluni.hide(),labeluni2.hide(),labeluni3.hide()
                pravesh()
           btnuni.clicked.connect(backuni)
           btnuni.show()
     btnp5.clicked.connect(uni)
     
     btnp3 = QPushButton(w)
     btnp3.setText("FLAGS")
     btnp3.setGeometry(370,320,300,50)
     btnp3.setStyleSheet('''QPushButton {
    background-color: skyblue;
    color: red;
    border-style: inset;
    padding: 2px;
    font: bold 16px;
    border-color: blue;
    border-width: 6px;
    border-radius: 10px;
}
QPushButton:hover {
    background-color: #FF1493;
    color: Cyan;
    border-width: 4px;
    border-radius: 8px;
}''')
     #btnp3.setStyleSheet("font-style:bold;font-size:20px; color:red;background-color:skyblue;")
     btnp3.show()
     btnp3.clicked.connect(flag)
     
     btnp4 = QPushButton(w)
     btnp4.setText("SIGN, SALUTE, LEFT HAND SHAKE")
     btnp4.setGeometry(370,380,300,50)
     btnp4.setStyleSheet('''QPushButton {
    background-color: skyblue;
    color: red;
    border-style: inset;
    padding: 2px;
    font: bold 16px;
    border-color: blue;
    border-width: 6px;
    border-radius: 10px;
}
QPushButton:hover {
    background-color: #FF1493;
    color: Cyan;
    border-width: 4px;
    border-radius: 8px;
}''')
     #btnp4.setStyleSheet("font-style:bold;font-size:18px; color:red;background-color:skyblue;")
     btnp4.show()
     btnp4.clicked.connect(hand)

     btnp6 = QPushButton(w)
     btnp6.setText("SONGS WITH MEANING")
     btnp6.setGeometry(370,440,300,50)
     btnp6.setStyleSheet('''QPushButton {
    background-color: skyblue;
    color: red;
    border-style: inset;
    padding: 2px;
    font: bold 16px;
    border-color: blue;
    border-width: 6px;
    border-radius: 10px;
}
QPushButton:hover {
    background-color: #FF1493;
    color: Cyan;
    border-width: 4px;
    border-radius: 8px;
}''')
     #btnp6.setStyleSheet("font-style:bold;font-size:18px; color:red;background-color:skyblue;")
     btnp6.show()
     def song():
           btnp6.hide(),btnp.hide(),btnP2.hide(),btnp3.hide(),btnp4.hide(),btnp5.hide()
           btns = QPushButton(w)
           btns.setText("NATIONAL ANTHEM")
           btns.setGeometry(370,200,300,50)
           btns.setStyleSheet("font-style:bold;font-size:18px; color:red;background-color:skyblue;")
           def nation():
                 btns.hide(),btns1.hide(),btns2.hide()
                 labelnation = QLabel(w)
                 labelnation.setPixmap(QPixmap('nationalanthem.jpg'))
                 labelnation.setGeometry(0,140,270,350)
                 labelnation.show()

                 labelnation1 = QLabel(w)
                 labelnation1.setText('''Jana-gana-mana-adhinayaka, jaya he
Bharata-bhagya-vidhata
Panjaba-Sindha-Gujrata-Maharata-
Dravida-Utkala-Vanga
Vindhya-Himachala-Yamuna-Ganga
Uchhala-Jaladhi-taranga
Tava shubha name jage

Tava shubha ashisha mage
Gave tava jaya-gatha
Jana-gana-mangala-dayaka jaya he
Bharata-bhagya-vidhata.
Jaya he! Jaya he! Jaya he!
Jaya jaya jaya, jaya he!''')
                 labelnation1.setGeometry(270,140,360,370)
                 labelnation1.setStyleSheet("font-style:bold;font-size:20px;color:red;background-color:lightgreen; border: 5px solid voilet")
                 labelnation1.show()

                 labelnation2 = QLabel(w)
                 labelnation2.setText('''Thou art the ruler of the 
minds of all people,
Thou Dispenser of India's destiny.
Thy name rouses the hearts of 
Punjab, Sind, Gujrat and Maratha,
Of Dravid, Orissa and Bengal.

It echoes in the hills of the
Vindhyas and Himalayas,Mingles
in the music of Jamna and Ganges 
and is chanted by the waves of 
the Indian sea.They pray for Thy
blessings and sing thy praise.The  
saving of all people waits in thy hand,
Thou Dispenser of India's destiny,
Victory, Victory, Victory to Thee.''')
                 labelnation2.setGeometry(630,140,360,390)
                 labelnation2.setStyleSheet("font-style:bold;font-size:20px;color:red;background-color:lightgreen; border: 5px solid voilet")
                 labelnation2.show()
                 btnna = QPushButton(w)
                 btnna.setText('play audio')
                 #btn.move(450,130)
                 btnna.setGeometry(600,550,220,50)
                 btnna.setStyleSheet("font-style:bold;font-size:20px; color:red;background-color:grey; border: 2px solid gold")
                 btnna.show()
                 def nationsong():
                       os.startfile('national.mp3')
                 btnna.clicked.connect(nationsong)
                 
                 def backnation():
                       btnsback.hide(),btnna.hide()
                       labelnation.hide(),labelnation1.hide(),labelnation2.hide()
                       song()
                 btnsback = QPushButton(w)
                 btnsback.setText("GO BACK")
                 btnsback.setGeometry(900,50,120,20)
                 btnsback.clicked.connect(backnation)
                 btnsback.show()
           btns.clicked.connect(nation)
           btns.show()

           btns1 = QPushButton(w)
           btns1.setText("FLAG SONG")
           btns1.setGeometry(370,260,300,50)
           btns1.setStyleSheet("font-style:bold;font-size:18px; color:red;background-color:skyblue;")
           def flagsong():
                 labelflag = QLabel(w)
                 labelflag.setPixmap(QPixmap('flag song.jpg'))
                 labelflag.setGeometry(190,140,638,460)
                 labelflag.show()
                 btnfa = QPushButton(w)
                 btnfa.setText('play audio')
                 #btn.move(450,130)
                 btnfa.setGeometry(600,550,220,50)
                 btnfa.setStyleSheet("font-style:bold;font-size:20px; color:red;background-color:grey; border: 2px solid gold")
                 btnfa.show()
            
                 btnfback = QPushButton(w)
                 btnfback.setText("GO BACK")
                 btnfback.setGeometry(900,50,120,20)
                 def backflag():
                       btnfback.hide(),labelflag.hide(),btnfa.hide()
                       song()
                 btnfback.clicked.connect(backflag)
                 btnfback.show()
                 

                 def flagsong():
                       os.startfile('flagsong.mp3')
                 btnfa.clicked.connect(flagsong)
           btns1.clicked.connect(flagsong)
           btns1.show()
           
           btns2 = QPushButton(w)
           btns2.setText("PRAYER SONG")
           btns2.setGeometry(370,320,300,50)
           btns2.setStyleSheet("font-style:bold;font-size:18px; color:red;background-color:skyblue;")
           def prayer():
                 labelpray = QLabel(w)
                 labelpray.setPixmap(QPixmap('prayer.jpg'))
                 labelpray.setGeometry(200,135,638,479)
                 labelpray.show()
                 btnfa2 = QPushButton(w)
                 btnfa2.setText('play audio')
                 #btn.move(450,130)
                 btnfa2.setGeometry(620,570,220,50)
                 btnfa2.setStyleSheet("font-style:bold;font-size:20px; color:red;background-color:grey; border: 2px solid gold")
                 def prayeraud():
                       os.startfile('prayersong.mp3')
                 btnfa2.clicked.connect(prayeraud)
                 btnfa2.show()
                 btnfback2 = QPushButton(w)
                 btnfback2.setText("GO BACK")
                 btnfback2.setGeometry(900,50,120,20)
                 def backflag2():
                       btnfback2.hide(),btnfa2.hide(),labelpray.hide()
                       song()
                 btnfback2.clicked.connect(backflag2)
                 btnfback2.show()
                 

           btns2.clicked.connect(prayer)
           btns2.show()
           btnfb1 = QPushButton(w)
           btnfb1.setText("GO BACK")
           btnfb1.setGeometry(900,50,120,20)
           def backfb():
                btns.hide(),btns1.hide(),btns2.hide(),btnfb1.hide()
                pravesh()
           btnfb1.clicked.connect(backfb)
           btnfb1.show()
     btnp6.clicked.connect(song)
def hand(): 
      labelhan = QLabel(w)
      labelhan.setPixmap(QPixmap('sign.jpg'))
      labelhan.setGeometry(180,170,720,437)
      labelhan.show()
      btnhan = QPushButton(w)
      btnhan.setText("NEXT PAGE")
      btnhan.setGeometry(400,600,220,50)
      btnhan.setStyleSheet("font-style:bold;font-size:20px; color:red;background-color:grey")
      btnhan.show()
     
      def nexthan():
            labelhan.hide()
            def sal():
                  labelsal = QLabel(w)
                  labelsal.setPixmap(QPixmap('salute.jpg'))
                  labelsal.setGeometry(240,160,760,457)
                  labelsal.show()
                  btnhan.setGeometry(400,620,220,50)
                  btnhan.setText("PREV")
                  def prev():
                        labelsal.hide()
                        nexthan()
                        def han():
                              btnhan.hide()
                              hand()
                        btnhan.clicked.connect(han)
                  btnhan.clicked.connect(prev)

            btnhan.clicked.connect(sal)
            
            labelnex = QLabel(w)
            labelnex.setPixmap(QPixmap('lefthand.jpg'))
            labelnex.setGeometry(220,170,720,437)
            labelnex.show()
      btnhan.clicked.connect(nexthan)
      btnback = QPushButton(w)
      btnback.setText("GO BACK")
      btnback.setGeometry(200,610,150,50)
      btnback.show()
      def backprav():
           btnback.hide()
           print("argv: ", sys.argv)
           print("sys executable: " , sys.executable)
           os.execv(sys.executable,['python'] + sys.argv)
      btnback.clicked.connect(backprav)          
      
      
def flag():
      labelfla = QLabel(w)
      labelfla.setPixmap(QPixmap('flag.jpg'))
      labelfla.setGeometry(160,180,720,437)
      labelfla.show()

      btnfla = QPushButton(w)
      btnfla.setText("ABOUT THE FLAG")
      btnfla.setGeometry(435,610,180,50)
      btnfla.setStyleSheet("font-style:bold;font-size:20px;color:red;background-color:skyblue;")
      btnfla.show()
      def btnfa():
            os.startfile("mainweb.html")

      btnfla.clicked.connect(btnfa)

      btnfla1 = QPushButton(w)
      btnfla1.setText("GO BACK")
      btnfla1.setGeometry(900,50,120,20)
      def backfla():
            btnfla1.hide(),btnfla.hide(),labelfla.hide()
            pravesh()
      btnfla1.clicked.connect(backfla)
      btnfla1.show()
def law():
      labella = QLabel(w)
      labella.setPixmap(QPixmap('pro.jpg'))
            #labella.resize(100,100)
      labella.setGeometry(10,160,491,531)
      labella.show()
      labelm = QLabel(w)
      labelm.setPixmap(QPixmap('moto.jpg'))
      labelm.setGeometry(500,340,500,246)
      labelm.show()
      btnl2 = QPushButton(w)
      btnl2.setText('play audio')
      #btn.move(450,130)
      btnl2.setGeometry(620,580,220,50)
      btnl2.setStyleSheet("font-style:bold;font-size:20px; color:red;background-color:grey; border: 2px solid gold")
      btnl2.show()
      btnl2.clicked.connect(ls)
      labellaw = QLabel(w)
      labellaw.setText('''MOTO
It is achived by being Physically 
Strong, Mentally awake, and
Morally Straight.
      "Be Prepared"''')
      labellaw.setGeometry(500,160,440,180)
      labellaw.setStyleSheet("font-style:bold;font-size:20px;color:red;background-color:lightgreen; border: 5px solid voilet")
      labellaw.show()
      btnlaw = QPushButton(w)
      btnlaw.setText("GO BACK")
      btnlaw.setGeometry(900,50,120,20)
      def backlaw():
            btnlaw.hide(),labella.hide(),labelm.hide(),btnl2.hide(),labellaw.hide()
            pravesh()
            
      btnlaw.clicked.connect(backlaw)
      btnlaw.show()
                  
def his():
            
            labelhis = QLabel(w)
            labelhis.setText('''Boy Scouts, organization, originally for boys from 11 to 14 or 15 years of age, that aimed to
      develop in them good citizenship, chivalrous behaviour, and skill in various outdoor activities.The Boy Scout 
      movement was founded in Great Britain in 1908 by a cavalry officer, Lieutenant General Robert S.S 
      (later Lord)Baden-Powell, who had written a book called Scouting for Boys (1908) but who was 
      better known as the defender of the town of Mafeking in the South African (or Boer) War. 
      Baden-Powell's book described many games and contests that he had used to train cavalry troops
      in scouting, and it became popular reading among the boys of Great Britain. Prior to the 
      book's publication, Baden-Powell held an experimental camp on Brownsea Island off the coast of 
      southern England in which he put into practice his ideas on the trainng of boys.''')
            labelhis.setGeometry(10,250,1000,400)
            labelhis.setStyleSheet("font-style:bold;font-size:20px;color:red;background-color:lightgreen; border: 5px solid voilet")
            labelhis.show()
            btnhis = QPushButton(w)
            btnhis.setText("GO BACK")
            btnhis.setGeometry(900,50,120,20)
            def back():
                  btnhis.hide()
                  labelhis.hide()
                  pravesh()
            btnhis.clicked.connect(back)
            btnhis.show()
            
      
def ls():
      speak('''Scout and Guide Law
            
A Scout Guide is trustworthy
A Scout Guide is loyal
A Scout Guide is a friend to all and a brother sister to every other Scout Guide.
A Scout Guide is courteous
A Scout Guide is a friend to animals and loves nature.
A Scout Guide is disciplined and helps to protect public property.
A Scout Guide is courageous.
A Scout Guide is thrifty.
A Scout Guide is pure in thought, word and deed.''')

def sound():
      webbrowser.open("app.html")
def search():
      text, ok = QInputDialog.getText(w, 'Search Input bar', 'Enter what you want to search from internet:')
      if ok:
         webbrowser.open("https://www.google.com/search?q=" + text)

def pratham():
      label3.show()
      btn7.hide(),btn8.hide(),btn9.hide(),btn10.hide()
      btnpra = QPushButton(w)
      btnpra.setGeometry
      btnpra.setText("LOOKING AFTER YOURSELF")
      btnpra.setGeometry(410,200,220,50)
      btnpra.setStyleSheet('''QPushButton {
    background-color: skyblue;
    color: red;
    border-style: inset;
    padding: 2px;
    font: bold 14px;
    border-color:  #4B0082;
    border-width: 6px;
    border-radius: 10px;
}
QPushButton:hover {
    background-color: #FF1493;
    color: Cyan;
    border-width: 4px;
    border-radius: 8px;
}''')
      def look1():
            label3.hide()
            labellook = QLabel(w)
            labellook.setText('''
(a) DUTIES AT HOUSE                          (c) Health rules regarding personal cleaniness
Maintaining a neat bedroom                        Brushing teeth twice a day
taking care of pets                                      Bathing regularly.
Folding and putting away clean clothes         Washing hair once in a week.
Vacuuming, sweeping, dusting                     Train your nails.
Feeding my brothers and sisters                  wearing clean and tidy clothes daily.
cookin and main help to parents.                 Wash you hands regularly
                                                                 Prefere hygine good.
(b) Be able to make your bed.
clear the bed.
Put the fitted sheet on.
Put the top sheet on.
Make hospital corners.
Fold the top sheet and duvet down.
Fluff the pillows.
Adding the finishing touches.
                        
''')
            labellook.setGeometry(10,140,900,510)
            labellook.setStyleSheet("font-style:bold;font-size:20px;color:red;background-color:lightgreen; border: 5px solid voilet")
            labellook.show()
            btnlook = QPushButton(w)
            btnlook.setText("GO BACK")
            btnlook.setGeometry(900,50,120,20)
            def backpra():
                  btnlook.hide()
                  labellook.hide()
                  pratham()
            btnlook.clicked.connect(backpra)
            btnlook.show()
      btnpra.clicked.connect(look1)
      btnpra.show()
      btnpra1 = QPushButton(w)
      btnpra1.setText("B.P EXERCISE")
      btnpra1.setGeometry(410,250,220,50)
      btnpra1.setStyleSheet('''QPushButton {
    background-color: skyblue;
    color: red;
    border-style: inset;
    padding: 2px;
    font: bold 16px;
    border-color:  #4B0082;
    border-width: 6px;
    border-radius: 10px;
}
QPushButton:hover {
    background-color: #FF1493;
    color: Cyan;
    border-width: 4px;
    border-radius: 8px;
}''')
      #btnpra1.setStyleSheet("font-style:bold;font-size:20px; color:red;background-color:skyblue;")
      def bp():
            labelbp = QLabel(w)
            labelbp.setPixmap(QPixmap('bpsix.jpg'))
            labelbp.setGeometry(10,140,720,480)
            labelbp.show()
            btnbp = QPushButton(w)
            btnbp.setText("ABOUT THE EXCERSIE")
            btnbp.setGeometry(800,200,180,60)
            btnbp.setStyleSheet("font-style:bold; font-size:15px; color:yellow ;background-color:blue;")
            btnbp.show()
            btnbp1 = QPushButton(w)
            btnbp1.setText("GO BACK")
            btnbp1.setGeometry(900,50,120,20)
            def bpback():
                  btnbp1.hide()
                  labelbp.hide(), btnbp.hide()
                  pratham()
            btnbp1.clicked.connect(bpback)
            btnbp1.show()
            def bpex():
                  webbrowser.open("bpe2.html")
            btnbp.clicked.connect(bpex)
      btnpra1.clicked.connect(bp)
      btnpra1.show()
      btnpra2 = QPushButton(w)
      btnpra2.setText("DISCIPLINE")
      btnpra2.setStyleSheet('''QPushButton {
    background-color: skyblue;
    color: red;
    border-style: inset;
    padding: 2px;
    font: bold 16px;
    border-color:  #4B0082;
    border-width: 6px;
    border-radius: 10px;
}
QPushButton:hover {
    background-color: #FF1493;
    color: Cyan;
    border-width: 4px;
    border-radius: 8px;
}''')
      #btnpra2.setStyleSheet("font-style:bold;font-size:20px; color:red;background-color:skyblue;")
      btnpra2.setGeometry(410,300,220,50)
      btnpra2.show()
      def displ():
            buttondis = QPushButton(w)
            buttondis.setText("Next page")
            buttondis.setGeometry(870,20,120,20)
            def disp2():
                  buttondis.setText("Prev page")
                  labeldis.setText('''PATROL YELL:
The patrol yell is a distinctive shout or cheer used by a 
patrol in the scouting movement. It is used to show unity and spirit among the members of the 
patrol. The yell is usually created by the patrol members themselves and can be based on their 
patrol name

PATROL CORNER: Each patrol is given a place or a corner at institute. It should be a peace full
place where the members of the patrol set together and discuss..
                                   
PATROL IN COUNCIL: it is a system used to organize small groups of scouts within a troop. 
Each patrol is led by a patrol leader and is responsible for its own activities and internal 
organization. The patrol method is designed to encourage teamwork, leadership, and self-sufficiency among scoutS''')
                  buttondis.show
                  buttondis.clicked.connect(displ)
            buttondis.clicked.connect(disp2)
            buttondis.show()
            labeldis = QLabel(w)
            labeldis.setText('''PATROL NAME:
The name you choose should be representative of your patrol’s
spirit and it’s members. It can be one word or phrase and should
 be a name that you’ll be proud of. 

PATROL FLAG: The flag is the heart and sould of any patrol. Second
to its members. of course. To create an amazing patrol flag, select 
a durable material (like fabric) on which you can create a design.
On flag following things must be there.
- Your patrol name
- Your troop number
- Your patrol logo
- Your member names(in banner)

Patrol call: A patrol call is a signal used by a patrol to identify
itself and to communicate with other patrols. It is usually a 
whistle or a bugle call that is unique to the patrol. The patrol call
is used to signal the start of a patrol meeting, to call the patrol 
together, or to signal the end of a patrol activity.''')
            labeldis.setGeometry(10,140,900,510)
            labeldis.setStyleSheet("font-style:bold;font-size:20px;color:red;background-color:lightgreen; border: 5px solid voilet")
            labeldis.show()
            buttondisback = QPushButton(w)
            buttondisback.setText("GO BACK")
            buttondisback.setGeometry(890,80,120,20)
            def btndisback():
                  labeldis.hide(),buttondis.hide(),buttondisback.hide()
                  pratham()
            buttondisback.clicked.connect(btndisback)
            buttondisback.show()
      btnpra2.clicked.connect(displ)
      btnpra3 = QPushButton(w)
      btnpra3.setText("HAND AND WHISTLE SIGNALS")
      btnpra3.setStyleSheet('''QPushButton {
    background-color: skyblue;
    color: red;
    border-style: inset;
    padding: 2px;
    font: bold 14px;
    font-size:13px;
    border-color: #4B0082;
    border-width: 6px;
    border-radius: 10px;
}
QPushButton:hover {
    background-color: #FF1493;
    color: Cyan;
    border-width: 4px;
    border-radius: 8px;
}''')
      #btnpra3.setStyleSheet("font-style:bold;font-size:15px; color:red;background-color:skyblue;")
      btnpra3.setGeometry(410,350,220,50)
      def handandwhis():
            webbrowser.open("handsignal.html")
      btnpra3.clicked.connect(handandwhis)
      btnpra3.show()
      btnpra4 = QPushButton(w)
      btnpra4.setText("KNOTS AND LASHING")
      btnpra4.setGeometry(410,400,220,50)
      btnpra4.setStyleSheet('''QPushButton {
    background-color: skyblue;
    color: red;
    border-style: inset;
    padding: 2px;
    font: bold 16px;
    border-color:  #4B0082;
    border-width: 6px;
    border-radius: 10px;
}
QPushButton:hover {
    background-color: #FF1493;
    color: Cyan;
    border-width: 4px;
    border-radius: 8px;
}''')
      #btnpra4.setStyleSheet("font-style:bold;font-size:20px; color:red;background-color:skyblue;")
      def knots():
            webbrowser.open("knots.html")
      btnpra4.clicked.connect(knots)
      btnpra4.show() 
      btnpra5 = QPushButton(w)
      btnpra5.setText("FIRST AID")
      btnpra5.setGeometry(410,450,220,50)
      btnpra5.setStyleSheet('''QPushButton {
    background-color: skyblue;
    color: red;
    border-style: inset;
    padding: 2px;
    font: bold 16px;
    border-color:  #4B0082;
    border-width: 6px;
    border-radius: 10px;
}
QPushButton:hover {
    background-color: #FF1493;
    color: Cyan;
    border-width: 4px;
    border-radius: 8px;
}''')
      #btnpra5.setStyleSheet("font-style:bold;font-size:20px; color:red;background-color:skyblue;")
      btnpra5.show()
      def firstaid():
            webbrowser.open("firstaid.html")
      btnpra5.clicked.connect(firstaid)
      btnbackpra = QPushButton(w)
      btnbackpra.setText("GO BACK")
      btnbackpra.setGeometry(410,530,220,50)
      btnbackpra.setStyleSheet("font-style:bold;font-size:23px; color:white;background-color:purple;")
      btnbackpra.show()
      def backpra():
            print("argv: ", sys.argv)
            print("sys executable: " , sys.executable)
            os.execv(sys.executable,['python'] + sys.argv)
      btnbackpra.clicked.connect(backpra)

def dwitya():
      btn.hide(),btn2.hide(),btn3.hide(),btn4.hide(),btn5.hide(),btn6.hide(),btn7.hide()
      btn8.hide(),btn9.hide(),btn10.hide()
      btndwi = QPushButton(w)
      btndwi.setText("TOOLS HANDLING")
      btndwi.setStyleSheet('''QPushButton {
    background-color: #32CD32;
    color: black;
    border-style: inset;
    padding: 2px;
    font: bold 16px;
    border-color: gray;
    border-width: 6px;
    border-radius: 10px;
}
QPushButton:hover {
    background-color: #FF1493;
    color: Cyan;
    border-width: 4px;
    border-radius: 8px;
}''')
      #btndwi.setStyleSheet("font-style:bold;font-size:20px; color:red;background-color:skyblue;")
      btndwi.setGeometry(410,200,220,50)
      def tools():
            webbrowser.open("tools.html")
      btndwi.clicked.connect(tools)
      btndwi.show()
      btndwi2 = QPushButton(w)
      btndwi2.setText("FIRE")
      btndwi2.setStyleSheet('''QPushButton {
    background-color: #32CD32;
    color: black;
    border-style: inset;
    padding: 2px;
    font: bold 16px;
    border-color: gray;
    border-width: 6px;
    border-radius: 10px;
}
QPushButton:hover {
    background-color: #FF1493;
    color: Cyan;
    border-width: 4px;
    border-radius: 8px;
}''')
     # btndwi2.setStyleSheet("font-style:bold;font-size:20px; color:red;background-color:skyblue;")
      btndwi2.setGeometry(410,250,220,50)
      def fire():
            webbrowser.open("https://www.scouterlife.com/blog/2019/2/7/nine-different-types-of-fires")
      btndwi2.clicked.connect(fire)
      btndwi2.show()

      btndwi3 = QPushButton(w)
      btndwi3.setText("COOKING")
      btndwi3.setGeometry(410,300,220,50)
      btndwi3.setStyleSheet('''QPushButton {
    background-color: #32CD32;
    color: black;
    border-style: inset;
    padding: 2px;
    font: bold 16px;
    border-color: gray;
    border-width: 6px;
    border-radius: 10px;
}
QPushButton:hover {
    background-color: #FF1493;
    color: Cyan;
    border-width: 4px;
    border-radius: 8px;
}''')
      #btndwi3.setStyleSheet("font-style:bold;font-size:20px; color:red;background-color:skyblue;")
      def cook():
            webbrowser.open("cook.html")
      btndwi3.clicked.connect(cook)
      btndwi3.show()
      
      btndwi4 = QPushButton(w)
      btndwi4.setText("COMPASS")
      btndwi4.setGeometry(410,350,220,50)
      btndwi4.setStyleSheet('''QPushButton {
    background-color: #32CD32;
    color: black;
    border-style: inset;
    padding: 2px;
    font: bold 16px;
    border-color: gray;
    border-width: 6px;
    border-radius: 10px;
}
QPushButton:hover {
    background-color: #FF1493;
    color: Cyan;
    border-width: 4px;
    border-radius: 8px;
}''')
      #btndwi4.setStyleSheet("font-style:bold;font-size:20px; color:red;background-color:skyblue;")
      def comp():
            webbrowser.open("compass.html")
      btndwi4.clicked.connect(comp)
      btndwi4.show()

      btndwi5 = QPushButton(w)
      btndwi5.setText("CONSTELLATIONS")
      btndwi5.setGeometry(410,400,220,50)
      btndwi5.setStyleSheet('''QPushButton {
    background-color: #32CD32;
    color: black;
    border-style: inset;
    padding: 2px;
    font: bold 16px;
    border-color: gray;
    border-width: 6px;
    border-radius: 10px;
}
QPushButton:hover {
    background-color: #FF1493;
    color: Cyan;
    border-width: 4px;
    border-radius: 8px;
}''')
      #btndwi5.setStyleSheet("font-style:bold;font-size:20px; color:red;background-color:skyblue;")
      def constel():
            webbrowser.open("conste.html")
      btndwi5.clicked.connect(constel)
      btndwi5.show()

      btndwi6 = QPushButton(w)
      btndwi6.setText("MAPPING")
      btndwi6.setGeometry(410,450,220,50)
      btndwi6.setStyleSheet('''QPushButton {
    background-color: #32CD32;
    color: black;
    border-style: inset;
    padding: 2px;
    font: bold 16px;
    border-color: gray;
    border-width: 6px;
    border-radius: 10px;
}
QPushButton:hover {
    background-color: #FF1493;
    color: Cyan;
    border-width: 4px;
    border-radius: 8px;
}''')
      #btndwi6.setStyleSheet("font-style:bold;font-size:20px; color:red;background-color:skyblue;")
      def mapping():
            webbrowser.open("map.html")
      btndwi6.clicked.connect(mapping)
      btndwi6.show()

      btndwi7 = QPushButton(w)
      btndwi7.setText("ESITMATION")
      btndwi7.setGeometry(410,500,220,50)
      btndwi7.setStyleSheet('''QPushButton {
    background-color: #32CD32;
    color: black;
    border-style: inset;
    padding: 2px;
    font: bold 16px;
    border-color: gray;
    border-width: 6px;
    border-radius: 10px;
}
QPushButton:hover {
    background-color: #FF1493;
    color: Cyan;
    border-width: 4px;
    border-radius: 8px;
}''')
      #btndwi7.setStyleSheet("font-style:bold;font-size:20px; color:red;background-color:skyblue;")
      def esti():
            webbrowser.open("estim.html")
      btndwi7.clicked.connect(esti)
      btndwi7.show()

      btndwi8 = QPushButton(w)
      btndwi8.setText("IMPORTANT ACTIVITY")
      btndwi8.setGeometry(410,550,220,50)
      btndwi8.setStyleSheet('''QPushButton {
    background-color: #32CD32;
    color: black;
    border-style: inset;
    padding: 2px;
    font: bold 16px;
    border-color: gray;
    border-width: 6px;
    border-radius: 10px;
}
QPushButton:hover {
    background-color: #FF1493;
    color: Cyan;
    border-width: 4px;
    border-radius: 8px;
}''')
      #btndwi8.setStyleSheet("font-style:bold;font-size:20px; color:red;background-color:skyblue;")
      def act():
            webbrowser.open("act.html")
      btndwi8.clicked.connect(act)
      btndwi8.show()

      btnbackdwi = QPushButton(w)
      btnbackdwi.setText("GO BACK")
      btnbackdwi.setGeometry(840,70,130,50)
      btnbackdwi.setStyleSheet("font-style:bold;font-size:23px; color:white;background-color:purple;")
      btnbackdwi.show()
      def backpra():
            print("argv: ", sys.argv)
            print("sys executable: " , sys.executable)
            os.execv(sys.executable,['python'] + sys.argv)
      btnbackdwi.clicked.connect(backpra)

def tritya():
      btn.hide(),btn2.hide(),btn3.hide(),btn4.hide(),btn5.hide()
      btn6.hide(),btn7.hide(),btn8.hide(),btn9.hide(),btn10.hide()
      btntri = QPushButton(w)
      btntri.setText("CAMPING")
      btntri.setGeometry(410,200,220,50)
      btntri.setStyleSheet('''QPushButton {
    background-color: skyblue;
    color: red;
    border-style: inset;
    padding: 2px;
    font: bold 16px;
    border-color: #00008B;
    border-width: 6px;
    border-radius: 10px;
}
QPushButton:hover {
    background-color: red;
    color: Cyan;
    border-width: 4px;
    border-radius: 8px;
}''')
      #btntri.setStyleSheet("font-style:bold;font-size:20px; color:red;background-color:skyblue;")
      def camp():
            webbrowser.open("camp.html")
      btntri.clicked.connect(camp)
      btntri.show()

      btntri2 = QPushButton(w)
      btntri2.setText("ESTIMATION")
      btntri2.setGeometry(410,250,220,50)
      btntri2.setStyleSheet('''QPushButton {
    background-color: skyblue;
    color: red;
    border-style: inset;
    padding: 2px;
    font: bold 16px;
    border-color:  #00008B;
    border-width: 6px;
    border-radius: 10px;
}
QPushButton:hover {
    background-color: red;
    color: Cyan;
    border-width: 4px;
    border-radius: 8px;
}''')
      #btntri2.setStyleSheet("font-style:bold;font-size:20px; color:red;background-color:skyblue;")
      def estii():
            webbrowser.open("estim.html")
      btntri2.clicked.connect(estii)
      btntri2.show()

      btntri3 = QPushButton(w)
      btntri3.setText("First Aid II")
      btntri3.setGeometry(410,300,220,50)
      btntri3.setStyleSheet('''QPushButton {
    background-color: skyblue;
    color: red;
    border-style: inset;
    padding: 2px;
    font: bold 16px;
    border-color:  #00008B;
    border-width: 6px;
    border-radius: 10px;
}
QPushButton:hover {
    background-color: red;
    color: Cyan;
    border-width: 4px;
    border-radius: 8px;
}''')
      #btntri3.setStyleSheet("font-style:bold;font-size:20px; color:red;background-color:skyblue;")
      def firstaid2():
            webbrowser.open("firstaid.html")
      btntri3.clicked.connect(firstaid2)
      btntri3.show()

      btntri4 = QPushButton(w)
      btntri4.setText("MAPPING II")
      btntri4.setGeometry(410,350,220,50)
      btntri4.setStyleSheet('''QPushButton {
    background-color: skyblue;
    color: red;
    border-style: inset;
    padding: 2px;
    font: bold 16px;
    border-color:  #00008B;
    border-width: 6px;
    border-radius: 10px;
}
QPushButton:hover {
    background-color: red;
    color: Cyan;
    border-width: 4px;
    border-radius: 8px;
}''')
      #btntri4.setStyleSheet("font-style:bold;font-size:20px; color:red;background-color:skyblue;")
      def mapp2():
            webbrowser.open("map2.html")
      btntri4.clicked.connect(mapp2)
      btntri4.show()

      btntri5 = QPushButton(w)
      btntri5.setText("SIGNALLING")
      btntri5.setGeometry(410,400,220,50)
      btntri5.setStyleSheet('''QPushButton {
    background-color: skyblue;
    color: red;
    border-style: inset;
    padding: 2px;
    font: bold 16px;
    border-color:  #00008B;
    border-width: 6px;
    border-radius: 10px;
}
QPushButton:hover {
    background-color: red;
    color: Cyan;
    border-width: 4px;
    border-radius: 8px;
}''')
      #btntri5.setStyleSheet("font-style:bold;font-size:20px; color:red;background-color:skyblue;")
      def signal():
            btntri.hide(),btntri2.hide(),btntri3.hide(),btntri4.hide(),btntri5.hide()
            label3.hide()
            labelsig = QLabel(w)
            labelsig.setText('''SIGNALLING
---Learn Morse signalling and be able to send and receive simple massages of ten words..
 and flag signalling...''')
            labelsig.setGeometry(10,100,900,100)
            labelsig.setStyleSheet("font-style:bold;font-size:20px;color:red;background-color:lightgreen; border: 5px solid voilet")
            labelsig.show()
            img = QLabel(w)
            img.setPixmap(QPixmap('morse.png'))
            img.setGeometry(10,200,283,178)
            img.show()

            img2 = QLabel(w)
            img2.setPixmap(QPixmap('signalflag.jpg'))
            img2.setGeometry(290,200,700,500)
            img2.show()

            btnbacksign = QPushButton(w)
            btnbacksign.setGeometry(840,70,130,50)
            btnbacksign.setText("GO BACK")
            btnbacksign.setStyleSheet("font-style:bold;font-size:23px; color:white;background-color:purple;")
            btnbacksign.show()
            def backsign():
                  labelsig.hide(),img.hide(),img2.hide(),btnbacksign.hide()
                  tritya()
            btnbacksign.clicked.connect(backsign)

      btntri5.clicked.connect(signal)
      btntri5.show()
      btntri6 = QPushButton(w)
      btntri6.setText("IMPORTANT ACTIVITY")
      btntri6.setGeometry(410,450,220,50)
      btntri6.setStyleSheet('''QPushButton {
    background-color: skyblue;
    color: red;
    border-style: inset;
    padding: 2px;
    font: bold 16px;
    border-color: #00008B;
    border-width: 6px;
    border-radius: 10px;
}
QPushButton:hover {
    background-color: red;
    color: Cyan;
    border-width: 4px;
    border-radius: 8px;
}''')
      def imp2():
            webbrowser.open("act2.html")
      btntri6.clicked.connect(imp2)
      btntri6.show()

      btnbacktri = QPushButton(w)
      btnbacktri.setText("GO BACK")
      btnbacktri.setGeometry(840,70,130,50)
      btnbacktri.setStyleSheet("font-style:bold;font-size:23px; color:white;background-color:purple;")
      btnbacktri.show()
      def backtri():
            print("argv: ", sys.argv)
            print("sys executable: " , sys.executable)
            os.execv(sys.executable,['python'] + sys.argv)
      btnbacktri.clicked.connect(backtri)

def rajya():
      btn.hide(),btn2.hide(),btn3.hide(),btn4.hide(),btn5.hide()
      btn6.hide(),btn7.hide(),btn8.hide(),btn9.hide(),btn10.hide()
      btnraj = QPushButton(w)
      btnraj.setText("PIONEERING PROJECT")
      btnraj.setGeometry(410,200,220,50)
      btnraj.setStyleSheet('''QPushButton {
    background-color: #CD5C5C;
    color: black;
    border-style: outset;
    padding: 2px;
    font: bold 18px;
    border-width: 6px;
    border-radius: 10px;
    border-color: gray;
}
QPushButton:hover {
    background-color: #ADFF2F;
    color: #FF1493;
    border-style: inset;
    border-width: 4px;
    border-radius: 8px;
}''')
      btnraj.show()
      def raj2():
            webbrowser.open("pioneerpro.pdf")
      btnraj.clicked.connect(raj2)
      btnraj3 = QPushButton(w)
      btnraj3.setText("CAMP CRAFT")
      btnraj3.setStyleSheet('''QPushButton {
    background-color: #CD5C5C;
    color: black;
    border-style: outset;
    padding: 2px;
    font: bold 16px;
    border-width: 6px;
    border-radius: 10px;
    border-color: gray;
}
QPushButton:hover {
    background-color: #ADFF2F;
    color: #FF1493;
    border-style: inset;
    border-width: 4px;
    border-radius: 8px;
}''')
      btnraj3.setGeometry(410,250,220,50)
      def raj4():
            webbrowser.open("campcraft.pdf")
      btnraj3.clicked.connect(raj4)
      btnraj3.show()
      btnraj2 = QPushButton(w)
      btnraj2.setText("IMPORTANT ACTIVITIES")
      btnraj2.setStyleSheet('''QPushButton {
    background-color: #CD5C5C;
    color: black;
    border-style: outset;
    padding: 2px;
    font: bold 16px;
    border-width: 6px;
    border-radius: 10px;
    border-color: gray;
}
QPushButton:hover {
    background-color: #ADFF2F;
    color: #FF1493;
    border-style: inset;
    border-width: 4px;
    border-radius: 8px;
}''')
      btnraj2.setGeometry(410,300,220,50)
      btnraj2.show()
      def raj3():
            webbrowser.open("raj2.html")
      btnraj2.clicked.connect(raj3)

      btnbacktri2 = QPushButton(w)
      btnbacktri2.setText("GO BACK")
      btnbacktri2.setGeometry(840,70,130,50)
      btnbacktri2.setStyleSheet("font-style:bold;font-size:23px; color:white;background-color:purple;")
      btnbacktri2.show()
      def backtri():
            print("argv: ", sys.argv)
            print("sys executable: " , sys.executable)
            os.execv(sys.executable,['python'] + sys.argv)
      btnbacktri2.clicked.connect(backtri)

def rashtra():
      btn.hide(),btn2.hide(),btn3.hide(),btn4.hide(),btn5.hide()
      btn6.hide(),btn7.hide(),btn8.hide(),btn9.hide(),btn10.hide()
      btnrash = QPushButton(w)
      btnrash.setText("MAIN WEB")
      btnrash.setGeometry(330,250,400,300)
      btnrash.setStyleSheet('''QPushButton {
    background-color: gold;
    color: black;
    border-style: outset;
    padding: 2px;
    font: bold 16px;
    border-width: 6px;
    border-radius: 10px;
    border-color: gray;
}
QPushButton:hover {
    background-color: #ADFF2F;
    color: #FF1493;
    border-style: inset;
    border-width: 4px;
    border-radius: 8px;
}''')
      btnrash.show()
      def rash2():
            webbrowser.open("rash.html")
      btnrash.clicked.connect(rash2)

      btnbacktri3 = QPushButton(w)
      btnbacktri3.setText("GO BACK")
      btnbacktri3.setGeometry(840,70,130,50)
      btnbacktri3.setStyleSheet("font-style:bold;font-size:23px; color:white;background-color:purple;")
      btnbacktri3.show()
      def backtri():
            print("argv: ", sys.argv)
            print("sys executable: " , sys.executable)
            os.execv(sys.executable,['python'] + sys.argv)
      btnbacktri3.clicked.connect(backtri)

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(300,300)
    w.setWindowTitle("THE BHARATH SCOUTS AND GUIDS")
    wsize = 1000
    hsize = 740
    w.setFixedWidth(wsize)
    w.setFixedHeight(hsize)
    label = QLabel(w)
    label.setPixmap(QPixmap('intro2.jpg'))
    label.resize(900,900)
    label.setGeometry(0,0,1600,739)
    #label.setGeometry(0,0,1600,739)
    label.show()

    label2 = QLabel(w)
    label2.setText("THE BHARAT SCOUTS AND GUIDES")
    font = label2.font()
    font.setPointSize(30)
    label2.setFont(font)
    label2.move(190,10)
    label2.setStyleSheet("font-style: italic; color:white ;background-color: darkgreen;  border: 5px solid darkorange;")
    label2.show()

    label3 = QLabel(w)
    label3.setText("SELECT ONE OPTION")
    font.setPointSize(30)
    label3.setFont(font)
    label3.move(320,70)
    label3.setStyleSheet("font-style: normal; color:white ;background-color: purple;  border: 5px solid darkorange;")
    label3.show()
    
    btn = QPushButton(w)
    btn.setText('PRAVESH')
    #btn.move(450,130)
    btn.setGeometry(410,200,220,50)
    btn.setStyleSheet('''QPushButton {
    background-color: #FF6347;
    color: black;
    border-style: outset;
    padding: 2px;
    font: bold 20px;
    border-width: 6px;
    border-radius: 10px;
    border-color: gray;
}
QPushButton:hover {
    background-color: #00FFFF;
    color: #FF1493;
    border-style: inset;
    border-width: 4px;
    border-radius: 8px;
}''')
    #btn.setStyleSheet("font-style:bold;font-size:20px; color:red;background-color:#F4C430;")
    btn.show()
    btn.clicked.connect(pravesh)


    btn2 = QPushButton(w)
    btn2.setText('PRATHAM SOPAN')
    btn2.setGeometry(410,250,220,50)
    btn2.setStyleSheet('''QPushButton {
    background-color: #FF6347;
    color: black;
    border-style: outset;
    padding: 2px;
    font: bold 20px;
    border-width: 6px;
    border-radius: 10px;
    border-color: gray;
}
QPushButton:hover {
    background-color: #00FFFF;
    color: #FF1493;
    border-style: inset;
    border-width: 4px;
    border-radius: 8px;
}''')
    #btn2.setStyleSheet("font-style:bold;font-size:20px; color:red;background-color:#F4C430")
    btn2.show()
    btn2.clicked.connect(pratham)
    
    btn3 = QPushButton(w)
    btn3.setText('DWITHIYA SOPAN')
    btn3.setGeometry(410,300,220,50)
    btn3.setStyleSheet('''QPushButton {
    background-color: white;
    color: black ;
    border-style: outset;
    padding: 2px;
    font: bold 20px;
    border-width: 6px;
    border-radius: 10px;
    border-color: gray;
}
QPushButton:hover {
    background-color: #00FFFF;
    color: #FF1493;
    border-style: inset;
    border-width: 4px;
    border-radius: 8px;
}''')
    #btn3.setStyleSheet("font-style:bold;font-size:20px; color:#000080;background-color:white")
    btn3.clicked.connect(dwitya)
    btn3.show()

    btn4 = QPushButton(w)
    btn4.setText('TRITHIYA SOPAN')
    #btn.move(450,130)
    btn4.setGeometry(410,350,220,50)
    btn4.setStyleSheet('''QPushButton {
    background-color: white;
    color: black ;
    border-style: outset;
    padding: 2px;
    font: bold 20px;
    border-width: 6px;
    border-radius: 10px;
    border-color: gray;
}
QPushButton:hover {
    background-color: #00FFFF;
    color: #FF1493;
    border-style: inset;                   
    border-width: 4px;
    border-radius: 8px;
}''')
    #btn4.setStyleSheet("font-style:bold;font-size:20px; color:#000080;background-color:white; ")
    btn4.clicked.connect(tritya)
    btn4.show()

    btn5 = QPushButton(w)
    btn5.setText('RAJYAPURASKAR')
    #btn.move(450,130)
    btn5.setGeometry(410,400,220,50)
    btn5.setStyleSheet('''QPushButton {
    background-color: green;
    color: black ;
    border-style: outset;
    padding: 2px;
    font: bold 20px;
    border-width: 6px;
    border-radius: 10px;
    border-color: gray;
}
QPushButton:hover {
    background-color: #00FFFF;
    color: #FF1493;
    border-style: inset;                   
    border-width: 4px;
    border-radius: 8px;
}''')
    #btn5.setStyleSheet("font-style:bold;font-size:20px; color:red;background-color:green ")
    btn5.show()
    btn5.clicked.connect(rajya)

    btn6 = QPushButton(w)
    btn6.setText('RASHTRAPATHI AWARD')
    #btn.move(450,130)
    btn6.setGeometry(410,450,220,50)
    btn6.setStyleSheet('''QPushButton {
    background-color: green;
    color: black ;
    border-style: outset;
    padding: 2px;
    font: bold 16px;
    border-color: gray;
    border-width: 6px;
    border-radius: 10px;
}
QPushButton:hover {
    background-color: #00FFFF;
    color: #FF1493;
    border-style: inset;                   
    border-width: 4px;
    border-radius: 8px;
}''')
    #btn6.setStyleSheet("font-style:bold;font-size:20px; color:red;background-color:green; ")
    btn6.clicked.connect(rashtra)
    btn6.show()

    btn10 = QPushButton(w)
    btn10.setText("APRO pdf")
    btn10.setGeometry(410,530,220,50)
    btn10.setStyleSheet('''QPushButton {
    background-color: #32CD32;
    color: black;
    border-style: inset;
    padding: 2px;
    font: bold 16px;
    border-color: gray;
    border-width: 6px;
    border-radius: 10px;
}
QPushButton:hover {
    background-color: #00FFFF;
    color: Black;
    border-style: inset;                    
    border-width: 4px;
    border-radius: 8px;
}''')
    #btn10.setStyleSheet("font-style:bold;font-size:20px;color:red;background-color:lightgreen; border: 5px solid voilet")
    btn10.show()
    def apro():
          webbrowser.open("apro.pdf")
    btn10.clicked.connect(apro)

    btn7 = QPushButton(w)
    btn7.setText('ABOUT THE APP')
    #btn.move(450,130)
    btn7.setGeometry(100,600,220,50)
    btn7.setStyleSheet("font-style:bold;font-size:20px; color:red;background-color:grey")
    btn7.show()
    def about():
          webbrowser.open("https://github.com/keerthiherer/Scouts-and-Guides")
          text, ok = QInputDialog.getText(w, 'Easter egg Input bar', 'Enter the word similar to founder of this app GKB or LBP:')
          if ok:
            if text == "GKB":
               webbrowser.open("https://gkbeasteregg.blogspot.com/2023/09/jamboree.html")
            else: 
                  print("try again")
                  print("argv: ", sys.argv)
                  print("sys executable: " , sys.executable)
                  os.execv(sys.executable,['python'] + sys.argv)
    btn7.clicked.connect(about)

    btn8 = QPushButton(w)
    btn8.setText('ABOUT THE DEVELOPER')
    #btn.move(450,130)
    btn8.setGeometry(700,600,220,50)
    btn8.setStyleSheet("font-style:bold;font-size:20px; color:red;background-color:grey")
    btn8.show()
    btn8.clicked.connect(sound)

    btn9 = QPushButton(w)
    btn9.setText("SEARCH ENGINE")
    btn9.setGeometry(400,600,220,50)
    btn9.setStyleSheet("font-style:bold;font-size:20px; color:red;background-color:grey")
    btn9.show()
    btn9.clicked.connect(search)
    
    
    w.show()
    sys.exit(app.exec_())