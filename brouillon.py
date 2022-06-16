import datetime
import random


class DataBase:
    def __init__(self, filename):
        self.filename = filename
        self.users = None
        self.file = None
        self.load()

    def load(self):
        self.file = open(self.filename, "r")
        self.users = {}

        for line in self.file:
            email, password, name, created = line.strip().split(";")
            self.users[email] = (password, name, created)

        self.file.close()

    def get_user(self, email):
        if email in self.users:
            return self.users[email]
        else:
            return -1
    def give_user_name(self,email):
        return self.users[email][1]
    def add_user(self, email, password, name):
        if email.strip() not in self.users:
            self.users[email.strip()] = (password.strip(), name.strip(), DataBase.get_date())
            self.save()
            return 1
        else:
            print("Email exists already")
            return -1

    def validate(self, email, password):
        if self.get_user(email) != -1:
            return self.users[email][0] == password
        else:
            return False

    def save(self):
        with open(self.filename, "w") as f:
            for user in self.users:
                f.write(user + ";" + self.users[user][0] + ";" + self.users[user][1] + ";" + self.users[user][2] + "\n")

    @staticmethod
    def get_date():
        return str(datetime.datetime.now()).split(" ")[0]


class bd_proposition:
    def __init__(self, filename):
        self.filename = filename
        self.propo = None
        self.file = None
        self.nbr_prop_par_bloc = 8
        self.nbr_bloc = 4
        self.current_bloc = None
        self.current_proposition = None
        self.id_bloc = 1
        self.load()
        #print(self.current_bloc)

    def load(self):
        self.file = open(self.filename, "r")
        self.propo = []

        for line in self.file:
            proposition, DE, AE, EN, IN, IS, IA, IAD, SM = line.split(";")
            self.propo.append([proposition,DE, AE, EN, IN, IS, IA, IAD, SM[:len(SM)-1]])
        self.file.close()


    def dict_proposition(self):
        return self.propo

    def set_current_bloc_proposition(self):
        if(self.nbr_bloc * self.nbr_prop_par_bloc != len(self.propo)):
            print('error')
            #break
        else:
            n = random.randint(1,self.nbr_bloc)
            #print(n)
            while self.current_bloc == n:
                n = random.randint(1, self.nbr_bloc)
                #print(n)
            return n
    def aleatoire(self):
        global id_bloc
        n = random.randint(1, self.nbr_bloc)
        while id_bloc == n:
            n = random.randint(1, self.nbr_bloc)
        id_bloc = n
    def get_new_bloc_proposition(self):
        global id_bloc
        self.current_proposition = []
        for i in range((id_bloc - 1) * self.nbr_prop_par_bloc,id_bloc * self.nbr_prop_par_bloc):
            self.current_proposition.append(self.propo[i][0])
        return self.current_proposition

id_bloc = random.randint(1, 4)


