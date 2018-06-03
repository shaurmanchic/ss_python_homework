# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 17:31:35 2018

@author: shaurmanchic
"""

class Department(object):
    def __init__(self, managers):
        self.managers = managers
    
    @staticmethod
    def give_salary(employee):
        if type(employee) == Manager and employee.team == []:
            raise SalaryGivingError(employee.last_name)
        print("{} {}: got salary: {}".format(
            employee.first_name, employee.last_name, employee.salary))
            
    def add_team_members(manager, team):
        try:
            manager.add_to_team(team)
        except NotEmployeeException:
            print('The list is empty, please add employees to the list before adding.')
        except WrongEmployeeRoleError:
            print('There is a manager in the list, please check your list.')
        
    

class Employee(Department):
    def __init__(self, first_name, last_name, salary, experience, manager):
        self.first_name = first_name
        self.last_name = last_name
        self.experience = experience
        self.manager = manager
        
        if self.experience > 5:
            self.salary = salary * 1.2 + 500
        elif self.experience > 2:
            self.salary = salary + 200
        else:
            self.salary = salary
        
    def __str__(self):
        return "{} {}, manager:{}, experience:{}".format(
            self.first_name, self.last_name, self.manager.last_name,
            self.experience)
    

class Manager(Employee):
    def __init__(self, first_name, last_name, salary, experience, team):
        super().__init__(first_name, last_name, salary, experience, manager=None)
        self.team = team
        
        if len(team) > 10:
            self.salary = salary + 300
        elif len(team) > 5:
            self.salary = salary + 200
        
        developer_count = 0
        for team_member in team:
            if type(team_member) == Developer:
                developer_count += 1
        
        if developer_count > (len(team)/2):
            self.salary *= 1.1
        
    def add_to_team(self, team):
        if not team:
            raise NotEmployeeException('There are no employees in the list!')
        for team_member in team:
            if type(team_member == Manager):
                raise WrongEmployeeRoleError(manager.last_name)
            
class SalaryGivingError(Exception):
    def __init__(self, last_name):
        print("{} has no team! Why should we give him salary?".format(last_name))
        
        
class WrongEmployeeRoleError(Exception):
    def __init__(self, last_name):
        print("Employee {} has unexpected role!".format(last_name))
        
        
class NotEmployeeException(Exception):
    def __init__(self, message):
        print(message)
            

class Designer(Employee):
    def __init__(self, first_name, last_name, salary, experience, manager, efficiency):
        super().__init__(first_name, last_name, salary, experience, manager)
        
        assert(efficiency >= 0 and efficiency <= 1),\
            "Invalid Designer efficiency coefficient!"
        self.efficiency = efficiency
        self.salary = salary * efficiency
    

class Developer(Employee):
    def __init__(self, first_name, last_name, salary, experience, manager):
        super().__init__(first_name, last_name, salary, experience, manager)