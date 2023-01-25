import datetime

class Employee:
  def __init__(self, fname, lname, empid, title, sal):
    self.firstname = fname
    self.lastname = lname
    self.employeeid = empid
    self.jobtitle = title
    self.salary = sal

    self.hireddate = datetime.date.today()

  #returns first name
  def get_firstname(self):
    return self.firstname

  #sets firstname if fname isn't an empty string
  def set_firstname(self,fname):
    if len(fname) > 0:
      self.firstname = fname

  #returns last name
  def get_lastname(self):
    return self.lastname

  #set lastname if lname isn't an empty string
  def set_lastname(self,lname):
    if len(lname) > 0:
      self.lastname = lname

  #returns job title
  def get_jobtitle(self):
    return self.jobtitle

  #sets job title if job title isn't an empty string
  def set_jobtitle(self,title):
    if len(title) > 0:
      self.jobtitle = title
  
  #return employee id
  def get_employeeid(self):
    return "Employee ID: " + str(self.employeeid)

  #returns salary
  def get_salary(self):
    return "${:,.2f}".format(self.salary)

  #sets salary if salary isn't an empty string
  def set_salary(self,sal):
    if sal > 0:
      self.salary = sal

  #increase salary
  def increase_salary(self,percent):
    if percent > 0:
      self.set_salary(self.salary + self.salary * percent)
    else:
      print("Increase of salary must be greater than 0.")
    
empdata = Employee("Steven", "Evens", 9090, "Director of Custodial arts", 100000)
print(empdata.get_firstname())
print(empdata.get_lastname())
print(empdata.get_employeeid())
print(empdata.get_jobtitle())
print(empdata.get_salary())

#increase of salary
empdata.increase_salary(0.02)
print("After increase: " + empdata.get_salary())