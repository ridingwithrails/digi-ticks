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
    
    @staticmethod
    def build():
        admin = User("Donovan", "ADMIN", 10000, [], [], "admin", "admin")

        #print(admin.name) for printing anything use the variable and the subject with a dot in between
        teacher1 = User("Mrs.Postovoit", "TEACHER", 0, [], [], "teacher1", "teacher") 
        teacher2 = User("Mr.Alcala", "TEACHER", 0, [], [], "teacher2", "teacher")
        #How do I print both names because print(teacher.name) prints Mr.Alcala?
        student1 = User("Owen", "STUDENT",  0, [], [], "student1" , "student" )
        student2 = User("Mux", "STUDENT", 10000, [], [], "student2", "student")
        student3 = User("Dugoo", "STUDENT", 10000, [], [], "student3", "student")
        student4 = User("Johnny", "STUDENT", 0, [], [], "student4", "student")
        
        users = {"admin": admin,"teacher1": teacher1, "teacher2": teacher2,"student1":student1,"student2":student2,"student3":student3,"student4":student4}
        return users
