#შექმენით პროგრამა, რომელიც სთხოვს მომხმარებელს გამოიცნოს პაროლი. პროგრამა კვლავ მოუწოდებს მოსთხვოს პაროლის შეყვანას, სანამ არ გამოიცნობს სწორ პაროლს.
password = "GOA 500"
guess = input("Please Enter password! ")

while guess != password:
    print("Please Try again!")
    guess = input("Try again") 
print("Its correct good job!")