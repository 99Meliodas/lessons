def number_to_choice(number):
    dict_ = {1: "Usain", 2 : 'Me', 3 : 'Aybek'}
    return dict_[number]
def test_number_to_choice():
   assert number_to_choice(1) == 'Usain'
   assert number_to_choice(2) == 'Me'
   assert number_to_choice(3) == 'Aybek'
   print("YOUR CODE IS CORRECT!")
print (test_number_to_choice())