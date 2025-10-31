"""
Exercise 1: Mailing Address
(Solved—9 Lines)
Create a program that displays your name and complete mailing address formatted in
the manner that you would usually see it on the outside of an envelope. Your program
does not need to read any input from the user.
"""
my_name = "aaron"
address = {
    'street' : 'Calle norte 25',
    'number' : '9 int c104',
    'neighborhood': 'Moctezuma 2da seccion',
    "delegation" : 'Venustiano Carranza',
    'zip code' : 15530,
    'city': 'Ciudad De México'
    
}
print(f"Hello my name is {my_name} and i lived in {address['street']} {address['number']}, {address['neighborhood']},{address['delegation']}, {address['zip code']}, {address['city']}")
