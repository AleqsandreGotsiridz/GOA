#1) შექმენით dictionary სადაც შეინახავთ მინიმუმ 3 key'ს და ასევე შექმენით 2 ცარიელი სია for loop'ის დახმარებით პირველ სიაში დაამატეთ key
# ხოლო მეორე სიაში კი value ბოლოს კი გამოიტანეთ ერთად. 
dict = {
    "name": "sandro",
    "age": 12,
    "city": "tbilisi"
}
list1 = []
list2 = []
for key, value in dict.items():
    list1.append(key)
    list2.append(value)

print(list1,list2)