# a = 5
# b = 7
# print(a==b)# == <-- ტოლობა
# print(a!=b)# != <-- არ უდრის
# print(a>b)#  >  <-- მეტობა
# print(a<b)#  <  <-- ნაკლებობა
# print(a>=b)# >= <-- თუ მეტია ან უდრის
# print(a<=b)# <= <-- თუ ნაკლებია ან უდრის
#1)შექმენით ცვლადი სადაც მომხარებელს შემოატანინებ თავის ასაკს, input ის საშუალებით, და მერე შეამოწმე მეტია ის თუ არა 18 ზე, გამოიყენეტ შედარების ოპერატორები
age = float(input("please enter your age:"))
print(age > 18)
#2)რას გამოიტანს ეს კოდი(ახენით დეტალურად კომენტარებით) print(True and False or 5>2 and False or False and True)
print(True and False or 5>2 and False or False and True)
#ჯერ შედგება შედარება ხოლო შემდეგ and-or
#false უფრო or უყვარს True უფრო and
#საბოლოოდ ეს კოდი გამოიტანს False
