

Um diese Applikation zu starten, müssen die requirements installiert werden.
Dafür gebe den command pip install -r requirements.txt ein.

 python manage.py makemigrations
 python manage.py migrate
 python runserver

Um das Backend in einer Frontend Applikation zu implementieren muss folgende API im Frontend integriert werden.
Folgender Code muss noch für eigene Zwecke entsprechend angepasst werden

Local oder alternativ mit **********pythonanywhere.com/ ersetzen WICHTIG HTTPS!!!
URLS

http://127.0.0.1:8000/todos/
http://127.0.0.1:8000/categories/
http://127.0.0.1:8000/subtasks/

Für Updates 

http://127.0.0.1:8000/todos/${ID}/
http://127.0.0.1:8000/categories/${ID}/
http://127.0.0.1:8000/subtasks/${ID}/

method = 'POST'


async function getTodos() {
    try {
        let responseServer = await fetch('http://127.0.0.1:8000/todos/', { method: 'GET', headers: { 'Content-Type': 'application/json', } });
        if (!responseServer.ok)
            throw new Error("Response not ok")
        const tasks = await responseServer.json();
        console.log(tasks);
    }
    catch (error) {
        console.error(error)
    }
}
async function getCategories() {
    try {
        let responseServer = await fetch('http://127.0.0.1:8000/categories/', { method: 'GET', headers: { 'Content-Type': 'application/json', } });
        if (!responseServer.ok)
            throw new Error("Response not ok")
        const tasks = await responseServer.json();
        console.log(tasks);
    }
    catch (error) {
        console.error(error)
    }
}
async function getSubtasks() {
    try {
        let responseServer = await fetch('http://127.0.0.1:8000/subtasks/', { method: 'GET', headers: { 'Content-Type': 'application/json', } });
        if (!responseServer.ok)
            throw new Error("Response not ok")
        const tasks = await responseServer.json();
        console.log(tasks);
    }
    catch (error) {
        console.error(error)
    }
}


async function postTodo() {
    let a = 'Test1titte'
    let b = 'Test1desc'
    let c = 'MA'
    let d = 'H'
    let e = 'Hans Wurst'
    let f = '12/30/2022' // Format DD//MM//YYYY Wichtig
    let s1 = "Aufgabe1"
    let s2 = "Aufgabe2"
    let categoriesid = ''
    // ... ff
    var data = JSON.stringify({
        "title": a, "description": b, "categories": [
            {
               
                "title": "Backoffice",
                "color": "brown"
            }
        ], "priority": d, "user": e, "due_date": f, "subtasks": [
            {

                "title": "def",
                "done": "false"
            },
            {

                "title": "abc",
                "done": "false"
            }
        ]
    });
    console.log(data)
    fetch('http://127.0.0.1:8000/todos/', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: data
    })
        .then(response => response.json())
        .then(response => console.log(JSON.stringify(response)))
}

async function postCategory() {
    let title = 'Marketing'
    let color = 'green'

    // ... ff
    var data = JSON.stringify({
        "title": title,
        "color": color
    });
    console.log(data)
    fetch('http://127.0.0.1:8000/categories/', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: data
    })
        .then(response => response.json())
        .then(response => console.log(JSON.stringify(response)))
}

async function postSubtask() {
    let title = 'Test1tit'
    let done = 'true'

    // ... ff
    var data = JSON.stringify({
        "title": title,
        "color": done
    });
    console.log(data)
    fetch('http://127.0.0.1:8000/subtasks/', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: data
    })
        .then(response => response.json())
        .then(response => console.log(JSON.stringify(response)))
}

async function updateTodo() {
    let a = 'Test1titte'
    let b = 'Test1desc'
    let c = 'MA'
    let d = 'H'
    let e = 'Hans Wurst'
    let f = '12/30/2022' // Format DD//MM//YYYY Wichtig
    let s1 = "Aufgabe1"
    let s2 = "Aufgabe2"
    let categoriesid = ''
    // ... ff
    var data = JSON.stringify({
        "title": a, "description": b, "categories": [
            {
               
                "title": "Backoffice",
                "color": "brown"
            }
        ], "priority": d, "user": e, "due_date": f, "subtasks": [
            {

                "title": "def",
                "done": "false"
            },
            {

                "title": "abc",
                "done": "false"
            }
        ]
    });
    console.log(data)
    fetch('http://127.0.0.1:8000/todos/', {
        method: 'PUT',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: data
    })
        .then(response => response.json())
        .then(response => console.log(JSON.stringify(response)))
}