#დაწერეთ პროგრამა, რომელიც სთხოვს მომხმარებელს გამოიცნოს პაროლი. პროგრამა კვლავ მოუწოდებს მოსთხვოს პაროლის შეყვანას, სანამ არ გამოიცნობს სწორ პაროლს.
password = "GOA_500"
guess = input("Please Enter password! ")

while guess != password:
    print("Please Try again!")
    guess = input("Its not correct") 
print("Its correct hell ya!")