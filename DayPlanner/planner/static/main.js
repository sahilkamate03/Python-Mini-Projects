console.log('Flask App by: Sahil Kamate')

var today = new Date();
var dd = String(today.getDate()).padStart(2, '0');
var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0
var yyyy = today.getFullYear();

today = yyyy + '_' + mm + '_' + dd;

// undoTodo start
todoList_complete = document.getElementsByClassName('completeTodo')
Array.from(todoList_complete).forEach(element => {
    element.addEventListener('click', function (e) {
        undoTodo(e)
    });
})

undoTodo = (e) => {
    todo_id = e.target.children[0].innerText
    $.ajax({
        type: 'POST',
        url: '/todo/' + todo_id + '/undo',
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
}
// undoTodo ends

// completeTodo start
todoList_remaining = document.getElementsByClassName('remainingTodo')
Array.from(todoList_remaining).forEach(element => {
    element.addEventListener('click', function (e) {
        completeTodo(e)
    });
})

completeTodo = (e) => {
    todo_id = e.target.children[0].innerText
    $.ajax({
        type: 'POST',
        url: '/todo/' + todo_id + '/complete',
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
}
// completeTodo ends

// add todo starts
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
// add todo ends

// get todo starts
function getTodoList(dateSelected) {
    $.ajax({
        type: 'GET',
        url: '/' + dateSelected + '/getTable',
        success: successFn,
        error: errorFn
    })

    function successFn(result) {
        $(".remainingTodoList").html(result['remain'])
        $(".completeTodoList").html(result['complete'])
    }

    function errorFn(xhr) {
        console.log('Error: ', xhr)
    }
}
// get todo ends

// datepicking function starts
var dateSelected;
var date_input = document.getElementById('todoDatePicker');
date_input.valueAsDate = new Date();

date_input.onchange = function () {
    dateSelected = this.value.split('-')
    dateSelected = dateSelected.join('_')
    getTodoList(dateSelected)
}
// datepicking function ends