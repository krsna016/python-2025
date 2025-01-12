# def test(a,b):
#     return a+b
# print(test(2,3)) # Addition
# print(test("Anurag"," Pareek")) # Concatenation
# print(test([1,2,3],[4,5,6])) # List concatenation





class data_science:

    def __init__(self):
        pass

    def syllabus(self):
        print("This is my syllabus for data science masters")

class web_dev:

    def __init__(self):
        pass

    def syllabus(self):
        print("This is my syllabus for web dev")

def class_parser(class_object): # This function is working differently according to the object
    for i in class_object:
        i.syllabus()


data_science = data_science()
web_dev = web_dev()
class_obj = [data_science,web_dev]
class_parser(class_obj)