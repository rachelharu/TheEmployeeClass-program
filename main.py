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


class Contractor(Person):
  def __init__(self,fname,lname,title,wage,contractorid):
    super().__init__(fname,lname,title)
    self.contractorid = contractorid
    self.hourlywage = wage

  #return contractor id
  def get_contractorid(self):
    return "Contractor ID: " + str(self.contractorid)

  #set hourly wage
  def set_hourlywage(self, wage):
    if wage > 0:
      self.hourlywage = wage

  #return wage
  def get_hourlywage(self):
    return "${:,.2f}".format(self.hourlywage)

  #sets job wage if wage greater than 0
  def set_get_hourlywage(self,get_hourlywage):
    if get_hourlywage > 0:
      self.wage = get_hourlywage

con = Contractor('Temp','Emp','Developer',60,2)
print(con.get_firstname())
print(con.get_lastname())
print(con.get_contractorid())
print(con.get_jobtitle())
print(con.get_hourlywage())
print(con.set_hourlywage(50))
print(con.get_hourlywage())