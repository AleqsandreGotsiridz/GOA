let lst = [13,12,"Goa","Aleqsa"]
console.log(lst.length) //ზომავს ჩვენი სიის სიგრძეს
console.log(lst.toString()) //გადაყავს ელემენტები ერთ სტრინგად
console.log(lst.at()) //არის ცუდი მეთოდი ელემენტების გამოსატანად at-იგივე ინდექსინგია
console.log(lst.join()) //არის იგივე რამ რაც toString თუ ბრჩხილებში არაფერს არ დავწერთ მაგრამ თუ კი მასში მძიმეს ჩავწერთ ჩაემატება ელემენტებს
console.log(lst.pop()) //აგდებს ელემენტს სიის ბოლოდან
console.log(lst.push()) //იგივე რაც append-ი ანუ სიაში ამატებს ელემენტს 
console.log(lst.shift()) //შლის სიის პირველ ელემენტს
console.log(lst.unshift()) //ამატებს ახალ ელემენტს სიაში მაგ:1,"str",rr...
console.log(lst.delete()) //ინდეგსინგით ვშლით ელემენტს და მის მაგივრად underfined
console.log(lst.concat()) //სხვა სიას აერთიანებს რაიმე სიასთანდ და ერთ სიად გარდაქმნის
console.log(lst.copyWithin()) //შეგვიძლია დავაკოპიროთ ელემენტები ინდექსინგის მიხედვით
console.log(lst.slice()) //იგივე არის რაც slicing-ი უბრალოდ სხვა სინტაქსი აქვს 

