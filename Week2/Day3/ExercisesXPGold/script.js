// Exercise 1 : Divisible By Three
let numbers = [123, 8409, 100053, 333333333, 7]

for (let i=0; i<numbers.length; i++) {
 console.log(numbers[i] % 3 === 0);
}

// Exercise 2 : Attendance
let guestList = {
    randy: "Germany",
    karla: "France",
    wendy: "Japan",
    norman: "England",
    sam: "Argentina"
  }

  let names = prompt("give me a name", "randy")
  if (names in guestList) {  
    console.log(`Hi! I'm ${names}, and I'm from ${guestList[names]}.`)  
  } else {
    console.log("Hi! I'm a guest.")
  }

//   Exercise 3 : Playing With Numbers
