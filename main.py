import datetime

class Person:
  def __init__(self, fname, lname, title):
    self.firstname = fname
    self.lastname = lname
    self.jobtitle = title

    self.hireddate = datetime.date.today()

  #returns first name
  def get_firstname(self):
    return self.firstname

  #sets firstname if fname isn't an empty string
  def set_firstname(self, fname):
    if len(fname) > 0:
      self.firstname = fname

  #returns last name
  def get_lastname(self):
    return self.lastname

  #set lastname if lname isn't an empty string
  def set_lastname(self, lname):
    if len(lname) > 0:
      self.lastname = lname

  #returns job title
  def get_jobtitle(self):
    return self.jobtitle

  #sets job title if job title isn't an empty string
  def set_jobtitle(self, title):
    if len(title) > 0:
      self.jobtitle = title


class Employee(Person):
  def __init__(self, fname, lname, title, sal, empid):
    super().__init__(fname, lname, title)
    self.employeeid = empid
    self.salary = sal
    self.vacationdaysperyear = 14
    self.vacationdays = self.vacationdaysperyear

  #returns employee id
  def get_employeeid(self):
    return "Employee ID: " + str(self.employeeid)

  #returns salary
  def get_salary(self):
    return "${:,.2f}".format(self.salary)

  #sets salary if salary isn't an empty string
  def set_salary(self, sal):
    return "${:,.2f}".format(self.salary)

  #increase salary
  def increase_salary(self, percent):
    if percent > 0:
      self.set_salary(self.salary + self.salary * percent)
    else:
      print("Increase of salary must be greater than 0.")

  #increase vacation days per year
  def increase_vacation_days_per_year(self, days):
    if days > 0:
      self.vacationdayspersyear = self.vacationdaysperyear + days

  #increase vacation days
  def increase_vacation_days(self, days):
    if days > 0:
      self.vacationdays = self.vacation + days

  #increase vacation days by year
  def increase_vacation_days_yearly(self):
    self.vacationdays = self.vacationdays + self.vacationdaysperyear

  #take some vacation days
  def take_vacation_days(self, days):
    if days > 0 and self.vacationdays - days >= 0:
      self.vacationdays = self.vacationdays - days
    elif days <= 0:
      print("Vacation days taken must be greater than 0.")
    elif self.vacationdays - days < 0:
      print(
        f"Employee does not have enough vacation days to take off {days} days."
      )

    #return vacation days
  def get_vacation_days(self):
    return "Vacation Days: " + str(self.vacationdays)


emp1 = Employee('Jack', 'Krichen', 'Manager', 500000, 1)

print(emp1.get_firstname())
print(emp1.get_lastname())
print(emp1.get_employeeid())
print(emp1.get_jobtitle())
print(emp1.get_salary())

print(emp1.get_vacation_days())
emp1.take_vacation_days(10)
print(emp1.get_vacation_days())
emp1.take_vacation_days(10)
emp1.take_vacation_days(-1)

emp1.increase_vacation_days_yearly()
print(emp1.get_vacation_days())
