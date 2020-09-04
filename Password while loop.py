# Set a password
PASSWORD = "Martin"

# Give the user 3 lives
attempts = 3

# Give the user 3 tries to guess the number, and tell them whether they are correct or not
while attempts > 0:
  guess = input("Enter your password")
  if guess == PASSWORD:
    print("Correct")
    attempts = 0
  else: 
    print("Wrong!")
    attempts -= 1
