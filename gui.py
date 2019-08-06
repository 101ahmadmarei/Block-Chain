import sys
import signal
import time
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QDesktopWidget, QLineEdit, QFormLayout, QLabel, QPushButton, QTabWidget, QTextEdit, QMessageBox
from Block import Block
from Blockchain import Blockchain


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AcademicChain")
        self.resize(640, 480)

        # Submit tab
        self.submitLayout = QFormLayout()

        self.slblStudentID = QLabel("Student ID")
        self.submitLayout.addWidget(self.slblStudentID)
        self.stxtStudentID = QLineEdit()
        self.submitLayout.addWidget(self.stxtStudentID)

        self.slblStudentName = QLabel("Student Name")
        self.submitLayout.addWidget(self.slblStudentName)
        self.stxtStudentName = QLineEdit()
        self.submitLayout.addWidget(self.stxtStudentName)

        self.slblClassID = QLabel("Class ID")
        self.submitLayout.addWidget(self.slblClassID)
        self.stxtClassID = QLineEdit()
        self.submitLayout.addWidget(self.stxtClassID)

        self.slblClassName = QLabel("Class Name")
        self.submitLayout.addWidget(self.slblClassName)
        self.stxtClassName = QLineEdit()
        self.submitLayout.addWidget(self.stxtClassName)

        self.slblGrade = QLabel("Grade")
        self.submitLayout.addWidget(self.slblGrade)
        self.stxtGrade = QLineEdit()
        self.submitLayout.addWidget(self.stxtGrade)

        self.slblAbsences = QLabel("Absences")
        self.submitLayout.addWidget(self.slblAbsences)
        self.stxtAbsences = QLineEdit()
        self.submitLayout.addWidget(self.stxtAbsences)

        self.slblCredits = QLabel("Credits")
        self.submitLayout.addWidget(self.slblCredits)
        self.stxtCredits = QLineEdit()
        self.submitLayout.addWidget(self.stxtCredits)

        self.sBtnSubmit = QPushButton("Submit data to chain") 
        self.sBtnSubmit.clicked.connect(self.add_block)
        self.submitLayout.addWidget(self.sBtnSubmit)

        submit = QWidget()
        submit.setLayout(self.submitLayout)

        # Request tab
        self.requestLayout = QFormLayout()

        request = QWidget()
        request.setLayout(self.requestLayout)

        #Student ID Required
        self.rlblStudentID = QLabel("Student ID")
        self.requestLayout.addWidget(self.rlblStudentID)
        self.rtxtStudentID = QLineEdit()
        self.requestLayout.addWidget(self.rtxtStudentID)

        self.rBtnGPA = QPushButton("Get GPA")
        self.requestLayout.addWidget(self.rBtnGPA)
        self.rBtnGPA.clicked.connect(self.get_gpa)

        self.rBtnCredits = QPushButton("Get Credit Count")
        self.requestLayout.addWidget(self.rBtnCredits)
        self.rBtnCredits.clicked.connect(self.get_credits)

        self.rBtnStudentName = QPushButton("Get Student Name")
        self.requestLayout.addWidget(self.rBtnStudentName)
        self.rBtnStudentName.clicked.connect(self.get_student_name)

        self.rBtnStudentAttendance = QPushButton("Get Student Attendance")
        self.requestLayout.addWidget(self.rBtnStudentAttendance)
        self.rBtnStudentAttendance.clicked.connect(self.get_student_attendance)

        #Class ID required
        self.rlblClassID = QLabel("Class ID")
        self.requestLayout.addWidget(self.rlblClassID)
        self.rtxtClassID = QLineEdit()
        self.requestLayout.addWidget(self.rtxtClassID)

        self.rBtnClassAvg = QPushButton("Get Class Average")
        self.requestLayout.addWidget(self.rBtnClassAvg)
        self.rBtnClassAvg.clicked.connect(self.get_class_average)

        self.rBtnNumStudents = QPushButton("Get Student Count")
        self.requestLayout.addWidget(self.rBtnNumStudents)
        self.rBtnNumStudents.clicked.connect(self.get_num_students)

        self.rBtnClassName = QPushButton("Get Class Name")
        self.requestLayout.addWidget(self.rBtnClassName)
        self.rBtnClassName.clicked.connect(self.get_name_class)

        #Both required
        self.rlblBoth = QLabel("Both Student ID and Class ID Required")
        self.requestLayout.addWidget(self.rlblBoth)

        self.rBtnSummary = QPushButton("Get Summary")
        self.requestLayout.addWidget(self.rBtnSummary)
        self.rBtnSummary.clicked.connect(self.get_summary)

        # Info tab
        self.infoLayout = QFormLayout()

        self.btnSave = QPushButton("Save to Disk")
        self.infoLayout.addWidget(self.btnSave)
        self.btnSave.clicked.connect(self.save_to_disk)

        self.bcViewer = QTextEdit()
        self.bcViewer.setReadOnly(1)
        self.bcViewer.setFixedSize(800,400)
        self.infoLayout.addWidget(self.bcViewer)

        info = QWidget()
        info.setLayout(self.infoLayout)

        # Tabs init
        self.tab = QTabWidget()
        self.tab.addTab(submit, "Submit")
        self.tab.addTab(request, "Request")
        self.tab.addTab(info, "Stats")

        self.setCentralWidget(self.tab)

        self.show()

    def save_to_disk(self):
        f = open("saved_chain_state.txt", "w")
        f.write(str(bc))
        f.close()

    def gpa(self, gr):
        grmin=65
        grmax=96
        gpmin=1.0
        gpmax=4.0
        grspan=grmax-grmin
        gpspan=gpmax-gpmin
        scale=float(gr - grmin)/float(grspan)
        return gpmin + (scale*gpspan)

    def get_student_attendance(self):
        absenses=0
        for b in range(bc.get_length()):
            block = bc.get_block(b)
            if (block.student_id == self.rtxtStudentID.text()):
                absenses=absenses+block.absences
        msg="Student with ID "+self.rtxtStudentID.text()+" has "+str(absenses)+" absences on record"
        self.msg_box(msg)

    def get_student_name(self):
        for b in range(bc.get_length()):
            block = bc.get_block(b)
            if (block.student_id == self.rtxtStudentID.text()):
                msg="Student with ID "+self.rtxtStudentID.text()+" maps to name "+block.student_name
                self.msg_box(msg)
                break

    def get_name_class(self):
        for b in range(bc.get_length()):
            block=bc.get_block(b)
            if(block.class_id == self.rtxtClassID.text()):
                msg="Class with ID "+self.rtxtClassID.text()+" maps to name "+block.class_name
                self.msg_box(msg)
                break

    def get_num_students(self):
        num=0
        for b in range(bc.get_length()):
            block=bc.get_block(b)
            if(block.class_id==self.rtxtClassID.text()):
                num=num+1
        msg="Class with ID "+self.rtxtClassID.text()+" was taken by "+str(num)+" students"
        self.msg_box(msg)

    def get_summary(self):
        for b in range(bc.get_length()):
            block=bc.get_block(b)
            if(block.student_id == self.rtxtStudentID.text() and block.class_id == self.rtxtClassID.text()):
                msg="Query Results\nClass ID:\t"+block.class_id+"\nStudent ID:\t"+block.student_id+"\nName:\t"+block.student_name+"\nGrade:\t"+str(block.grade)+"\nGPA:\t"+str(self.gpa(block.grade))+"\nAbsences:\t"+str(block.absences)+"\nCredits:\t"+str(block.credits)
        self.msg_box(msg)
                

    def get_credits(self):
        c=0
        for b in range(bc.get_length()):
            block = bc.get_block(b)
            if (block.student_id == self.rtxtStudentID.text()):
                c=c+block.credits
        if (c>0):
            msg=self.rtxtStudentID.text()+" has "+str(c)+" credit hours"
        else:
            msg="No credit hours found for "+self.rtxtStudentID.text()
        self.msg_box(msg)
            

    def get_class_average(self):
        av=0
        div=0
        for b in range(bc.get_length()):
            block = bc.get_block(b)
            if (block.class_id == self.rtxtClassID.text()):
                av=av+block.grade
                div=div+1
        if (div>0):
            msg=self.rtxtClassID.text()+" has a class average of "+str(int(av/div))
        else:
            msg="No grades found for class with ID "+self.rtxtClassID.text()
        self.msg_box(msg)

    def get_gpa(self):
        av=0
        div=0
        for b in range(bc.get_length()):
            block = bc.get_block(b)
            if (block.student_id == self.rtxtStudentID.text()):
                av=av+block.grade
                div=div+1
        if (div>0):
            g=self.gpa(int(av/div))
            msg=self.rtxtStudentID.text()+" has a GPA of "+str(g)
        else:
            msg="No grade records found for student with ID "+self.rtxtStudentID.text()
        self.msg_box(msg)


    def clearFields(self):
        self.stxtStudentID.clear()
        self.stxtStudentName.clear()
        self.stxtClassID.clear()
        self.stxtClassName.clear()
        self.stxtGrade.clear()
        self.stxtAbsences.clear()
        self.stxtCredits.clear()

    def updateInfo(self):
        self.bcViewer.clear()
        self.bcViewer.append(str(bc))

    def add_block(self): 
        prevBlock = bc.get_block(0)
        height = prevBlock.height+1
        timestamp = int(time.time())
        prevHash = prevBlock.currHash
        data = "tmp data"
        #nonce
        difficulty = prevBlock.difficulty
        # Data from QLineEdits
        student_id = self.stxtStudentID.text()
        student_name = self.stxtStudentName.text()
        class_id = self.stxtClassID.text()
        class_name = self.stxtClassName.text()
        grade = int(self.stxtGrade.text())
        absences = int(self.stxtAbsences.text())
        credits = int(self.stxtCredits.text())
        block = Block(timestamp,prevHash,"lol",difficulty,student_id,student_name,class_id,class_name,grade,absences,credits)
        bc.add_block(block)
        print("Block added to chain")
        #print(bc)
        self.updateInfo()
        self.clearFields()

    def msg_box(self, message):
        m = QMessageBox()
        m.setText(message)
        m.exec_()
 

if __name__ == '__main__':

    bc = Blockchain()
    b = Block(0,0,"main",4,"smithe4","Ethan Smith","COMP3800","Blockchain",75,3,4)
    bc.add_block(b)
    b = Block(0,0,"main",4,"khawajas1","Shaheer Khawaja","COMP3800","Blockchain",88,1,4)
    bc.add_block(b)
    b = Block(0,0,"main",4,"neupanep","Prabha Neupane","COMP3800","Blockchain",92,2,4)
    bc.add_block(b)
    b = Block(0,0,"main",4,"smithe4","Ethan Smith","COMP3700","Computer Science 1",99,8,4)
    bc.add_block(b)
    b = Block(0,0,"main",4,"smithe4","Ethan Smith","COMP3900","Computer Science 2",60,1,4)
    bc.add_block(b)


    signal.signal(signal.SIGINT, signal.SIG_DFL)
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
