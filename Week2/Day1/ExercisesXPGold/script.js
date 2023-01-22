//Exercise 1 : Favorite Color
let sentence = ["my","favorite","color","is","blue"];
console.log(sentence.join(" "))

//Exercise 2 : Mixup
let str1 = "hello";
let str2 = "world";
str1Mix = `${str2.slice(0, 2)}`+`${str1.slice(2, )}`
str2Mix = `${str1.slice(0, 2)}`+`${str2.slice(2, )}`
console.log(str1)
console.log(str2Mix)
let str3 = `${str1Mix}`+` ${str2Mix}`
console.log(str3)

//Exercise 3 : Calculator
let num1 = prompt("put first number", "Number")
let num2 = prompt("put second number", "Number")
alert("SUM = "+ Number(num1) + Number(num2) + " REST = "+ (Number(num1) - Number(num2))+ " MULT = "+ Number(num1) * Number(num2) + " and DIV = " + Number(num1) / Number(num2)  )
