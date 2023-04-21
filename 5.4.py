class Employee:
    #class variable
    additional_salary = 0

    def __init__(self, name, id, salary, department):
        self.name = name
        self.id = id
        self.salary = salary
        self.department = department 

    def __str__(self):
        return f"Name: {self.name}, ID: {self.id}, Salary: {self.salary}, Department: {self.department}, Additional Payment: {self.additional_salary}"

    def set_department(self, department):
        self.department = department

    def additional_payment(self, hours):
        if hours > 40:
            Employee.additional_salary = (hours - 40) * (self.salary / 40)


Steven = Employee("Steven Tornow", "S58746", 2500, "Accounting")

print(Steven)
Steven.set_department("Research")
print(Steven)
Steven.additional_payment(50)
print(Steven)