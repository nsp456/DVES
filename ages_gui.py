import ages_scan,ages_data_processing
from ages_data_processing import *
import sys
import os.path
from os import path
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
try:
    from PyQt5 import QtCore
    from PyQt5.QtCore import Qt
    from PyQt5.QtWidgets import QMainWindow,QApplication,QGridLayout,QLineEdit,QPushButton,QVBoxLayout,QWidget,QStackedWidget,QLabel,QMessageBox
   
  
    
    
except ImportError:
   
    install('pyqt5')
   
   
    from PyQt5.QtCore import Qt,QLabel
    from PyQt5.QtWidgets import QMainWindow,QApplication,QGridLayout,QLineEdit,QPushButton,QVBoxLayout,QWidget,QStackedWidget,QMessageBox
   

from functools import partial

class PageWindow(QMainWindow):
    gotoSignal = QtCore.pyqtSignal(str)

    def goto(self, name):
        self.gotoSignal.emit(name)


class MainWindow(PageWindow):
    password=""
    username=""
    def __init__(self):
        super().__init__()
        #self
        self.setWindowFlags(Qt.WindowStaysOnTopHint )
        # Set some main window's properties
        self.setWindowTitle("AGES")
        
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

class SetupConnection:
    

    def __init__(self, view):
       
        self._view = view
        # Connect signals and slots
        for btnText, btn in self._view.buttons.items():
            if(btnText=="Entry Scan"):
                btn.clicked.connect(partial(self.button_press_entry, btnText))
   
     
    def button_press_entry(self, sub_exp):
      print("\nClicked ",sub_exp)
      text=ages_scan.scan()
      flag=entry_check(text)
      if(flag==0):
          
          vis_entry_log(vno,name,flat)
        

class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.m_pages = {}

        self.register(MainWindow(), "main")
        self.register(WelcomeUser(), "welcome")
        self.register(RegisterUser(),"register")
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


def main():
    
   
        
    app = QApplication(sys.argv)
 
    view = Window()
    wel=view.m_pages["welcome"]
    SetupConnection(view=wel)
    view.show()
    
    #SetupConnection( view=view)
    sys.exit(app.exec())
       
       


if __name__ == "__main__" :
    main()
