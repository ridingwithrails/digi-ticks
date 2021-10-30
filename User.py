class User: 
    #This is a user
    def __init__(self, name, role, tickets, coupons, products, username, password): 
        self.name = name
        self.role = role
        self.tickets = tickets
        self.coupons = coupons
        self.products = products
        self.username = username
        self.password = password
    
admin = User("Donovan", "ADMIN", 10000, [], [], "admin", "admin")

 #print(admin.name) for printing anything use the variable and the subject with a dot in between
teacher1 = User("Mrs.Postovoit", "TEACHER", 0, [], [], "teacher", "teacher") 
teacher2 = User("Mr.Alcala", "TEACHER", 0, [], [], "teacher", "teacher")
#How do I print both names because print(teacher.name) prints Mr.Alcala?
student1 = User("Owen", "STUDENT",  0, [], [], "student" , "student" )
student2 = User("Mux", "STUDENT", 10000, [], [], "student", "student")
student3 = User("Dugoo", "STUDENT", 0, [], [], "student", "student")
 #print(student1.password) HAXXXX
