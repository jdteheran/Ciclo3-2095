let btn_agregar = document.getElementById('agregar')


btn_agregar.addEventListener('click', () => {
    let seccion_registro = document.querySelector('.registro')
    let seccion_lista = document.querySelector('.lista')

    seccion_registro.style.display = 'block'
    seccion_lista.style.display = 'none'
})