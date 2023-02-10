const tasks = []
const firstForm = document.forms[0];


firstForm.addEventListener("submit", addTask);

function addTask(evt) {
  evt.preventDefault()
  correctTask = true
  const input = firstForm.querySelector('input')
  tasks.forEach(function (tsk) {
    if (tsk == input.value) {
      console.log('task already exists')
      list.appendChild(newTask)
    } else {
      console.log('task created');
    }
  })
  if (input.value.length == 0) {
    correctTask = false
    evt.preventDefault()
    console.log(correctTask)
    alert('plz create a task')
  } else if (tasks[tasks.length - 1] != input.value) {
    tasks.push(input.value)
    correctTask = true
  } else {
    correctTask = false
    console.log(correctTask);
    evt.preventDefault()
    alert('put a diferent task')
  }
  if (correctTask == true) {
    let newDiv = document.createElement('div')
    newDiv.classList.add('task')
    let newTask = document.createElement('label')
    let newTextNode = document.createTextNode(`${tasks[tasks.length - 1]}`)
    let checkbox = document.createElement('input')
    checkbox.setAttribute('type', "checkbox")
    checkbox.setAttribute('id', "addTask")
    newTask.setAttribute('for', "addTask")
    newTask.appendChild(newTextNode)
    newTask.classList.add('fa-solid', 'fa-square-xmark')
    let list = document.getElementsByClassName('listTasks')[0]
    list.appendChild(newDiv)
    newDiv.appendChild(checkbox)
    newDiv.appendChild(newTask)
  }
  }

