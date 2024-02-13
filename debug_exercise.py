# IMPORTANT
# (1) For each exercise, copy the code to https://www.online-python.com/ and try it out. 
# (2) Do not use AI or any debugging tool for these exercises. 

# Exercise 1 Wrong output. Try to find and fix the bug(s)
def is_odd_number(num):
  if num % 2 == 0:
    return True 
  else:
    return False 

print(is_odd_number(4)) # Expected False
print(is_odd_number(7)) # Expected True



# Exercise 2 Wrong output. Try to find and fix the bug(s)
def calculate_divide(number, divisor):
  return number // divisor

print(calculate_divide(10, 2)) # Expected 5
print(calculate_divide(10, 3)) # Expected 3.33

# Exercise 3: Read the error output and fix the bug
def greet_user(name):
   result = f"Hello {name}"
    return result

print(greet_user("John")) # Expected: Hello John


# Exercise 4: This program converts a username to an email address, but it's buggy. Try to find and fix the bug(s).

# Remove special characters and space from the username
def remove_special_char(username):
  updated_username = ""
  for char in username:
    if char in ";.@#$%ˆ&*:_ ":
      updated_username += char
  return updated_username

# add the @ symbol at the end of the username
def add_at_symbol(username):
  return username + "@"

# add the domain (mail.com) name to the username
def add_domain_name(username):
  return "mail" + username + ".com"

# call the main function
def main():
  username = "user&#123_ @" # username we want to convert to email
  new_username = remove_special_char(username)
  new_username_with_at = add_at_symbol(new_username)
  user_email = add_domain_name(new_username_with_at)
  print(user_email) # Expected user12@mail.com
