import dves_scan,dves_data_processing
from dves_data_processing import *
import sys
import os.path
from os import path
from datetime import datetime,date as dt
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
try:
    from PyQt5 import QtCore
    from PyQt5.QtCore import Qt,QDate,QTime
    from PyQt5.QtWidgets import QMainWindow,QApplication,QGridLayout,QLineEdit,QPushButton,QVBoxLayout,QWidget,QStackedWidget,QLabel,QMessageBox,QDialog,QComboBox,QDateEdit,QTimeEdit,QTableWidget,QTableWidgetItem
    
  
    
    
except ImportError:
   
    install('pyqt5')
   
   
    from PyQt5.QtCore import Qt
    from PyQt5.QtWidgets import QMainWindow,QApplication,QGridLayout,QLineEdit,QPushButton,QVBoxLayout,QWidget,QStackedWidget,QLabel,QMessageBox,QDialog,QComboBox
   

from functools import partial

class PageWindow(QMainWindow):
    gotoSignal = QtCore.pyqtSignal(str)

    def goto(self, name):
        self.gotoSignal.emit(name)

#-----------------------------------------------------------------------
class MainWindow(PageWindow):
    password=""
    username=""
    def __init__(self):
        super().__init__()
        #self
        self.setWindowFlags(Qt.WindowStaysOnTopHint )
        # Set some main window's properties
        self.setWindowTitle("DVES")
        
        self.setFixedSize(400, 590)
        # Set the central widget and the general layout
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        if(path.exists("reg_log.txt")):
            with open('reg_log.txt', 'r') as f:
                
                lines = f.read().splitlines()
                self.username = lines[0]
                self.password=lines[1]
        self.unm = QLineEdit(self)
        self.unm.move(100, 60)
        self.unm.resize(220,40)
        self.unm.setPlaceholderText("Username")
        self.pwd = QLineEdit(self)
        self.pwd.setEchoMode(QLineEdit.Password)
        self.pwd.move(100, 120)
        self.pwd.resize(220,40)
        self.pwd.setPlaceholderText("Password")
        self.loginButton = QPushButton("Login", self)
        self.loginButton.move(150,200)
        self.registerButton = QPushButton("Register", self)
        self.registerButton.move(150,280)
        self.loginButton.clicked.connect(self._gotoButton("logIn",self.username,self.password))
        self.registerButton.clicked.connect(self._gotoButton("Reg",self.username,self.password))

       
  
    def _gotoButton(self,button,username,password):
        def handleButton(): #why?
            if button == "logIn":
                if(str(self.pwd.text())==str(password) and self.unm.text()==username):
                    print("Logged In Successfully!")
                    #clear password text
                    self.goto("welcome")
                else:
                    QMessageBox.about(self,"Log In Failed","Wrong Credentials\nPlease Re-enter")
                    self.pwd.setText("")
            elif button== "Reg":
                
                if(username==""):
                    
                    self.goto("register")
                else:
                    QMessageBox.about(self,"Failed","Already Registered\nPlease Log In")
                    
                    
            
        return handleButton

#--------------------------------------------------------------------------------------------
class RegisterUser(PageWindow):
    def __init__(self):
        
        super().__init__()
        #self
        self.setWindowFlags(Qt.WindowStaysOnTopHint )
        # Set some main window's properties
        self.setWindowTitle("Register")
        
        self.setFixedSize(400, 590)
        # Set the central widget and the general layout
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
   
        
        self.unm = QLineEdit(self)
        self.unm.move(100, 60)
        self.unm.resize(220,40)
        self.unm.setPlaceholderText("Username")
        self.pwd = QLineEdit(self)
        self.pwd.setEchoMode(QLineEdit.Password)
        self.pwd.move(100, 120)
        self.pwd.resize(220,40)
        self.pwd.setPlaceholderText("Password")
        
        self.registerButton = QPushButton("Register", self)
        self.registerButton.move(150,200)
        self.registerButton.clicked.connect(self._gotoButton("Reg"))
        

       

    def _gotoButton(self,button):
        def handleButton(): #why?
           if button== "Reg":
                
                with open('reg_log.txt', 'w') as f:
                
                    f.write(self.unm.text()+"\n")
                    f.write(self.pwd.text())

                QMessageBox.about(self,"Success","Registered Successfully")
                self.goto("welcome")
                    
               
                    
            
        return handleButton


      
#--------------------------------------------------------------------------------------------------------

class WelcomeUser(PageWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self._createButtons()

    def initUI(self):
        self.setWindowTitle("Welcome User")
        self.setFixedSize(400, 590)
        # Set the central widget and the general layout
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
       
        

       
    """
    def goToMain(self):
        self.goto("main")
    """
 
    def _createButtons(self):
        
        self.buttons1 = {}
        buttonsLayout = QGridLayout()
        
       
        buttons1 = [
            "Entry Scan","Exit Scan","Report Generation"
        ]
        #print(buttons1[0])
        self.buttons={}
        
        i=0
        j=0
        for button in buttons1:
            #print(button,i,j)
            
            i=i+1
                
           
            self.buttons[button] = (i,j)
            
            
            
            
            
        # Create the buttons and add them to the grid layout
        for btnText, pos in self.buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(250, 60)
            
            buttonsLayout.addWidget(self.buttons[btnText], pos[0], pos[1])
        # Add buttonsLayout to the general layout
        self.generalLayout.addLayout(buttonsLayout)

        for btnText, btn in self.buttons.items():
            if(btnText=="Entry Scan"):
                btn.clicked.connect(partial(self.button_press_entry, btnText))
            if(btnText=="Exit Scan"):
                btn.clicked.connect(partial(self.button_press_exit, btnText))
            
            if(btnText=="Report Generation"):
                btn.clicked.connect(self.gotoReport)
            

     
   
     
    def gotoReport(self):
        self.goto("report")
        
    def button_press_entry(self, sub_exp):
      print("\nClicked ",sub_exp)
      text=dves_scan.scan()
      if(text!=""):
          message="Plate Number is : "+text
          QMessageBox.about(self, "Scan Successfull",message)
      flag=entry_check(text)
      if(flag==-1):
          QMessageBox.about(self, "Failure","Vehicle already Inside,Please Try Exit Scan")

      if(flag==0):
          vform=QDialog(parent=self)
          vform.setWindowTitle("Visitor Detials")
          vform.setModal(True)
          vform.v_name=QLineEdit(vform)
          vform.v_name.setPlaceholderText("Visitor Name")
          vform.flat=QLineEdit(vform)
          vform.flat.setPlaceholderText("Flat Visiting")
          vform.resize(500,400)
          vform.v_name.move(100,40)
          vform.v_name.resize(300,40)
          vform.flat.move(100,100)
          vform.flat.resize(300,40)
          vform.submit=QPushButton("Submit",vform)
          vform.submit.move(100,150)
          vform.submit.clicked.connect(lambda : vform.close() if(vis_entry_log(text,vform.v_name.text(),vform.flat.text())==1) else False )
          vform.show()
          #vis_entry_log(self.vform.v_name,name,flat)

    def button_press_exit(self,sub_exp):
      print("\nClicked ",sub_exp)
      text=dves_scan.scan()
      if(text!=""):
          message="Plate Number is : "+text
          QMessageBox.about(self, "Scan Successfull",message)
          flag=exit_log(text)
          print(flag)
          if(flag==-1):
              QMessageBox.about(self, "Failure","Vehicle already Outside,Please Try Entry Scan")
      else:
          QMessageBox.about(self, "Scan Failed","Please Try again")

#-----------------------------------------------------------------------------

class ReportGen(PageWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.createWidgets()

    def initUI(self):
        self.setWindowTitle("Report Generation")
        self.setFixedSize(400, 590)
        # Set the central widget and the general layout
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)

    def createWidgets(self):
        self.logSelector=QComboBox(self)
        self.logSelector.resize(110,40)
        self.logSelector.move(140,40)
        self.logSelector.addItem("Resident Log")
        self.logSelector.addItem("Visitor Log")
        self.datepicker=QDateEdit(self)
        self.datepicker.setCalendarPopup(True)
        self.datepicker.move(145,120)
        
        self.datepicker.setDate(dt.today())
        self.startTime=QTimeEdit(self)
        self.startTime.move(65,200)
        self.endTime=QTimeEdit(self)
        self.endTime.move(225,200)
        self.genButton=QPushButton("Generate",self)
        self.genButton.move(145,280)
        self.backButton=QPushButton("Back",self)
        self.backButton.move(145,340)
        self.backButton.clicked.connect(self.goBack)
        self.genButton.clicked.connect(self.repGen)
    def goBack(self):
        self.goto("welcome")

    def repGen(self):
        #print("Hey")
        log=self.logSelector.currentText()
        date=str(self.datepicker.date().toPyDate())
        #print(date)
        start=str(self.startTime.time().toPyTime())
        end=str(self.endTime.time().toPyTime())
        vbox=QVBoxLayout()
        table=QTableWidget()
        #print("Heyo")
        #print(log+" "+date+" "+start+" "+end)
        repList=getRepData(log,date,start,end)
        rows=len(repList)
        print(repList)
        table.setRowCount(rows+1)
        if(log=="Resident Log"):
            #print("hey")
            table.setColumnCount(4)
            table.setItem(0,0,QTableWidgetItem("Vehicle No."))
            table.setItem(0,1,QTableWidgetItem("Flat No."))
            table.setItem(0,2,QTableWidgetItem("Entry Time"))
            table.setItem(0,3,QTableWidgetItem("Exit Time"))
            table.resize(650,400)
            
        else:
            table.setColumnCount(5)
            table.setItem(0,0,QTableWidgetItem("Vehicle No."))
            table.setItem(0,1,QTableWidgetItem("Visitor Name"))
            table.setItem(0,2,QTableWidgetItem("Flat No."))
            table.setItem(0,3,QTableWidgetItem("Entry Time"))
            table.setItem(0,4,QTableWidgetItem("Exit Time"))
            table.resize(800,400)

        try:
            i=1
            j=0
            for row in repList:
                for j in range(len(row)):
                    #print(j+" "+row[j])
                    table.setItem(i,j,QTableWidgetItem(row[j]))
                i+=1
        except Exception as e:
            print(e)
        
        table.horizontalHeader().setDefaultSectionSize(155)
        table.show()
        vbox.addWidget(table)
        self.setLayout(vbox)
        
        
        
#------------------------------------------------------------------------------

class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.m_pages = {}

        self.register(MainWindow(), "main")
        self.register(WelcomeUser(), "welcome")
        self.register(RegisterUser(),"register")
        self.register(ReportGen(),"report")
        self.goto("main")

    def register(self, widget, name):
        self.m_pages[name] = widget
        self.stacked_widget.addWidget(widget)
        if isinstance(widget, PageWindow):
            widget.gotoSignal.connect(self.goto)

    @QtCore.pyqtSlot(str)
    def goto(self, name):
        if name in self.m_pages:
            widget = self.m_pages[name]
            self.stacked_widget.setCurrentWidget(widget)
            self.setWindowTitle(widget.windowTitle())
#-----------------------------------------------------------------------------------------------

def main():
    
   
        
    app = QApplication(sys.argv)
 
    view = Window()
    #wel=view.m_pages["welcome"]
    #SetupConnection(view=wel)
    view.show()
    
    #SetupConnection( view=view)
    sys.exit(app.exec())
       
       


if __name__ == "__main__" :
    main()
