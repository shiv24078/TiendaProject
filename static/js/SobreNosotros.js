const image = document.querySelector("img");
const modal = document.querySelector(".modal");
const modalImage = document.querySelector(".modal img");

image.addEventListener("click", function() {
  modal.style.display = "block";
  modalImage.src = this.src;
});

modal.addEventListener("click", function() {
  modal.style.display = "none";
});
var map = L.map('map').setView([51.505, -0.09], 13);
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);