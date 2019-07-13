def account_random():
    import random
    users = []
    status = []
    class account():
        def __init__(self, userid):
            global users, status
            self.userid = userid
            if status[self.userid] == False:
                if users[self.userid] == True:
                    self.login()
                else:
                    self.register()
            else:
                print("This account is online or has been registered. Please make it offline or use another user id first.")
        def login(self):
            global users, status
            pw = input("Please input the password of the user \"", self.userid, "\":")
            random.seed = pw
            pw = random.randint(100)
            if pw == users[self.userid]:
                del pw
                status[self.userid] = True
                print("Login successfully!")
            else:
                print("The password isn't correct.")
        def register(self):
            global users, status
            pw = input("Please input the password you want to set of the user \"", self.userid, "\":")
            pw2 = input("Please input the password you want to set of the user \"", self.userid, "\" again:")
            if pw == pw2:
                random.seed = pw
                del pw2
                users[self.userid] = random.randint(100)
                del pw
                print("Setting password successfully! You can log in now.")
            else:
                print("The first password is different from the second one.")
        def changePW(self):
            global users, status
            oldPW = input("Please input the old password:")
            random.seed = oldPW
            if random.randint(100) == users[self.userid]:
                del oldPW
                newPW1 = input("Please input the password you'd like to change to:")
                newPW2 = input("Please input the password you'd like to change to again:")
                if newPW1 == newPW2:
                    random.seed = newPW1
                    users[self.userid] = random.randint(100)
                    del newPW1, newPW2
                    print("Change the password successfully!")
                else:
                    print("The first password is different from the second one.")