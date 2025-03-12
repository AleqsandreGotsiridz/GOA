#2) შემენით tuple, რომელშიც შეინახავთ საყიდლების სიას და მოახდინეთ მათი unpacking (დაშლა),რათა მიანიჭოთ თითოეული ელემენტი ცალკეულ ცვლადებს და დაბეჭდეთ ეს ცვლადები.
Guitar_shopping = ("Acoustic,Fender", "Classical,Yamaha", "Electric,Fender" )
(item1, item2, item3) = Guitar_shopping
print(item2)

#3) შექმენით tuple და შეინახეთ Fast food პროდუქტები. შემდეგ შეცვალეთ ეს tuple და მათში ჩაამატეთ ჯანსაღი საკვები პროდუქტები.
Fast_food = ("Burger", "Frie", "Pizza")
Fast_food = list(Fast_food)
Fast_food[0] = "Salad"
Fast_food[1] = "Water"
Fast_food[2] = "Vegetables"
print(tuple(Fast_food))

#4) კომენტარის სახით ახსენით, თუ რა ფუნქციას ასრულებს Asterisk და როგორ აღინიშნება ის.
#Asterisk - ვიყენებთ როცა გვინდა ელემენტები სხვა თაფლში მოვაქციოთ.

#5) მოცემულია შემდეგნაირი tuple:
months = ("January", "February", "March", "April",)
(first, second, third, fourth)= months

#რას გამოიტანს მოცემული კოდი?print(first)
#print(second)
#print(third)
#print(fourth)