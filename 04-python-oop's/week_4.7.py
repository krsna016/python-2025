class pwskills:
    def student_details(self,name,mail,num):
        print(name,mail,num)
        self.mentor_for_class("Shyam")
    @staticmethod
    def mentor_for_class(list_mentor):
        pwskills.mentor_id("abc@gmail.com")
        print(list_mentor)
    @classmethod
    def class_name(cls):
        cls.mentor_for_class("Ravi")
    @staticmethod
    def mentor_id(id):
        print(id)
    def mentor(self,mentor_list):
        print(mentor_list)


pw = pwskills()
pw.student_details("Anurag","abc@gmail.com","293u78278")
pw.mentor(["A","B"])
pwskills.mentor_for_class("Ravan")
pwskills.class_name()
