class Student:
    def __init__(self,roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def get_result(self):
        if self.marks>=35:
            print(f"Student {self.roll_no}-{self.name}: PASS")
        else:
            print(f"Student {self.roll_no}-{self.name}: Fail")

student1 = Student(1,"Riya",80)
student2 = Student(2,"abc",29)

student1.get_result()
student2.get_result()