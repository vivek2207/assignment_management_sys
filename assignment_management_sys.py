
print('Welcome to student management')
students = []
student = {}
assessments=[]
assessment={}

def findstu(a):
    for student in students:
        if student['ID']==a:
            return False
    return True




def add():
    ch='Y'
    while ch:
        student = {}
        flag=1
        while flag==1:
            a = input('Please enter the student ID: ' )
            try:
                val = int(a)
                if (val>0 and findstu(a)):
                    flag=0
            except ValueError:
                print("No.. input is not a number. It's a string")
        student['ID'] = a
        student['Name'] = input('Please enter the student name: ') 
        student['Course_Name'] = input('Please enter the course: ')
        students.append(student)
        print('Thank You!')
        print('The details of the student you entered are as follows:')
        print('Student ID:', student['ID'])
        print('Student name:', student['Name'])
        print('Please enter the course:', student['Course_Name'])
        s = ' '.join(student.values())
        print('The record has been successfully added to the students.txt file.')
        with open('students.txt', 'a+') as myFile:
            myFile.write(s+'\n')
        print('Do you want to enter Details for another student (Y/N)?')
        ch=input('= ')
        while ch is not 'Y' and ch is not 'N': 
            print('Do you want to enter Details for another student (Y/N)?')
            ch=input('= ')
        if ch=='Y':
            continue
        elif ch=='N':
            menu()

def insertassignment():
    assessment = {}
    flag=1
    ch='Y'
    while flag==1:
        a = input('Please enter the student ID: ' )
        try:
            val = int(a)
            if (findstu(a) == False):
                flag=0
        except ValueError:
            print("No.. input is not a number. It's a string")


    while ch=='Y':
        assessment['ID'] = a
        assessment['Subject_code'] = input('Please enter the subject code: ')
        while True:
            assessment['a_no']=input('Please enter assessment No.: ')
            if int(assessment['a_no'])>=0:
                break
        while True:
            assessment['a_marks']=input('Please enter assessment Marks: ')
            if int(assessment['a_marks'])>=0:
                break
        assessments.append(assessment)
        print('Thank You!')
        print('The details of the student you entered are as follows:')
        print('Student ID:', assessment['ID'])
        print('Subject Code:', assessment['Subject_code'])
        print('Assessment No', assessment['a_no'])
        print('Assessment Marks', assessment['a_marks'])
        s = ' '.join(assessment.values())
        print('The record has been successfully added to the assessments.txt file.')
        with open('assessment.txt', 'a+') as myFile1:
            myFile1.write(s+'\n')
        print('Do you want to enter marks for another assessment (Y/N)?')
        ch=input('= ')
        while ch is not 'Y' and ch is not 'N': 
            print('Do you want to enter Marks for another assessment (Y/N)?')
            ch=input('= ')
        if ch=='Y':
            continue
        elif ch=='N':
            menu()

def searchstudent():
    ch='Y'
    while ch:
        flag=1
        while flag:
            a=input('Please enter the student ID you want to search assessment marks for: ')
            try:
                val = int(a)
                if findstu(a)== False:
                    flag=0
            except ValueError:
                print("No.. input is not a number. It's a string")
                
        print('Thank You')
        print('A student has been found:')
        for student in students:
            if student['ID']==a:
                print('Student ID: ', student['ID'])
                print('Student Name: ', student['Name'])
                print('Course: ', student['Course_Name'])
        print('Subject Code\tAssessment Number\tMarks')
        file1 = open('assessment.txt', 'r') 
        Lines = file1.readlines() 
        for line in Lines:
            d = {}
            ssplit = line.split(" ")
            d['ID'] = ssplit[0]
            if d['ID']==a:
                d['subject_code'] = ssplit[1]
                d['a_no'] = ssplit[2]
                d['a_marks'] = ssplit[3]
                print(d['subject_code'], end='\t\t')
                print(d['a_no'], end='\t\t\t')
                print(d['a_marks'])
                
        print('Do you want to search assessment marks for another student (Y/N)?')
        ch=input('= ')
        while ch is not 'Y' and ch is not 'N': 
            print('Do you want to search assessment marks for another student (Y/N)?')
            ch=input('= ')
        if ch=='Y':
            continue
        elif ch=='N':
            menu()

def menu():
    print('=================================================================')
    print('Welcome to the Student and Assessment Management System')
    print('<A> add details of a student.\n<I> insert assignment marks of a student\n<S> search assessment marks for a student.\n<Q> quit.')
    print('=================================================================')
    option = input('= ')
    if option == 'A':
        add()
    elif option == 'I':
        insertassignment()
    elif option == 'S':
        searchstudent()
    elif option == 'Q':
        print('Good bye')
        exit()
    else:
        while option != 'A' or option != 'I' or option != 'S':
            print('Invalid entry, enter again')
            option = input('= ')

menu()
