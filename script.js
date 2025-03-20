function searchBooks() {
    let tag = document.getElementById('searchBox').value;
    fetch(`/search?tag=${tag}`)
        .then(response => response.json())
        .then(books => {
            let resultsDiv = document.getElementById('results');
            resultsDiv.innerHTML = '';
            books.forEach(book => {
                let bookElement = document.createElement('div');
                bookElement.classList.add('book');
                bookElement.innerHTML = `
                    <img src="/static/covers/${book[3]}" onclick="downloadBook('${book[4]}')">
                    <p>${book[1]}</p>
                `;
                resultsDiv.appendChild(bookElement);
            });
        });
}

function downloadBook(pdfFile) {
    window.location.href = `/static/ebooks/${pdfFile}`;
}
