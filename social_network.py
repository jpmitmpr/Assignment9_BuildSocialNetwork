""" class Person:
    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)

class SocialNetwork:
    def __init__(self):
        self.people = {}

    def add_person(self, name):
        if name in self.people:
            print(f"{name} already exists in the network!")
        else:
            self.people[name] = Person(name)

    def add_friendship(self, person1_name, person2_name):
        if person1_name not in self.people:
            print(f"Friendship not created. {person1_name} doesn't exist!")
            return
        if person2_name not in self.people:
            print(f"Friendship not created. {person2_name} doesn't exist!")
            return
    
        person1 = self.people[person1_name]
        person2 = self.people[person2_name]

        person1.add_friend(person2)
        person2.add_friend(person1)

    def print_network(self):
        for name, person in self.people.items():
            friends_names = [friend.name for friend in person.friends]
            print(f"{name} is friends with: {', '.join(friends_names)}") """


# Test your code here

class Person:
    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)

class SocialNetwork:
    def __init__(self):
        self.people = {}

    def add_person(self, name):
        if name in self.people:
            print(f"{name} already exists in the network!")
        else:
            self.people[name] = Person(name)

    def add_friendship(self, person1_name, person2_name):
        if person1_name not in self.people:
            print(f"Friendship not created. {person1_name} doesn't exist!")
            return
        if person2_name not in self.people:
            print(f"Friendship not created. {person2_name} doesn't exist!")
            return

        person1 = self.people[person1_name]
        person2 = self.people[person2_name]

        person1.add_friend(person2)
        person2.add_friend(person1)

    def print_network(self):
        for name, person in self.people.items():
            friends_names = [friend.name for friend in person.friends]
            print(f"{name} is friends with: {', '.join(friends_names)}")

if __name__ == "__main__":
    network = SocialNetwork()

    network.add_person("JP")
    network.add_person("Gabriel")
    network.add_person("Miguel")
    network.add_person("Sonia")
    network.add_person("Jose")
    network.add_person("Rosa")

    network.add_friendship("JP", "Gabriel")
    network.add_friendship("JP", "Miguel")
    network.add_friendship("Gabriel", "Sonia")
    network.add_friendship("Gabriel", "Johnny")  # Should print error with Jhonny
    network.add_friendship("Miguel", "Jose")
    network.add_friendship("Sonia", "Rosa")
    network.add_friendship("Jose", "Rosa")
    network.add_friendship("Miguel", "Rosa")
    network.add_friendship("JP", "Sonia")

    network.print_network()