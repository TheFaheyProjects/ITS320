#Kyle Fahey
#ITS320-1
#Portfolio Project: Module 8

#Student Course Registration System

#Course Class
class Course:
    def __init__(self, courseID, title, description, credits, capacity):
        self.courseID = courseID
        self.title = title
        self.description = description
        self.credits = credits
        self.capacity = capacity
        self.enrolledStudents = []
    
    #Checking if the Course is Full
    def isCourseFull(self):
        return len(self.enrolledStudents) >= self.capacity
    
    #Printing Course Information
    def __str__(self):
        return (f"\nCourse ID: {self.courseID}"
                f"\nTitle: {self.title}"
                f"\nDescription: {self.description}"
                f"\nCredits: {self.credits}"
                f"\nCourse Capacity: {len(self.enrolledStudents)}/{self.capacity}"
                f"\n{'FULL' if self.isCourseFull() else 'Open'}")
  
        
#Student Class
class Student:
    def __init__(self, studentID, password):
        self.studentID = studentID
        self.password = password
        self.registeredCourses = []
    
    #Printing Student Information 
    def __str__(self):
        return f"Student ID: {self.studentID}"
    

#Registation System Class
class RegistrationSystem:
    #Creating Admin and Student Logins
    def __init__(self):
        #Student Credentials
        self.students = {
            '01': Student('01', 'pass123'),
            '02': Student('02', 'pass456'),
            '03': Student('03', 'pass789')
        }
        #Admin Credentials
        self.adminUsername = 'admin'
        self.adminPassword = 'password'
        self.courses = {}
        
    #Login Authentication
    def registrationMenuLogin(self):
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        
        #Checking if Admin or Student is Logged In
        if username == self.adminUsername and password == self.adminPassword:
            print("\nAdmin Logged In Successfully.")
            #Open Admin Main Menu
            self.adminMainMenu()
        elif username in self.students and self.students[username].password == password:
            print(f"\nStudent {username} Logged In Successfully.")
            #Open Student Main Menu
            self.studentMainMenu(self.students[username])
        
        #Handle Invalid Login
        else:
            print("\nInvalid Credentials. Login Not Successful.")
            
    #Admin Main Menu
    def adminMainMenu(self):
        while True:
            print("\n--- Admin Main Menu ---")
            print("1. Add Course")
            print("2. Remove Course")
            print("3. Update Course")
            print("4. Search Course")
            print("5. List Students in a Course")
            print("6. List All Courses For a Student")
            print("7. List All Student Information (Login Credentials)")
            print("8. List All Courses")
            print("9. Logout")
        
            #Admin Main Menu Selection
            adminInput = input("\nSelect from the Menu: 1-9: ")
            
            #Handling Admin Menu Options
            if adminInput == "1":
                self.addCourse()
            elif adminInput == "2":
                self.removeCourse()
            elif adminInput == "3":
                self.updateCourse()
            elif adminInput == "4":
                self.searchCourse()
            elif adminInput == "5":
                self.listOfStudentsInCourse()
            elif adminInput == "6":
                self.listCoursesOfStudent()
            elif adminInput == "7":
                self.allStudentInformation()
            elif adminInput == "8":
                self.listAllCourses()
            elif adminInput == "9":
                print("\nAdmin has Successfully Logged Out.")
                break
            else:
                print("\nInvalid Menu Option. Please Select From the Menu.")
                
    #Student Main Menu
    def studentMainMenu(self, student):
        while True:
            print("\n--- Student Main Menu ---")
            print("1. Register For a Course")
            print("2. Drop a Course")
            print("3. View My Registered Courses")
            print("4. List All Courses")
            print("5. Logout")
            
            #Student Main Menu Selection
            studentInput = input("\nSelect from the Menu: 1-5: ")
            
            #Handling Student Menu Options
            if studentInput == "1":
                self.registerForCourses(student)
            elif studentInput == "2":
                self.dropCourse(student)
            elif studentInput == "3":
                self.viewRegisteredCourses(student)
            elif studentInput == "4":
                self.listAllCourses()
            elif studentInput == "5":
                print("\nStudent has Successfully Logged Out.")
                break
            else:
                print("\nInvalid Menu Option. Please Select From the Menu.")
                
    #Adding, Removing, Updating, and Searching Courses
    #Adding Course
    def addCourse(self):
        try:
            courseID = input("Course ID: ")
            if courseID in self.courses:
                print("\nThis Course already exists within our System.")
                return
            title = input("Title: ")
            description = input("Description: ")
            credits = int(input("Credits: "))
            capacity = int(input("Capacity: "))
            self.courses[courseID] = Course(courseID, title, description, credits, capacity)
            print("\nThe Course Has Been Added Successfully.")
        except ValueError:
            print("\nNot a Valid Course. Please Try Again.")
            
    #Removing Course
    def removeCourse(self):
        courseID = input("\nEnter the Course ID you wish to Remove: ")
        if courseID in self.courses:
            course = self.courses[courseID]
            for studentID in course.enrolledStudents:
                if courseID in self.students[studentID].registeredCourses:
                    self.students[studentID].registeredCourses.remove(courseID)
            del self.courses[courseID]
            print("\nThe Course Has Been Removed Successfully.")
        else:
            print("\nCourse Was Not Found.")
            
    #Updating Course
    def updateCourse(self):
        courseID = input("\nEnter the Course that you Wish to Update: ")
        if courseID in self.courses:
            course = self.courses[courseID]
            course.title = input(f"New Title ({course.title}): ") or course.title
            course.description = input(f"New Description ({course.description}): ") or course.description
            try:
                course.credits = int(input(f"New Credits ({course.credits}): ") or course.credits)
                course.capacity = int(input(f"New Capacity ({course.capacity}): ") or course.capacity)
                print("\nThe Course Has Been Updated Successfully.")
            except ValueError:
                print("\nInvalid Input. Please use Integers Only.")
        else:
            print("\nCourse Was Not Found.")
            
    #Searching Courses
    def searchCourse(self):
        courseLookUp = input("\nEnter the Title of the Course or the Course ID: ").lower()
        found = False
        for course in self.courses.values():
            if courseLookUp in course.title.lower() or courseLookUp == course.courseID:
                print(course)
                found = True
        if not found:
            print("\nThe Course you're Searching for Cannot be Found.")
            
    #Registering and Dropping Classes
    #Registering For A Class
    def registerForCourses(self, student):
        courseID = input("Enter the Course ID: ")
        if courseID not in self.courses:
            print("\nCourse Does Not Exist.")
            return
        course = self.courses[courseID]
        if courseID in student.registeredCourses:
            print("\nYou're Already Registered.")
        elif course.isCourseFull():
            print("\nThe Course is Already Full.")
        else:
            student.registeredCourses.append(courseID)
            course.enrolledStudents.append(student.studentID)
            print("\nYou Have Successfully Registered for this Course.")
            
    #Dropping A Class
    def dropCourse(self, student):
        courseID = input("Enter the Course ID: ")
        if courseID in student.registeredCourses:
            student.registeredCourses.remove(courseID)
            if courseID in self.courses:
                self.courses[courseID].enrolledStudents.remove(student.studentID)
                print("\nYou Have Successfully Dropped this Course.")         
        else:
            print("\nYou're not currently Registered in this Course.") 
            
    #Displaying All Course Information and Students
    #Students in a Course
    def listOfStudentsInCourse(self):
        courseID = input("Enter the Course ID: ") 
        if courseID in self.courses:
            course = self.courses[courseID]
            print(f"Students in {course.title}: ({course.courseID})")
            if course.enrolledStudents:
                for studentID in course.enrolledStudents:
                    print(f"{studentID}")
            else:
                print("No Students Currently Enrolled")
        else:
            print("\nCourse Was Not Found or It Does Not Exist.")
            
    #Courses of a Specific Student
    def listCoursesOfStudent(self):
        studentID = input("Enter Student ID: ")
        if studentID in self.students:
            student = self.students[studentID]
            print(f"Student {studentID} Registered Courses ")
            if student.registeredCourses:
                for courseID in student.registeredCourses:
                    if courseID in self.courses:
                        print(f"{courseID}: {self.courses[courseID].title}")
                    else:
                        print(f"{courseID} No Longer Exists.")
            else:
                print("The Student has not yet Registered for Any Courses.")
        else:
            print("\nStudent Was Not Found in the System.")
            
    #Listing All Students
    def allStudentInformation(self):
        for studentID, student in self.students.items():
            print(f"Student ID: {studentID}, Password: {student.password}")
            
    #All Registered Courses for Student
    def viewRegisteredCourses(self, student):
        print(f"All Registered Courses for the Following Student: {student.studentID}")
        if student.registeredCourses:
            for courseID in student.registeredCourses:
                if courseID in self.courses:
                    print(f"{courseID}: {self.courses[courseID].title}")
                else:
                    print(f"{courseID} No Longer Exists.")
        else:   
            print("\nStudent is not Currently Registered in Any Courses.")
            
    #List of All Courses
    def listAllCourses(self):
        if not self.courses:
            print("\nThere is Not Currently Any Courses Available.")
        for course in self.courses.values():
            print(course)

#Program Main Menu Login Screen
def registrationMainMenu():
    system = RegistrationSystem()
    while True:
        print("\n--- Student Course Registration System ---")
        print("1. Login")
        print("2. Exit")
        
        #Menu Selection
        userInput = input("\nSelect from the Menu. 1 or 2: ")
        
        #Handling Menu
        if userInput == "1":
            system.registrationMenuLogin()
        elif userInput == "2":
            print("The Program is Closing. See You Next Time!")
            break
        else:
            print("\nInvalid Option. Please Select 1 or 2.")
        
#Running the Program
if __name__ == "__main__":
    registrationMainMenu()
                
                
            
            
            
    
    
    
    
                
        
        
        
        
        
        