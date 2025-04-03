#mad_lib_project

name = input("Enter a name: ")
place = input("Enter a place: ")
activity = input("Enter an activity: ")
adjective = input("Enter an adjective: ")
food = input("Enter a type of food: ")


story = f"""
Once upon a time, {name} went to {place}. 
It was a {adjective} day, and {name} decided to {activity}.
After that, they enjoyed some delicious {food}.
It was a perfect adventure!
"""

print("Here is your story!")
print(story)