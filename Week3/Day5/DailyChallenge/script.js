const tasks = []
const firstForm = document.forms[0];


firstForm.addEventListener("submit", addTask);

function addTask(evt) {
    correctTask = true
    const input = firstForm.querySelector('input')
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
    let newTask = document.createElement('div')
    let newTextNode = document.createTextNode(`${tasks[tasks.length - 1]}`)
    newTask.appendChild(newTextNode)
    let list = document.getElementsByClassName('listTasks')[0]
    list.appendChild(newTask)
    }
}