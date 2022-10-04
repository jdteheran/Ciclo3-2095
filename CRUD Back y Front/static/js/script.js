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


    if (validacion()) {

        const estudiante = {
            nombre: nombre.value,
            apellido: apellido.value,
            celular: celular.value,
            correo: correo.value,
            contrasena: pass.value
        }

        fetch('/home', {
            method: 'POST',
            body: JSON.stringify(estudiante),
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(res => res.text())
            .then(response => {
                consultar_todos_estudiantes()
            })
            .catch(error => console.error('Error:', error))

    }
})

function consultar_todos_estudiantes() {
    fetch('/get_all_students')
        .then(res => res.json())
        .then(response => {
            llenar_tabla(response)
            ver_lista()
        })
        .catch(error => console.log('Error:', error))
}

function llenar_tabla(estudiantes) {
    let cuerpo_table = document.querySelector('tbody')
    cuerpo_table.innerHTML = ''
    estudiantes.forEach(estudiante => {
        let template_registro = `<tr>
                                    <th scope="row">${estudiante[0]}</th>
                                    <td>${estudiante[1]} - ${estudiante[2]}</td>
                                    <td>${estudiante[3]}</td>
                                    <td>
                                        <button class="btn btn-success ver">Ver</button>
                                        <button class="btn btn-warning editar">Editar</button>
                                        <button class="btn btn-danger eliminar">Eliminar</button>
                                    </td>
                                </tr>`

        cuerpo_table.innerHTML = cuerpo_table.innerHTML + template_registro
    });
}

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
