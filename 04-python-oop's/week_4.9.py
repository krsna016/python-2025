class pwskills:
    def __init__(self,course_price,course_name) -> None:
        self.__course_price = course_price
        self.__course_name = course_name
    @property
    def course_price_access(self):
        print(self.__course_price)
    @course_price_access.setter
    def course_price_set(self,new_price):
        self.__course_price = new_price
    @course_price_access.deleter
    def course_price_del(self):
        del self.__course_price


pw = pwskills("1000","Impact")
# pw._pwskills__course_name
# pw._pwskills__course_price
pw.course_price_access        # 1. Now using the property decorator we are able
                              #    to access the attribute values
pw.course_price_set = 8888    # 2. Now we are able to set the new value
pw.course_price_access
del pw.course_price_del
pw.course_price_access        # 3. Now we are able to delete it
# Similarly we can also use 'getter'.

