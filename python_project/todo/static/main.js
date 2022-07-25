console.log('inside')

var today = new Date();
var dd = String(today.getDate()).padStart(2, '0');
var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
var yyyy = today.getFullYear();

today = yyyy + '_' + mm + '_' + dd;

todoList = document.getElementsByClassName('deleteTodo')
Array.from(todoList).forEach(element => {
    element.addEventListener('click', function (e) {
        completeTodo(e)
    });
})

completeTodo = (e) => {
    todo_id = e.target.children[0].innerText
    $.ajax({
        type: 'POST',
        url: '/todo/' + todo_id + '/delete',
        data: { "todo_id": todo_id },
        success: successFn,
        error: errorFn
    })

    function successFn(result) {
        if (!dateSelected) {
            dateSelected = today
            getTodoList(dateSelected)
        } else {
            getTodoList(dateSelected)
        }
    }

    function errorFn(xhr) {
        console.log('Error: ', xhr)
    }
    console.log(todo_id)
}

$(document).ready(function () {
    $(document).on('submit', '#formTodo', function () {
        addTodo()
        return false;
    });
});

function addTodo() {
    todoData = document.getElementById('todoTitle')
    noTitle = document.getElementById('noTitle')
    if (!todoData) {
        noTitle.style.display = ''
    }

    if (todoData) {
        $.ajax({
            type: 'POST',
            url: '/addTodo',
            data: { 'title': todoData.value },
            success: successFn,
            error: errorFn
        })

        function successFn(result) {
            noTitle.style.display = 'none'
            if (!dateSelected) {
                dateSelected = today
                getTodoList(dateSelected)
            } else {
                getTodoList(dateSelected)
            }
            document.getElementById("formTodo").reset();
        }

        function errorFn(xhr) {
            console.log('Error: ', xhr)
        }
    }
}

function getTodoList(dateSelected) {
    $.ajax({
        type: 'GET',
        url: '/' + dateSelected + '/getTable',
        success: successFn,
        error: errorFn
    })

    function successFn(result) {
        // console.log(result)
        $("#todoList").html(result)
    }

    function errorFn(xhr) {
        console.log('Error: ', xhr)
    }
}

var dateSelected;
var date_input = document.getElementById('todoDatePicker');
date_input.valueAsDate = new Date();

date_input.onchange = function () {
    dateSelected = this.value.split('-')
    dateSelected = dateSelected.join('_')
    getTodoList(dateSelected)
}

console.log(today);