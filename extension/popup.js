const searchBox = document.getElementById('search-box')
const searchBtn = document.getElementById('search-btn')
const results = document.getElementById('results')
const status = document.getElementById('status')

searchBtn.addEventListener('click', () => {
    const query = searchBox.value
    console.log("Searching for:", query)

    fetch("http://127.0.0.1:8000/search?query=" + query)
        .then(response => response.json())
        .then(data => {
            results.innerHTML = ""
const metadatas = data.metadatas[0]

metadatas.forEach(function(item, index) {
    const card = document.createElement('div')
    card.className = 'result-card'
    if (index >= 2) card.style.display = 'none'
    card.innerHTML = `
        <a href="${item.url}" target="_blank">${item.title}</a>
        <p>${item.chunk}</p>
    `
    results.appendChild(card)
})

if (metadatas.length > 2) {
    const showMore = document.createElement('button')
    showMore.innerText = "Show More"
    showMore.onclick = function() {
        document.querySelectorAll('.result-card').forEach(c => c.style.display = 'block')
        showMore.style.display = 'none'
    }
    results.appendChild(showMore)
}
        })
})
const toggle = document.getElementById('toggle')
const toggleLabel = document.getElementById('toggle-label')

chrome.storage.local.get('capturing', function(data) {
    const isOn = data.capturing !== false
    toggle.checked = isOn
    toggleLabel.innerText = isOn ? "Capturing: ON" : "Capturing: OFF"
})

toggle.addEventListener('change', function() {
    const isOn = toggle.checked
    chrome.storage.local.set({ capturing: isOn })
    toggleLabel.innerText = isOn ? "Capturing: ON" : "Capturing: OFF"
})
