const searchBox = document.getElementById('search-box')
const searchBtn = document.getElementById('search-btn')
const results = document.getElementById('results')
const status = document.getElementById('status')

searchBtn.addEventListener('click', () => {
    const query = searchBox.value
    fetch("http://127.0.0.1:8000/search?query=" + query)
        .then(response => response.json())
        .then(data => {
            results.innerHTML = ""
            data.metadatas[0].forEach(function(item, index) {
                results.innerHTML += `
                    <div class="result-card">
                        <a href="${item.url}" target="_blank">${item.title}</a>
                        <p>${item.chunk}</p>
                    </div>
                `
            })
        })
})
