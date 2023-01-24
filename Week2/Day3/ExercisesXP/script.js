// Exercise 1 : List Of People part 1
let people = ["Greg", "Mary", "Devon", "James"];
people.shift()
people.splice(2, 1, "Jason")
people.push("Diego")
console.log(people.indexOf("Mary"))
let copyPeople = people.slice(1, 3)
console.log(people.indexOf("Foo"))
// Write code that gives the index of “Foo”. Why does it return -1 ? becouse dont exist so the index is not in normal index
let last = people[people.length-1]
console.log(last)
console.log(copyPeople)

// Part 2
for (let i = 0; i <= people.length-1; i++) {
    console.log(people[i])
}

for (let i = 0; i <= people.length-1; i++) {
    if (i === people.indexOf("Jason")+1) { 
        break;
      }
    console.log(people[i])
}

// Exercise 2 : Your Favorite Colors
let colors = ["red", "black", "white", "blue", "orange"]

for (let i = 0; i<=colors.length-1; i++) {
    console.log(`My #${i+1} choice is ${colors[i]}`)
}
// bonus
let suffixes = ["frst", "scnd", "trd", "frd", "fv"]
for (let i = 0; i<=colors.length-1; i++) {
    console.log(`My #${suffixes[i]} choice is ${colors[i]}`)
}

// Exercise 3 : Repeat The Question
let newString = +prompt("put a number", "5")
console.log(typeof(newString))

while (newString<10) {
    newString = prompt("put a number", "10")
}

// Exercise 4 : Building Management
const building = {
    numberOfFloors: 4,
    numberOfAptByFloor: {
        firstFloor: 3,
        secondFloor: 4,
        thirdFloor: 9,
        fourthFloor: 2,
    },
    nameOfTenants: ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan:  [4, 1000],
        david: [1, 500],
    },
}
console.log(building.numberOfFloors)
console.log(building["numberOfAptByFloor"]["firstFloor"])
console.log(building["numberOfAptByFloor"]["thirdFloor"])
console.log(building["nameOfTenants"][1])
console.log(building["numberOfRoomsAndRent"]["dan"][0])

if ((building["numberOfRoomsAndRent"]["sarah"][1]+building["numberOfRoomsAndRent"]["david"][1])>building["numberOfRoomsAndRent"]["dan"][1]) {
    building["numberOfRoomsAndRent"]["dan"][1]=1200     
}

// Exercise 5 : Family
const family = {
    father: ["gustavo"],
    mother: ["diana"],
    son: ["diego"],
}

for (let i in family) {
    console.log(`${i}: ${family[i]}`)
}
// Exercise 6 : Rudolf
const details = {
    my: 'name',
    is: 'Rudolf',
    the: 'raindeer',
  }

  let detailsString = ""
  for (const [key, value] of Object.entries(details)) {    
    detailsString += `${key} ${value} `    
  }
  console.log(detailsString)

//   Exercise 7 : Secret Group
const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];

names.sort()
let secretS = ""
var myFunc = function (array) {
    for (var i = 0; i < array.length; i += 1) {       
      secretS += array[i].charAt(0)      
    }
    console.log(secretS)
}
myFunc(names)