class School:
    school_name="Spring High School"
    def __init__(self, name, grade):
        self.name= name
        self.grade= grade
s1=School("Prabisha", "A")
s2=School("Dipa", "B")
print(s1.school_name)
print(s2.school_name)
School.school_name= "Samriddhi School"
print(s1.school_name)
print(s2.school_name)
s1.school_name= "Hi School"
print(s1.school_name)
print(s2.school_name)