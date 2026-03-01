class Person:
    '''
    A class representing a person in a social network.
    Attributes:
        name (str): The name of the person.
        friends (list): A list of friends (Person objects).
    Methods:
        add_friend(friend): Adds a friend to the person's friend list.
   '''
    
    # pass # Delete this line to implement the Person class
    def __init__(self, name) :
     self.name = name
     self.friends = [ ]
    
    def add_friend(self, friend) :
    
      """Add a friend if already in List. """  
      if friend not in self.friends :
        self.friends.append(friend)



class SocialNetwork:
    '''
    A class representing a social network.
    Attributes:
        people (dict): A dictionary mapping names to Person objects.
    Methods:
        add_person(name): Adds a new person to the network.
        add_friendship(person1_name, person2_name): Creates a friendship between two people.
        print_network(): Prints the names of all people and their friends.
    '''
    
    # pass # Delete this line to implement the SocialNetwork class
    def __init__(self):
        self.people = {}

    def add_person(self, name):
        """Add a person if they don't already exist."""
        if name in self.people:
            print(f"{name} already exists in the network. - social_network.py:42")
        else:
            self.people[name] = Person(name)

    def add_friendship(self, person1_name, person2_name):
        """Create a two-way friendship."""
        if person1_name not in self.people:
            print(f"Friendship not created. {person1_name} doesn't exist! - social_network.py:49")
            return

        if person2_name not in self.people:
            print(f"Friendship not created. {person2_name} doesn't exist! - social_network.py:53")
            return

        person1 = self.people[person1_name]
        person2 = self.people[person2_name]

        person1.add_friend(person2)
        person2.add_friend(person1)

    def print_network(self):
        """Display all people and their friends."""
        for name, person in self.people.items():
            friend_names = [friend.name for friend in person.friends]
            friends_string = ", ".join(friend_names)
            print(f"{name} is friends with: {friends_string} - social_network.py:67")


# Test your code here

# Test Your Network
network = SocialNetwork()

# Add people
network.add_person("Alex")
network.add_person("Jordan")
network.add_person("Morgan")
network.add_person("Taylor")
network.add_person("Casey")
network.add_person("Riley")

# Edge case: duplicate person
network.add_person("Alex")

#Create friendships (at least 8)
network.add_friendship("Alex", "Jordan")
network.add_friendship("Alex", "Morgan")
network.add_friendship("Jordan", "Taylor")
network.add_friendship("Morgan", "Casey")
network.add_friendship("Taylor", "Riley")
network.add_friendship("Morgan", "Riley")
network.add_friendship("Casey", "Riley")
network.add_friendship("Alex", "Taylor")

# Edge case: person doesn't exist
network.add_friendship("Jordan", "Johnny")

print("n\"Social Newtwork - social_network.py:99")
network.print_network()

# Design Memo
# Here the design of Memo.
"""
For this Assignment a graph is the best data structure to represent 
a social network because it models
relationships between individuals in a flexible and natural way. Each person is a node,
and each friendship is an edge connecting two nodes. Social relationships are typically
bidirectional and non-hierarchical, meaning any person can connect to multiple others
without a fixed structure. Graphs are specifically designed to represent these complex,
many-to-many relationships efficiently
A list would not work well because lists store items in sequence and cannot easily
represent multiple connections between different individuals. For example, a list cannot
clearly show that one person is connected to many others at the same time without
duplicating data or creating complicated nested structures. A tree structure is also not
suitable because trees require a hierarchy with a single root and parent-child
relationships. Social networks do not have a central “top” person, and friendships exist
between peers rather than in hierarchical levels.
While implementing the social network, I noticed some trade-offs in performance and
structure. Using an adjacency list makes adding friendships very efficient because we
only need to append to a list, which is typically constant time. It also saves memory
because we only store actual connections rather than all possible ones. However, checking
whether a specific friendship exists may require searching through a list, which can take
longer if a person has many friends. Printing the network is straightforward but requires
iterating through all nodes and their connections. Overall, adjacency lists provide a
good balance between memory efficiency and flexibility for representing social networks.

"""
