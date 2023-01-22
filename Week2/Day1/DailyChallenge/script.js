//Exercise 1 : Evaluation

5 >= 1 //true 5 is biger than 1
0 === 1 //false 0 is not equal to 1
4 <= 1 //false 4 is not biger than 1
1 != 1 //false 1 is not diferent than 1
"A" > "B" //i dont now //false
"B" < "C" //i dont now //true
"a" > "A" //i dont now //true
"b" < "A" //i dont now //false
true === false //false, true is diferent than false 
true != true //false, true its no diferent than true

//Exercise 2 : Ask For Numbers

number1 = prompt("a number plz", "number 1")
number2 = prompt("a 2nd number plz", "number 2")
arrayNumbers = [Number(number1), Number(number2)]

console.log(arrayNumbers[0]+arrayNumbers[1])

//Exercise 3 : Find Nemo

sentenceNemo = prompt(`"Give a sentence containing the word "Nemo"`, "plz put Nemo") 
sentenceArray = sentenceNemo.split(" ")
nemo = "Nemo"
findNemo = sentenceArray.includes(nemo)

if (findNemo == true) {whereNemo = sentenceArray.indexOf(`Nemo`)} else { console.log('I can’t find Nemo')}

if (findNemo == true) {console.log(`"I found Nemo at ${whereNemo}"`)}

//Exercise 4 : Boom

returnNumber = prompt("put a number", "1")
bigThan1 = Array(Number(returnNumber)+1).join("o")
if (returnNumber<2) {console.log("boom")} else if (Number(returnNumber) % 2 === 0 && Number(returnNumber) % 5 === 0) {console.log(`B${bigThan1}m!`.toUpperCase())} else if (Number(returnNumber) % 5 === 0) {console.log(`B${bigThan1}m`.toUpperCase())} else if (Number(returnNumber) % 2 === 0) {console.log(`B${bigThan1}m!`)} else {console.log(`B${bigThan1}m`)}



