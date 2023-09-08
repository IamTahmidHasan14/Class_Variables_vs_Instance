class Students4:

  dept = "CSE"
  uni = "VU"
  totalst = 0

  def __init__(self, name):
    self.name = name
    self.id = 67
    Students4.totalst += 1

  def details(self):
    print(
      f"{self.name}'s id is {self.id} in {self.dept} at {self.uni} where number of total Students are {self.totalst}\n"
    )


s4 = Students4("Tahmid")
s4.details()
s47 = Students4("Bayazid")
s47.id = 17
s47.details()
s05 = Students4("Hafizur")
s05.dept = "EEE"
s05.id = 5
s05.details()
Students4.uni = "Varendra University"
s4.details()