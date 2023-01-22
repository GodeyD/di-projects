// exercise 1
const favoriteFood = "sushi"
const favoriteMeal = "dinner"

console.log(`I eat ${favoriteFood} every ${favoriteMeal}`)

//exercise 2 part 1
const myWatchedSeries = ["black mirror", "money heist", "the big bang theory"];
const myWatchedSeriesLength = myWatchedSeries.length
const lastOne = myWatchedSeriesLength-1
const myWatchedSeriesSentence = `${myWatchedSeries[0]}, ${myWatchedSeries[1]}, and ${myWatchedSeries[lastOne]}`

console.log(`I watched ${myWatchedSeriesLength} series : ${myWatchedSeriesSentence}`)

//exercise 2 part 1
myWatchedSeries[2] = "friens"
myWatchedSeries.push("arcane","the wicher")
myWatchedSeries.shift()
console.log(myWatchedSeries[0][2])
console.log(myWatchedSeries)

//exercise 3
let celsius = 24
const fahrenheit = celsius/5*9+32

console.log(`<${celsius}>°C is <${fahrenheit}>°F`)

//exercise 4
let c;
let a = 34;
let b = 21;

console.log(a+b) //first expression
// Prediction: 55 becouse "a" and "b" are element number and can be added
// Actual: 55

a = 2;

console.log(a+b) //second expression
// Prediction: 23 becouse the value of "a" is now 2 
// Actual: 23

//value of "c" is null
console.log(3 + 4 + '5');
//will outcome 75

//exercise 5
typeof(15)
// Prediction: number is the type
// Actual: number

typeof(5.5)
// Prediction: float is the type of a float
// Actual: number

typeof(NaN)
// Prediction: var "NaN" its a variable
// Actual: number

typeof("hello")
// Prediction: string is in betwen quotation marks
// Actual: string

typeof(true)
// Prediction: boolean (ture a false are boolean)
// Actual: boolean

typeof(1 != 2)
// Prediction: true (1 is diferent to 2)
// Actual: true

"hamburger" + "s"
// Prediction: hamburgers ( the concatenation of strings put it togheter)
// Actual: 

"hamburgers" - "s"
// Prediction: hamburger (i think its the oposit to concatenation)
// Actual: NaN

"1" + "3"
// Prediction: 13 (concatenation again)
// Actual: 13

"1" - "3"
// Prediction: i dont know
// Actual: -2

"johnny" + 5
// Prediction: johnny5 (concatenation string and number)
// Actual: johnny5

"johnny" - 5
// Prediction: i dont know
// Actual: NaN

99 * "hello"
// Prediction: i dont know
// Actual: NaN

1 != 1
// Prediction: false 1 is no diferent at 1
// Actual: false

1 == "1"
// Prediction: true == only compare the value dont the type so 1 is 1
// Actual: true

1 === "1"
// Prediction: false === compare the value and the type so 1 is diferent than "1"
// Actual: false