window.addEventListener('load', function() {
  var section = document.getElementById('comprar-todas-las-armas');
  
  section.addEventListener('mouseover', function(event) {
    section.style.color = 'red';
  });
  
  section.addEventListener('mouseout', function(event) {
    section.style.color = '';
  });
});
