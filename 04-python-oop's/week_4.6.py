class pwskills:

    name = "Anurag Pareek"

    def __init__(self,name,email):
        self.name = name
        self.email = email
    @classmethod
    def change_name(cls,name):
        pwskills.name = name
    @classmethod
    def details(cls,name,email):
        return cls(name,email)
    def student_details(self):
        print(self.name,self.email,pwskills.name)

# pw = pwskills("Mohan","abc@gmail.com")
# print(pw.name)
# print(pw.email)
# pw.student_details()

pw1 = pwskills.details("abc","abc@gmail.com")
print(pw1.name)
print(pw1.email)
print(pwskills.name)
pwskills.change_name("Anurag")
print(pwskills.name)
pw2 = pwskills("Anurag Pareek","abc@gmail.com")
pw2 = pwskills.details("Hello","World")
pw2.student_details()

def course_details(cls,course_name):
    print(f"course name is {course_name}")

pwskills.course_details = classmethod(course_details)
pwskills.course_details("HEllo WOrld")

def mentor(cls,list_of_mentor):
    print(list_of_mentor)

pwskills.mentor = classmethod(mentor)
pwskills.mentor(["a","b","x"])

del pwskills.student_details
# print(pwskills("Hello","World").student_details()) # This is now deleted
delattr(pwskills,"name") # del pwskills.name <- Can use this as well
