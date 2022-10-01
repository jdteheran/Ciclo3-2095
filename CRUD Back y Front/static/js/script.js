let btn_agregar = document.getElementById('agregar')

let seccion_registro = document.querySelector('.registro')
let seccion_lista = document.querySelector('.lista')

btn_agregar.addEventListener('click', () => {

    if (btn_agregar.textContent == '+') {
        ver_registro('Cancelar', 'btn-danger')
    } else {
        ver_lista()
    }

})

function ver_registro(btn_text, class_btn) {
    seccion_registro.style.display = 'block'
    seccion_lista.style.display = 'none'

    btn_agregar.textContent = btn_text
    btn_agregar.setAttribute('class', `btn ${class_btn}`)
}

function ver_lista() {
    seccion_registro.style.display = 'none'
    seccion_lista.style.display = 'block'

    btn_agregar.textContent = '+'
    btn_agregar.setAttribute('class', 'btn btn-primary')
}

btn_crear = document.getElementById('crear')

btn_crear.addEventListener('click', (event) => {
    event.preventDefault()

    let nombre = document.getElementById('nombre')
    let apellido = document.getElementById('apellido')
    let celular = document.getElementById('celular')
    let correo = document.getElementById('correo')
    let pass = document.getElementById('contrasena')

    let id = uuidv4()

    if (validacion()) {
        let template_registro = `<tr>
                                    <th scope="row">${id}</th>
                                    <td>${nombre.value} - ${apellido.value}</td>
                                    <td>${correo.value}</td>
                                    <td>
                                        <button class="btn btn-success ver">Ver</button>
                                        <button class="btn btn-warning editar">Editar</button>
                                        <button class="btn btn-danger eliminar">Eliminar</button>
                                    </td>
                                </tr>`

        let cuerpo_table = document.querySelector('tbody')

        cuerpo_table.innerHTML = cuerpo_table.innerHTML + template_registro

        let estudiante = {
            id,
            nombre: nombre.value,
            apellido: apellido.value,
            celular: celular.value,
            correo: correo.value,
            pass: pass.value,
        }

        ver_lista()

        nombre.value = ''
        apellido.value = ''
        celular.value = ''
        correo.value = ''
        pass.value = ''
    }
})

function validacion() {

    let nombre = document.getElementById('nombre').value
    let apellido = document.getElementById('apellido').value
    let celular = document.getElementById('celular').value
    let correo = document.getElementById('correo').value
    let pass = document.getElementById('contrasena').value

    if (nombre.length < 3) { alert('El campo nombre es obligatorio, minimo 3 caracteres'); return false }
    if (apellido.length < 3) { alert('El campo apellido es obligatorio, minimo 3 caracteres'); return false }
    if (celular.length < 10) { alert('El campo celular es obligatorio, minimo 10 numeros'); return false }

    if (!/^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$/i.test(correo)) { alert('El correo no cumple con los requisitos'); return false }

    if (!/^(?=.*\d)(?=.*[\u0021-\u002b\u003c-\u0040])(?=.*[A-Z])(?=.*[a-z])\S{8,16}$/i.test(pass)) { alert('La contraseña debe tener al entre 8 y 16 caracteres, al menos un dígito, al menos una minúscula, al menos una mayúscula y al menos un caracter no alfanumérico.'); return false }

    return true
}
