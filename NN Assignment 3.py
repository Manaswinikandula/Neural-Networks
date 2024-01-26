#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Employee:

   
    count_of_employees = 0
    __name=""
    __family=""
    __salary=0
    __department=""

    
    def __init__(self, name, family, salary, department):
        self.__name = name
        self.__family = family
        self.salary = salary
        self.__department = department
        Employee.count_of_employees += 1 

    
    def average_salary(employees):
        total = 0
        for employee in employees:
            total += employee.salary
        return total / Employee.count_of_employees
    
    
    def showData(self):
        print("The count of an employee is\t\t:",Employee.count_of_employees)
        
class FulltimeEmployee(Employee):
    def __init__(self, name, family, salary, department):
        super().__init__(name, family, salary, department)

def main():
    employees = []
    one = FulltimeEmployee("Manaswini", "fam-Kandula", 140000, "Sales Representative") 
    employees.append(one)  
    two = FulltimeEmployee("Mallikarjuna", "fam-Nagendla", 160000, "Engineer")
    employees.append(two)
    three = Employee("Pallavi", "fam-Panguluri", 150000, "Doctor")
    employees.append(three)
    four = Employee("Chanadana", "Fam-pamidimukkala", 180000, "Lawyer")
    employees.append(four)
    Employee.showData(employees) 
    print("Average salary of an employee is:", FulltimeEmployee.average_salary(employees))

if __name__ == "__main__":
    main()


# In[3]:


import numpy as np

def replace_maxmium(array, replace_value, axis):
    result = np.where(array == np.max(
        array, axis=1).reshape(-1, 1), 0 * array, array)
    print(result)


def main():

    rand20 = np.random.random_sample(20) * 20 + 1
    print(rand20)
    
    rand20_4by5 = rand20.reshape((4, 5))
    print(rand20_4by5)

    replace_maxmium(rand20_4by5, 0, 1)

if __name__ == "__main__":
    main()


# In[ ]:




