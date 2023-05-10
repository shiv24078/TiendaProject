document.addEventListener('DOMContentLoaded', function() {
    var productCards = document.querySelectorAll('.product-card');

    productCards.forEach(function(card) {
        card.addEventListener('click', function() {
            window.location = card.querySelector('.product-title').href;
        });
    });
});
