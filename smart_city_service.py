#2.mini project- smart city service managent system.
from abc import ABC, abstractmethod

class service(ABC):

  @abstractmethod
  def start_service(self):
    pass

  @abstractmethod
  def calculate_fee(self):
    pass


#(inheritance+polymorphism) services.
class water_service(service):

  def __init__(self,meter_reading,per_litre_rate = 10):
    self.meter_reading = meter_reading
    self.per_litre_rate = per_litre_rate

  def start_service(self):
    print(f"water services started per meter reading {self.meter_reading}")

  def calculate_fee(self):
    return self.meter_reading * self.per_litre_rate


class electricity_service(service):

  def __init__(self,units,per_units_rate = 5):
    self.units = units
    self.per_units_rate = per_units_rate

  def start_service(self):
    print(f"electricity services started per units {self.units}")

  def calculate_fee(self):
     return self.units * self.per_units_rate


class internet_service(service):

  def __init__(self, speed, plan, fixed_monthly_fee = 800):
    self.plan = plan
    self.speed = speed
    self.fixed_monthly_fee = fixed_monthly_fee

  def start_service(self):
    print(f"internet services started per plan {self.plan} and speed {self.speed}")

  def calculate_fee(self):
     if self.plan.lower() == "basic":
       return self.fixed_monthly_fee
     elif self.plan.lower() == "pro":
       return self.fixed_monthly_fee + 300    #pro mate 300 extra
     else:
       return 0


#(encapsulation) citizen
class citizen:

  def __init__(self, name, home_no):
    self.__name = name
    self.__home_no = home_no
    self.__service = []

  # getter methods
  def get_name(self):
    return self.__name

  def get_home_no(self):
    return self.__home_no

  def get_service(self):    #aama list add thase.
    return self.__service

  def add_service(self, servicess):
    self.__service.append(servicess)



#main program
print("=========== SMART CITY SERVICE SYSTEM ==============")
print("-------------------- T TOWN --------------------")

name = input("enter your name:")
home_no = int(input("enter your home number:"))

citizen1 = citizen(name, home_no)

print("----------------------------------------")

while True:

  print("select service:")
  print("1.Water Service.")
  print("2.Electricity Service.")
  print("3.Internet Service.")
  print("4.Exit.")

  choice = int(input("enter your choice:"))

  if choice == 1:
    meter_reading = int(input("enter your meter reading:"))
    citizen1.add_service(water_service(meter_reading))     #object create karelo che water_service no
    print("water service added successfully!")

  elif choice == 2:
    units = int(input("enter electricity units used: "))
    citizen1.add_service(electricity_service(units))
    print("electricity service added successfully!")

  elif choice == 3:
    speed = int(input("enter internet speed: "))
    plan = input("enter internet plan (Basic/Pro): ")
    citizen1.add_service(internet_service(speed, plan))
    print("internet service added successfully!")

  if choice == 4:
    break

  again = input("do you want to add another service? (yes/no): ")
  if again.lower() != "yes":
    break

print("----------------BILL GENERATE----------------")
print("----------------------------------------------")
print(f"Generating Bill for Citizen: {citizen1.get_name()}")
print(f"Home Number: {citizen1.get_home_no()}")
print("----------------------------------------------")

total_bill = 0

for s in citizen1.get_service():

   if isinstance(s, water_service):   #isinstance (Check kare che: aa s water_service class no object che ke nathi)
     fee = s.calculate_fee()          #calculate_fee method che water_service ni.
     print(f"Water Service Bill: ₹{fee}")

   elif isinstance(s, electricity_service):
        fee = s.calculate_fee()
        print(f"Electricity Service Bill: ₹{fee}")

   elif isinstance(s, internet_service):
        fee = s.calculate_fee()
        print(f"Internet Service Bill: ₹{fee}")

   total_bill = total_bill + fee


print("----------------------------------------------")
print(f"Total Bill for : ₹{total_bill}")
print("----------------------------------------------")

print("Thank You for Using Smart City Service System!")
