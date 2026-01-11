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
        La=qtw.QLabel("pick something")
        self.layout().addWidget(La)
        #change font size
        La.setFont(qtg.QFont("bold",40))

        #combo box
        Co=qtw.QComboBox(self,
                         editable=True,
                         insertPolicy=qtw.QComboBox.InsertAtTop)
        #add items
        Co.addItem("curd","somthing")
        Co.addItem("paneer",2)
        Co.addItem("cheese",qtw.QWidget)
        Co.addItem("milk")
        Co.addItems(["one","two","three"])
        Co.insertItem(2,"3 thing")
        Co.insertItems(3,['1','23','34','67'])
        #put combo box to the screen
        self.layout().addWidget(Co)

        #button

        bu=qtw.QPushButton("click mee",clicked=lambda:pree())
        self.layout().addWidget(bu)



        #show the app
        self.show()



        def pree():
            #add name to table
            #La.setText(f"you picked {Co.currentText()}")
            #La.setText(f"you picked {Co.currentData()}")
            La.setText(f"you picked {Co.currentIndex()}")
            # La.setText(f"you picked {Co.text()}")
            
            
            
            
app=qtw.QApplication([])
mw=main()

#run the app
app.exec_()