# Ask the user to input their name. Then print a nice welcome message
# that welcomes them personally to your script.
# If a user enters more than one name, e.g. "firstname lastname",
# then use only their first name to overstep some personal boundaries
# in your welcome message.


welcome_user = str(input('Enter your name (ex. firstname lastname): '))

display_firstname = welcome_user.split()[0]

print(f'Hello {display_firstname} welcome to my script!')