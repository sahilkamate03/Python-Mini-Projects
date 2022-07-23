
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
        getTodoList()
    }

    function errorFn(xhr) {
        console.log('Error: ', xhr)
    }
    console.log(todo_id)
}


// $('form#formTodo').on('submit', function () {
//     var that = $(this),
//         url = that.attr('action'),  
//         method = that.attr('mehod'),
//         data = {${todoTitle}}
// })

// submitTodo = document.getElementById('submitTodo')
// submitTodo.addEventListener('click', addTodo)

// todoTitle = document.getElementById('todoTitle')
// todoTitle.addEventListener('change', addTodo)

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
            console.log(todoData)
            noTitle.style.display = 'none'
            getTodoList()
            document.getElementById("formTodo").reset();
        }

        function errorFn(xhr) {
            console.log('Error: ', xhr)
        }
    }
}

function getTodoList() {
    $.ajax({
        type: 'GET',
        url: '/getTable',
        success: successFn,
        error: errorFn
    })

    function successFn(result) {
        console.log(result)
        $("#todoList").html(result)
    }

    function errorFn(xhr) {
        console.log('Error: ', xhr)
    }
}
