#2) კომენტარის სახით ჩამოწერეთ თუ რა განსხვავებაა set-ებსა და list-ებს შორის.
#3) შექმენით set სადაც შეინახავთ რიცხვებს, შემდეგ კი ინდექსინგის საშუალებით სცადეთ თითოეული ელემენტის შეცვლა და დააკვირდით შედეგს.

#4) შექმენით set, რომელშიც შენახული გექნებათ Fast food საკვები პროდუქტები. შემდეგ კი ამოშალეთ ყველა პირვანდელი ელემენტები set-იდან, და მათ ნაცვლად დაამატეთ ჯანსაღი საკვები პროდუქტები.

#5) შექმენით ფუნქცია, რომელიც არგუმენტად იღებს სიას, და აბრუნებს იგივე სიას, მაგრამ დუპლიკატების გარეშე. hint: გააკეთეთ set-ის საშუალებით (output-ში ელემენტების თანმიმდევრობას მნიშვნელობა არ აქვს)
#test cases:

    #list1 = [7, 5, 44, 14, 5, 5, 44]
    #list2 = [89, 90, 56, 45, 90, 78, 90]
                               
                                  #2)
#set-ებსა და list-ებს შორის განსხვავებაა ის რომ set-ებს არ აქვთ ინდექსი, და ისინი არ იძლევიან ერთსა და იმავე მნიშვნელობის ერთდროულად შენახვას.

                                  #3)
numbers = {1, 2, 3, 4, 5}
my_list = list(numbers)
my_list[0] = 66
my_list[1] = 22
my_list[2] = 33
my_list[3] = 45
my_list[4] = 55
print(my_list)

                                  #4
fast_food = {"burger", "fry", "burger", "pizza"}
my_list = list(fast_food)
my_list.remove("burger")
my_list.remove("fry")
my_list.remove("pizza")
my_list.append("salad")
my_list.append("sandwich")
my_list.append("carrot")
my_list.append("apple")
print(my_list)

                                  #5)
def remove_duplicates(input_list):
    return list(set(input_list))
print(remove_duplicates([1, 2, 2, 3, 4, 4]))
