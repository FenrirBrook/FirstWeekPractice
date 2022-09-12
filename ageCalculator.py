def caltulate_age_in_decades(age):
    return age % 10

age_input = input("Enter your age: ")
# try: 
age = int(age_input)
years = age % 10
print("{}{}".format(caltulate_age_in_decades(age), years))
    
# except ValueError:
print(f'please enter a number:', {age_input}, " Is not valid")
    # raise

