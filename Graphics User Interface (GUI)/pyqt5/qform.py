import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class main(qtw.QWidget):
    def __init__(self):
        super().__init__()
        #add a title
        self.setWindowTitle("Hello World")
        
        #set vertical layout
        form=qtw.QFormLayout()
        self.setLayout(form)
        
        #add widgets
        lab1=qtw.QLabel("lable 1")
        lab1.setFont(qtg.QFont("bold",30))
        f_name=qtw.QLineEdit(self)
        l_name=qtw.QLineEdit(self)

        #add rows

        form.addRow(lab1)       
        form.addRow("first name",f_name)       
        form.addRow("last name",l_name)       

        #button

        bu=qtw.QPushButton("click mee",clicked=lambda:pree())
        self.layout().addWidget(bu)



        #show the app
        self.show()



        def pree():
            #add name to table
            lab1.setText(f"hello {f_name.text()}")
            
app=qtw.QApplication([])
mw=main()

#run the app
app.exec_()