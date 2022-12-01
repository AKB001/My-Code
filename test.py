class Person(object):

	# Constructor
	# def _init_(self, name):
	# 	self.name = name

	# To get name
	def getName(name):
		name = "Ram"
		return name

	# To check if this person is an employee
	def isEmployee(self):
		return False


# Inherited or Subclass (Note Person in bracket)
class Employee(Person):

	# Here we return true
	def isEmployee(self):
		return True


# Driver code
emp =Person()
print(emp.getName(), emp.isEmployee())

emp = Employee()