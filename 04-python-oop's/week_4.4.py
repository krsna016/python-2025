import abc
class pwskills:
    @abc.abstractmethod
    def students_details(self):
        pass
    @abc.abstractmethod
    def students_assignmenst(self):
        pass
    @abc.abstractmethod
    def students_marks(self):
        pass
class students_detail(pwskills):
    def students_details(self):
        return "This is a method for taking students details"
    def students_assignmenst(self):
        return "This is a method for assignments details for students"
class data_science_masters(pwskills):
    def students_details(self):
        return "Details for data-science-masters"
    def students_assignmenst(self):
        return "Students assignment details for d-s-m"
