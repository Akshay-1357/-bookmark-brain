const url = window.location.href
const title = document.title


const content = document.body.innerText.slice(0,5000)


function sendToBackend(){
    fetch("http://localhost:8000/store", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            url: url,
            title: title,
            content: content
        })
    })
}

setTimeout(sendToBackend, 30000)