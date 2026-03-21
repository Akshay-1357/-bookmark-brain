const url = window.location.href
const title = document.title


const content = document.body.innerText.slice(0,5000)


function sendToBackend(){
    console.log("Sending to backend...")
    fetch("http://127.0.0.1:8000/store", {
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
console.log("Bookmark Brain content.js loaded on:", url)

chrome.storage.local.get('capturing', function(data) {
    const isOn = data.capturing !== false
    if (isOn) {
        setTimeout(sendToBackend, 20000)
    }
})
