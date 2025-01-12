# l = [1,2,3,4] # l -> object
# print(type(l)) # class -> list

# class test:
#     pass
# a = test()
# print(type(a))





# class pwskills: # Class name : pwskills

#     def __init__(self,phone_num,email_id,student_id): # Initializing data
#         self.phone_nums = phone_num # Attribute = phone_nums
#         self.email_ids = email_id # Attribute = email_ids
#         self.student_ids = student_id # Attribute = student_ids
    
#     def student_details(self): # Method 1 : student_details
#         return self.student_ids,self.phone_nums,self.email_ids

#     def welcome_msg(self): # Method 2 : welcome_msg
#         print("Welcome to pw-skills")

# # rohan = pwskills()
# # print(type(rohan)) # type : <class '__main__.pwskills'> # Class object : rohan
# # rohan.welcome_msg()

# # gaurav = pwskills() # type : <class '__main__.pwskills'> # Class object : gaurav
# # gaurav.welcome_msg()

# anurag = pwskills(6900438634,"abc@gmail.com",2215000322)
# print(anurag.student_details())

# gaurav = pwskills(4378734378,"cdf@gmail.com",492723973)
# print(gaurav.student_details())

# print(anurag.email_ids)









class pwskills: # Class name : pwskills

    def __init__(self_1,phone_num,email_id,student_id): # Initializing data
        self_1.phone_nums = phone_num # Attribute = phone_nums
        self_1.email_ids = email_id # Attribute = email_ids
        self_1.student_ids = student_id # Attribute = student_ids
    
    def student_details(self_1): # Method 1 : student_details
        return self_1.student_ids,self_1.phone_nums,self_1.email_ids

    def welcome_msg(self_1): # Method 2 : welcome_msg
        print("Welcome to pw-skills")

# rohan = pwskills()
# print(type(rohan)) # type : <class '__main__.pwskills'> # Class object : rohan
# rohan.welcome_msg()

# gaurav = pwskills() # type : <class '__main__.pwskills'> # Class object : gaurav
# gaurav.welcome_msg()

anurag = pwskills(6900438634,"abc@gmail.com",2215000322)
print(anurag.student_details())

gaurav = pwskills(4378734378,"cdf@gmail.com",492723973)
print(gaurav.student_details())

print(anurag.email_ids)