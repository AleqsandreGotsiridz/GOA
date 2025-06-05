                                        //1
const inputi = int(prompt("Enter any number:"));
if(inputi / 2 == 0){
    console.log("'${inputi}' is even!");
}else{
    console.log("'${inputi} is odd!'");
}
                                        //2
let age = int(prompt("Enter your age:"));
if(age > 18){
    console.log("you are adult!");
}
else{
    console.log("You arent adult yet!!!");
}
                                        //4

let namelen = int(prompt("Enter your name:"))
if(namelen.lenght() == 6){
    console.log("hello my brother '${namelen}'")
}