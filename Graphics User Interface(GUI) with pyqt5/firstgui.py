import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class main(qtw.QWidget):
    def __init__(self):
        super().__init__()
        #add a title
        self.setWindowTitle("Hello World")
        
        #set vertical layout
        self.setLayout(qtw.QVBoxLayout())
        
        #label
        La=qtw.QLabel("hello label")
        self.layout().addWidget(La)
        #change font size
        La.setFont(qtg.QFont("bold",40))

        #entry box
        En=qtw.QLineEdit()
        En.setObjectName("name")
        En.setText("enter your name")#place holder Text
        self.layout().addWidget(En)

        #button

        bu=qtw.QPushButton("click mee",clicked=lambda:pree())
        self.layout().addWidget(bu)



        #show the app
        self.show()



        def pree():
            #add name to table
            La.setText(f"hello {En.text()}")
            #clear the box
            En.setText("")

app=qtw.QApplication([])
mw=main()

#run the app
app.exec_()