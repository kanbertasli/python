'''
Create a Simple Student Management System
    - one student must enter their name and surname
    - a student who enter name and surname correctly should write
        'welcome' on the screen with print. The Student has the right
        to enter his/her and surname incorrectly 3 times. For more than
        3 inccorect entiries, the system shuts down and the messafe 
        'Please try again later' should be printed on the screen.
    - 5 courses should be created and those courses should be kept in a list.
        all of these lessons be taken from the user.
    - this student can take minimum of 3 and maximum of 5 lessons.
    - this student can not take less than 3 courses.
    - Otherwise the message 'You failed in class' should be returned to student
        by using return statement.
    - the student must choose one of these courses and take an exam. add the grades 
        from this course to a dictionary and keep the student's grades in this
        dictionary as midlerm, final and project grades.
            Example: {'midlerm':38, 'final':68, 'project:89'}
    - percentages for grades
        - midlerm exam: %30
        - Final exam: %50
        - Project: %20
    - determine a course passing grade according to the grades received.
        -for notes,
            - >90 AA
            - 70<grade<90 BB
            - 50<grade<70 CC
            - 30<grade<50 DD
            - grade<30 FF
    - if student has received FF, he/she should print his/her failure on screen
'''
# as I understood students already in a list. otherwise we can create 'create,update and delete user'
StudentList= ('Kanber Taşlı','Ömer Cengiz','Elif Yiğit','Fuat Beşer','Mert Çobanov')
GradesDict = {'midlerm':38,'final':68,'project':89}
EntryErrorCount=0


# check the name and sruname in list
def IsStudentInList(_name,_surname):
    IsinList=False
    for i in StudentList:
        if(_name+' '+_surname == i):
           IsinList= True
    return IsinList

# calculate grade with midlerm,final and project
def CalculateGrade(_midlerm,_final,_project):
    return int(_midlerm*0.3+_final*0.5+_project*0.2)


#let user enterde lessons
def SelectLesson():       
    LessonsList=str(input('Please enter your lessons. For Example:Math,Music,Art ; ')).split(',')
    if(len(LessonsList)<3):
        print('You failed in class.')
    elif(len(LessonsList)>5):
        print('You cannot enter lessons more then five.')
    else:
        index=0
        for i in LessonsList:
            print (str(index+1) + ':'+ i)
            index+=1
        
        LesonNo = input('Please enter the number which you want to learn grade? ')
        grade = CalculateGrade(GradesDict["midlerm"],GradesDict["final"],GradesDict["project"])

        if(grade >90):
            print("Your grade : AA")
        elif (grade>70):
            print("Your grade : BB")
        elif (grade>50):
            print("Your grade : CC")
        elif(grade>30):
            print("Your grade : DD")
        else:
            print("Your grade : FF. You are failure.")


while True:
    Name=str(input('Please enter your name:'))
    Surname=str(input('Please enter your surname:'))
    if(EntryErrorCount < 2):        
        #print(IsStudentInList(Name,Surname))
        if(IsStudentInList(Name,Surname)):
            print ('Welcome '+ Name)
            SelectLesson()
            break
        else:
            EntryErrorCount+=1
            print('Your name or surname is not correct. Please check and try again.')
    else:
        print('Please try again later')
        break






