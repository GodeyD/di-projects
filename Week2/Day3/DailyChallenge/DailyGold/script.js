const numbers = [5,0,9,1,7,4,2,6,3,8]

console.log(numbers.toString())
console.log(numbers.join("+"))
console.log(numbers.join(" "))
console.log(numbers.join(""))

let numbersDecrease = []

for (var i = numbers.length - 1; i >= 0; i--) {
    numbersDecrease.push(numbers.sort()[i])    
}

console.log(numbersDecrease)