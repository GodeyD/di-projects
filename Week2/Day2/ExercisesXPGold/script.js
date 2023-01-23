//Exercise 1 : The World Translator
let language = prompt("which language you speak", "language").toLowerCase()

if (language == "french") {console.log("Bonjour")} else if (language == "english") {console.log("Hello")} else if (language == "hebrew") {console.log("Shalom")} else {console.log("01110011 01101111 01110010 01110010 01111001")}

//Exercise 2 : The Grade Assigner
let grade = prompt("Lets assign your grade", "number")

if (grade>90) {console.log("A")} else if (grade>80 && grade<=90) {console.log("B")} else if (grade>=70 && grade<=80) {console.log("C")} else {console.log("B")}

//Exercise 3 : Verbing
let newString = prompt("Put a verb", "verb")

if (newString.length >= 3 && newString.slice(-3) != "ing") {console.log(`${newString}ing`)} else if (newString.length >= 3 && newString.slice(-3) == "ing") {console.log(`${newString}ly`)} else {console.log(newString)}
