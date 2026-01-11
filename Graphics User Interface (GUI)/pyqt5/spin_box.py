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

        #spin box
        sp=qtw.QSpinBox(self,#QDoubleSpinBox used for float numbers
                        value=10,
                        maximum=100,
                        minimum=0,
                        singleStep=5,
                        prefix="#",
                        suffix="num")
        sp.setFont(qtg.QFont("bold",40))
        self.layout().addWidget(sp)
        #button

        bu=qtw.QPushButton("click mee",clicked=lambda:pree())
        self.layout().addWidget(bu)



        #show the app
        self.show()



        def pree():
            #add name to table
            La.setText(f"you pressed number:{sp.value()}")
            

app=qtw.QApplication([])
mw=main()

#run the app
app.exec_()