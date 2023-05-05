const formularioComentario = document.getElementById('formulario-comentario');
const comentarios = document.getElementById('comentarios');

formularioComentario.addEventListener('submit', function(e) {
  e.preventDefault();

  const nombre = document.getElementById('nombre').value;
  const comentario = document.getElementById('comentario').value;

  const nuevoComentario = document.createElement('div');
  nuevoComentario.classList.add('comentario');
  nuevoComentario.innerHTML = `
    <h4>${nombre}</h4>
    <p>${comentario}</p>
  `;


  comentarios.appendChild(nuevoComentario);


  document.getElementById('nombre').value = '';
  document.getElementById('comentario').value = '';
});
imagenContenedor.addEventListener('mousemove', function(e) {
    const anchoContenedor = imagenContenedor.offsetWidth;
    const altoContenedor = imagenContenedor.offsetHeight;
    const originalAncho = imagenContenedor.dataset.originalAncho;
    const originalAlto = imagenContenedor.dataset.originalAlto;
  
    // calcular la posición del cursor en relación al contenedor
    const posicionX = e.offsetX;
    const posicionY = e.offsetY;
  
    // calcular la cantidad de zoom a aplicar
    const factorX = originalAncho / anchoContenedor;
    const factorY = originalAlto / altoContenedor;
    const zoomX = (posicionX / anchoContenedor) * factorX;
    const zoomY = (posicionY / altoContenedor) * factorY;
  
    // ajustar el tamaño de la imagen utilizando transform: scale()
    imagen.style.transform = `scale(${zoomX}, ${zoomY})`;
  });
  
  // restaurar el tamaño original de la imagen cuando se saca el cursor del contenedor
  imagenContenedor.addEventListener('mouseleave', function() {
    imagen.style.transform = 'scale(1)';
  });
  function toggleFavorite() {
    const button = document.getElementById("favorite-button");
    button.classList.toggle("active");
  }




