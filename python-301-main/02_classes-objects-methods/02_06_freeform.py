# Write a script with three classes that model everyday objects.
# - Each class should have an `__init__()` method that sets at least 3 attributes
# - Include a `__str__()` method in each class that prints out the attributes
#     in a nicely formatted string.
# - Overload the `__add__()` method in one of the classes so that it's possible
#     to add attributes of two instances of that class using the `+` operator.
# - Create at least two instances of each class.
# - Once the objects are created, change some of their attribute values.
#
# Be creative. Have some fun. :)
# Using objects you can model anything you want:
# Animals, paintings, card games, sports teams, trees, people etc...


class People:
    """Models a food item used as an ingredient."""

    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age 
        self.occupation = occupation

    def __add__(self, other):
        """Combines two ingredients."""
        wisdom = self.name + other.name
        if self.age >= other.age:
            return People(name=wisdom, age=self.age, occupation=self.occupation)
        else:
            return People(name=wisdom, age=other.age, occupation=other.occupation)
    
    def __str__(self):
        return f"Hello {self.name}, {self.age} years old, {self.occupation}"
    
    #def __repr__(self):
        #return f"Ingredient(name={self.name}, amount={self.amount})"

if __name__ == '__main__':
    c = People("mike", 35, 'gov')
    p = People("ai", 37, 'conbini')
    s = c + p
    print(s)


class FootballTeams():
    
    def __init__(self, team_name, mascot, games_won=0):
        self.team_name = team_name
        self.games_won = games_won
        self.mascot = mascot

    def __str__(self):
        return f'Team: {self.team_name}, Mascot: {self.mascot}, Wins: {self.games_won}'

    def total_wins(self):
        self.games_won += 1


f1 = FootballTeams('Patriots', 'Patriot')
print(f1)
f1.total_wins()
print(f1)
print()

f2 = FootballTeams('Kansas City', 'Football Team', 6)
print(f2)
f2.total_wins()
f2.total_wins()
print(f2)


from datetime import datetime, timedelta
class Breakfast():

    def __init__(self, food, drink, time_to_eat = None, refrigerator=None):
        self.food = food
        self.drink = drink
        self.refrigerator = refrigerator
        self.time_to_eat = time_to_eat or datetime.now()

    def fridge_is_full_or_empty(self):
        if self.refrigerator == True:
            return f'full'
        else:
            return f'empty. Time for a grocery store run!'

    def quick_breakfast(self):
        return f'Hurry current time is: {self.time_to_eat + timedelta(minutes=4)}'
        

    def __str__(self):
        return f'You had {self.food} with {self.drink} and your fridge is {self.fridge_is_full_or_empty()}' 


d1 = Breakfast('eggs', 'orange juice')
print(d1)
print(d1.fridge_is_full_or_empty())
print(d1)
print(d1.quick_breakfast())