//Exercise 1 : Age Difference
let bornFirst = prompt("put a year of born", "1986")
let bornSecond = prompt("put a second year of born", "2010")
middleDate = 0

if (bornSecond > bornFirst) {(middleDate = Math.floor(((2023 - bornFirst )/2) + Number(bornSecond)))} else {(middleDate = Math.floor(((2023 - bornSecond )/2) + Number(bornFirst)))}
console.log(middleDate)

//Exercise 2 : Zip Codes first
let zipCode = prompt("put your zip code", "12345")
zipCode = zipCode.trim()

if (zipCode.length == 5 && isNaN(Number(zipCode)) == false) {console.log("success")} else {console.log("error")}

//Exercise 2 : Zip Codes second
let zipCode2 = prompt("put your zip code", "12345")

if (zipCode2.match(/\b\d{5}\b/g)) {console.log("success")} else {console.log("error")}

//Exercise 3 : Secret Word
let var1 = prompt("put a word", "word")
const noVowels = var1.replace(/[aeiou]/gi, '');
console.log(noVowels)

// Bonus: Replace the vowels with another character and console.log the result
let var2 = prompt("put a word", "word")
const regA = (/a{1,}/g)
const regE = (/e{1,}/g)
const regI = (/i{1,}/g)
const regO = (/o{1,}/g)
const regU = (/u{1,}/g)


newString = var2.replace(regA, "1") 
newString1 = newString.replace(regE, "2")
newString2 = newString1.replace(regI, "3")
newString3 = newString2.replace(regO, "4")
newString4 = newString3.replace(regU, "5")

console.log(newString4);
