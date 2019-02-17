


class Group:
    __slots__ = ("group_num", "group_name", "size", "term", "balance", "users", "group_holder")

    temperate_group_num = 1

    def __init__(self, group_name, size, term, user):
        self.group_name = group_name
        self.size = size
        self.term = term
        self.users = dict()
        self.group_holder = user
        num = str(self.temperate_group_num)
        length = 6 - len(num)
        temp = ""
        for i in range(length):
            temp += "0"
        self.group_num = temp + num
        Group.temperate_group_num += 1

    def get_group_name(self):
        return self.group_name

    def get_group_num(self):
        return self.group_num

    def get_size(self):
        return self.size

    def get_term(self):
        return self.term

    def get_balance(self):
        return self.balance

    def get_user_name_list(self):    # return a list of user name
        name = list(self.users.keys())
        return name

    def add_user(self, user):
        if user.get_username() in self.users:
            print("This user has already been in the group")
            return
        self.users[user.username] = user
        user.add_group(self.group_num, self)

    def get_user(self, username):
        if username in self.users:
            return self.users[username]
        print("This user is not in the group!")
        return

    def check_user(self, user):
        if user.get_username() in self.users:
            return True
        return False

    def delete_user(self, user):
        user_name = user.get_username()
        if user_name in self.users:
            self.users.pop(user_name)
            user.delete_group(self.group_num)
            print(user_name, "deleted")
        else:
            print("This user is not in the group!")
            return

