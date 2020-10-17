# Initial variable to track game play
user_play = 'y'
# While we are still playing...
while user_play=='y':
    user_number = int( input("how many numbers?"))
    for x in range (user_number):
        print (x)
        user_play= input ("Continue: (y)es or (n)o?")

