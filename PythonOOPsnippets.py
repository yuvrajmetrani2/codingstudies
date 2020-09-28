# Python OOPs

class Employee:
    num_of_emps = 0
    raise_amt = 1.04
    
    def __init__(self, first, last, pay=0):
        '''
        initialzation method
        '''
        self.first = first
        self.last = last
        self.pay = pay
        
        Employee.num_of_emps += 1
	
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)
        
    
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)
    
    def __add__(self, other):
        return self.pay + other.pay
    
    def __len__(self):
        return len (self.fullname())
    
    @property
    def email(self):
        return ('{}.{}@email.com'.format(self.first, self.last))
    
#    @fullname.setter
#    def fullname(self, name):
#        first, last = name.split(' ')
#        self.first = first
#        self.last = last
    
    @property
    def fullname(self):
        return ('{} {}'.format(self.first, self.last))
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last     

    @fullname.deleter
    def fullname(self):
        print('Deleting name')
        self.first = None
        self.last = None
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
        
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
        
    @staticmethod
    def is_workday(day):
        if (day.weekday() == 5 or day.weekday() == 6):
            return False
        return True
    

class Developer(Employee):
    raise_amt = 1.05
    
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang



class Manager(Employee):
    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
            
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
            
    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())
        #print(len(self.employees))

        
        
emp_1 = Employee('Yuvraj', 'emp1', 50000)
emp_2 = Employee('Shraddha', 'emp2', 60000)
dev_1 = Developer('Yuvraj', 'Metrani', 50000, 'Python')
dev_2 = Developer('Shraddha', 'Metrani', 60000, 'Java')
mgr_1 = Manager('sue', 'smith', 80000, [dev_1])


print(emp_1.first)
emp_1.first = 'Sheetal'
print(emp_1.first)
print(emp_1.email)

emp_1.fullname = 'Yuvraj Metrani'
print(emp_1.fullname)
print(emp_1.email)

del emp_1.fullname
print(emp_1.first)
print(emp_1.email)
##print(mgr_1.email)
#print(mgr_1.print_emps())
#
#mgr_1.add_emp(dev_2)
#print(mgr_1.print_emps())
#
#mgr_1.remove_emp(dev_1)
#print(mgr_1.print_emps())

#print(isinstance(mgr_1, Developer))
#print(isinstance(dev_1, Developer))

#print(type(Developer))
#print(issubclass(Employee, Developer))

#print(emp_1)

#print(repr(emp_1))
#print(str(emp_1))
#print(emp_1 + emp_2)
#print(len(emp_1))







#print(dev_1.pay)
#dev_1.apply_raise()
#print(emp_1.pay)

#print(help(Developer))

#print(emp_1.email)
#print(dev_1.email)
#print(dev_1.prog_lang)



#import datetime
#my_date = datetime.date(2016, 7, 11)
#
# 
#print(str(my_date))
#print(Employee.is_workday(my_date))
