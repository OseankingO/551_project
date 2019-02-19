


class Group:
    __slots__ = ("group_num", "group_name", "size", "size_used", "term", "balance", "users", "group_holder")

    temperate_group_num = 1

    def __init__(self, group_name, size, term, user):
        if Group.temperate_group_num >= 999999:
            print("The size is full!")
            return
        self.group_name = group_name
        self.size = size
        self.term = term
        self.users = dict()
        self.size_used = 0
        self.group_holder = user
        self.group_num = "{:06}".format(Group.temperate_group_num)
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
        if self.size_used >= self.size:
            print("The group is full")
            return
        self.users[user.username] = user
        self.size_used += 1
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
            self.size_used -= 1
            user.delete_group(self.group_num)
            print(user_name, "deleted")
        else:
            print("This user is not in the group!")
            return

 #   def create_add_member_request(self, user):
