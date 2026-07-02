function notification() {
    
    const hiddenBooks = document.querySelectorAll('.hidden-book');

    hiddenBooks.forEach(book => {
        book.classList.remove('hidden-book');
    });

    document.getElementById('exploreBtn').style.display = 'none';
}