class User:
    def __init__(self, first_name, last_name, email, age):
        self.fname = first_name
        self.lname = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print("User info: ", "\n",self.fname,"\n", self.lname, "\n",self.email, "\n",self.age)

    def enroll(self):
        if self.is_rewards_member == True:
            print("User already a member")
            return False
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
            return True

    def spend_points(self, amount):
        self.gold_card_points -= amount
        return self.gold_card_points



nima = User("Nima", "Bazofti", "nima@gmail.com", 29)
andres = User("Andres", "Yooo", "andres@gmail.com", 29)
jh = User("John", "Henry", "jh@gmail.com", 29)
nima.display_info()
andres.display_info()
jh.display_info()

nima.enroll()
print(nima.spend_points(50))

andres.enroll()
print(andres.spend_points(80))

jh.enroll()
print(jh.spend_points(100))

