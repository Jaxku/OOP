class AllStaff:     # The syperclass (parent class) covering universal attributes and methods
    def __init__(self, name, age, emp_id, brith_date, job_title):
        self.name = name
        self.age = age
        self.emp_id = emp_id
        self.brithdate = brith_date
        self.job_title = job_title

    def show(self):
        print(f"{self.emp_id} is {self.name} aged {self.age} being born {self.birthdate} employed as a {self.job_title}")

# Child classes contain attribute unique to that class
class Management(AllStaff):
    def __init__(self, name, age, emp_id, birthdate, job_title, car):
        super().__init__(name, age, emp_id, birthdate, job_title,)
        self.car = car

    def show(self):
        print(f"{self.emp_id} is {self.age} being born {self.birthdate} employed as {self.job_title} and "
              f"drives a {self.car}")

class Clerical(AllStaff):
        def __init__(self, name, age, emp_id, birthdate, job_title, typing_speed): # Add unique attribute typing speed
            super().__init__(name, age, emp_id, birthdate, job_title,)
            self.typing_speed = typing_speed

    def show(self):
        print(f"{self.emp_id} is {self.age} being born {self.birthdate} employed as {self.job_title} and "
              f"types at {self.typing_speed} words per minute")


class Factory(AllStaff):
    pass    # No Unique attributes or methods


# Main routine
a = Management("Jenny", 22, "ID007", "20.12.2000", "Manging Director", "Jaguar")
a.show()
print()

b = Clerical("Tim", "17", "ID119","01/01/2005", "Typist", 123)
b.show()
print()

c = Factory("Jake", 16, "ID125", "17/08/2006", "Labourer")
c.show()
print()




