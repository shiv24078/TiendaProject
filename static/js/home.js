window.addEventListener('load', function() {
  var section = document.getElementById('comprar-todas-las-armas');
  
  section.addEventListener('mouseover', function(event) {
    section.style.color = 'red';
  });
  
  section.addEventListener('mouseout', function(event) {
    section.style.color = '';
  });
});
var myCarousel = document.querySelector('#myCarousel')
var carousel = new bootstrap.Carousel(myCarousel, {
  interval: 4000,
  wrap: true
})
const miBoton = document.querySelector("#mi-boton");
miBoton.addEventListener("click", () => {
  alert("¡Haz hecho clic en el botón!");
});