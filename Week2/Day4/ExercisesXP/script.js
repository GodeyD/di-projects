// Exercise 1 : Information
// Part I : function with no parameters
function infoAboutMe() {
    console.log('I go to gym 5 times a week')
}
infoAboutMe()

// Part II : function with three parameters
function infoAboutPerson(personName, personAge, personFavoriteColor) {
    console.log(`You name is ${personName}, you are ${personAge} years old, your favorite color is ${personFavoriteColor}`)
}
infoAboutPerson("David", 45, "blue")
infoAboutPerson("Josh", 12, "yellow")

//  Exercise 2 : Tips
function calculateTip() {
    let bill = prompt('Bill amount', '200')
    if (bill < 50) {
        console.log(`${bill} + 20%`)
    } else if (bill <= 200) {
        console.log(`${bill} + 15%`)
    } else {
        console.log(`${bill} + 10%`)
    }
}
calculateTip()

// Exercise 3 : Find The Numbers Divisible By 23
function isDivisible() {
    let divisibl23 = ''
    let sum = 0
    for (let i = 0; i < 500; i++) {
        if (i % 23 == 0) {
            divisibl23 += `${i} `
            sum += i
        }
    }
    console.log(`Outcome : ${divisibl23}`)
    console.log(`Sum : ${sum}`)
}
isDivisible()

// Bonus: Add a parameter divisor to the function.
let divisor = prompt('put a number for divisor', '9')

function isDivisibleD(divisor) {
    let divisibl23 = ''
    let sum = 0
    for (let i = 0; i < 500; i++) {
        if (i % divisor == 0) {
            divisibl23 += `${i} `
            sum += i
        }
    }
    console.log(`Outcome : ${divisibl23}`)
    console.log(`Sum : ${sum}`)
}
isDivisibleD(divisor)

// Exercise 4 : Shopping List
const stock = {
    "banana": 6,
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry": 1
}

const prices = {
    "banana": 4,
    "apple": 2,
    "pear": 1,
    "orange": 1.5,
    "blueberry": 10
}

let shoppingList = ["banana", "orange", "apple"]

function myBill() {
    let sum = 0

    for (let i = 0; i < shoppingList.length; i++) {
        if (stock[shoppingList.at(i)] != 0) {
            if (shoppingList[i] in prices) {
                sum += prices[shoppingList.at(i)]
                stock[shoppingList.at(i)] -= 1
            }
        }
    }
    console.log(` Total price : ${sum}`)
}
myBill()

// Exercise 5 : What’s In My Wallet ?

let change = [0.25, 0.10, 0.05, 0.01]
// A quarters is 0.25
// A dimes is 0.10
// A nickel is 0.05
// A penny is 0.01

// let amountOfChange = [25, 20, 5, 0]

function changeEnough(itemPrice, amountOfChange) {
    let sumChange = 0
    for (let i = 0; i < change.length; i++) {
        let convertedChange = amountOfChange[i] * change[i]
        sumChange += convertedChange
    }
    if (itemPrice < sumChange) {
        return true
    } else {
        return false
    }
}

console.log(changeEnough(4.25, [25, 20, 5, 0]))
console.log(changeEnough(14.11, [2, 100, 0, 0]))
console.log(changeEnough(0.75, [0, 0, 20, 5]))

// Exercise 6 : Vacations Costs
function hotelCost(nights) {    
        // let nights = +prompt('how many nights?', '2')       
        // while (isNaN(nights)) {
        //     nights = +prompt('how many nights?', '2')
        // }
    let nightsCost = nights * 140
    return `the hotel cost: $${nightsCost} `
}


function planeRideCost(destination) {
    // let destination = prompt('where?', 'Paris');
    let destinationCost = 0;
    
    if (destination.toLowerCase().search('paris') != -1) {destinationCost += 220} else if (destination.toLowerCase().search('londom') != -1) {destinationCost += 183} else {destinationCost += 300};
    return `the plane to "${destination.charAt(0).toUpperCase() + destination.slice(1)}" cost: $${destinationCost}`;
}


function rentalCarCost(carDays) {
    // let carDays = prompt('how many days whant to rent a car?', '2')    
    // while (isNaN(carDays)) {
    //     carDays = +prompt('how many days whant to rent a car?', '2')
    // }
    let carCost = carDays * 40
    if (carCost >= 400) { carCost = carCost-carCost*5/100}
    return `The car cost: ${carCost}$ `
}


function totalVacationCost() {
    let nights = +prompt('how many nights?', '2')       
    while (isNaN(nights)) {
        nights = +prompt('how many nights?', '2')
    }
    let destination = prompt('where?', 'Paris')    
    let carDays = prompt('how many days whant to rent a car?', '2')    
    while (isNaN(carDays)) {
        carDays = +prompt('how many days whant to rent a car?', '2')
    }
console.log(`${rentalCarCost(carDays)}${hotelCost(nights)}${planeRideCost(destination)}`)

}
totalVacationCost()

