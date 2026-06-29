var noticeForm = document.getElementById("noticeForm");
var avisoEditando = null;

if (noticeForm) {
    noticeForm.addEventListener("submit", async function (e) {
        e.preventDefault();

        var codigo = document.getElementById("codigoAviso").value;
        var cedula_usuario = document.getElementById("cedulaUsuarioAviso").value;
        var tipo_dano = document.getElementById("tipoDano").value;
        var descripcion = document.getElementById("descripcion").value;
        var ubicacion = document.getElementById("ubicacion").value;
        var fecha = document.getElementById("fechaAviso").value;
        var estado = document.getElementById("estadoAviso").value;

        var noticeData = {
            codigo: codigo,
            cedula_usuario: cedula_usuario,
            tipo_dano: tipo_dano,
            descripcion: descripcion,
            ubicacion: ubicacion,
            fecha: fecha,
            estado: estado
        };

        var url = API_URL + "/notices/add";
        var method = "POST";

        if (avisoEditando !== null) {
            url = API_URL + "/notices/update/" + avisoEditando;
            method = "PUT";
        }

        try {
            var res = await fetch(url, {
                method: method,
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(noticeData)
            });

            if (res.ok) {
                showMessage("Aviso guardado correctamente");
                clearNoticeForm();
                loadNotices();
            } else {
                var errorMessage = await getErrorMessage(res);
                showMessage(errorMessage, "error");
            }

        } catch (error) {
            console.error(error);
            showMessage("Error de conexión con la API", "error");
        }
    });

    loadUserOptions();
    loadNotices();
}

async function loadUserOptions() {
    var select = document.getElementById("cedulaUsuarioAviso");

    if (!select) {
        return;
    }

    try {
        var res = await fetch(API_URL + "/users/list");
        var data = await res.json();

        select.innerHTML = `<option value="">Seleccione un usuario</option>`;

        data.forEach(function (user) {
            select.innerHTML += `
                <option value="${user.cedula}">
                    ${user.cedula} - ${user.nombre}
                </option>
            `;
        });

    } catch (error) {
        console.error(error);
    }
}

async function loadNotices() {
    var tableBody = document.getElementById("noticesTable");

    if (!tableBody) {
        return;
    }

    try {
        var res = await fetch(API_URL + "/notices/list");

        if (!res.ok) {
            throw new Error("Error al cargar avisos");
        }

        var data = await res.json();

        tableBody.innerHTML = "";

        data.forEach(function (notice) {
            var row = `
                <tr>
                    <td>${notice.codigo}</td>
                    <td>${notice.cedula_usuario}</td>
                    <td>${notice.tipo_dano}</td>
                    <td>${notice.descripcion}</td>
                    <td>${notice.ubicacion}</td>
                    <td>${notice.fecha}</td>
                    <td>${notice.estado}</td>
                    <td>
                        <button class="action-btn edit-btn"
                            onclick="editNotice('${notice.codigo}', '${notice.cedula_usuario}', '${notice.tipo_dano}', '${notice.descripcion}', '${notice.ubicacion}', '${notice.fecha}', '${notice.estado}')">
                            Editar
                        </button>
                        <button class="action-btn delete-btn"
                            onclick="deleteNotice('${notice.codigo}')">
                            Eliminar
                        </button>
                    </td>
                </tr>
            `;

            tableBody.innerHTML += row;
        });

    } catch (error) {
        console.error(error);
        showMessage("No se pudieron cargar los avisos", "error");
    }
}

function editNotice(codigo, cedula_usuario, tipo_dano, descripcion, ubicacion, fecha, estado) {
    avisoEditando = codigo;

    document.getElementById("codigoAviso").value = codigo;
    document.getElementById("cedulaUsuarioAviso").value = cedula_usuario;
    document.getElementById("tipoDano").value = tipo_dano;
    document.getElementById("descripcion").value = descripcion;
    document.getElementById("ubicacion").value = ubicacion;
    document.getElementById("fechaAviso").value = fecha;
    document.getElementById("estadoAviso").value = estado;

    document.getElementById("codigoAviso").disabled = true;

    showMessage("Modo edición activado");
}

function clearNoticeForm() {
    avisoEditando = null;

    document.getElementById("noticeForm").reset();
    document.getElementById("codigoAviso").disabled = false;
}

async function searchNotice() {
    var codigo = document.getElementById("searchCodigoAviso").value.trim();
    var tableBody = document.getElementById("noticesTable");

    if (!codigo) {
        showMessage("Digite el código del aviso", "error");
        return;
    }

    try {
        var res = await fetch(API_URL + "/notices/search/" + codigo);

        if (!res.ok) {
            throw new Error("Aviso no encontrado");
        }

        var notice = await res.json();

        tableBody.innerHTML = `
            <tr>
                <td>${notice.codigo}</td>
                <td>${notice.cedula_usuario}</td>
                <td>${notice.tipo_dano}</td>
                <td>${notice.descripcion}</td>
                <td>${notice.ubicacion}</td>
                <td>${notice.fecha}</td>
                <td>${notice.estado}</td>
                <td>
                    <button class="action-btn edit-btn"
                        onclick="editNotice('${notice.codigo}', '${notice.cedula_usuario}', '${notice.tipo_dano}', '${notice.descripcion}', '${notice.ubicacion}', '${notice.fecha}', '${notice.estado}')">
                        Editar
                    </button>
                    <button class="action-btn delete-btn"
                        onclick="deleteNotice('${notice.codigo}')">
                        Eliminar
                    </button>
                </td>
            </tr>
        `;

    } catch (error) {
        console.error(error);
        tableBody.innerHTML = "";
        showMessage("Aviso no encontrado", "error");
    }
}

async function deleteNotice(codigo) {
    var confirmacion = confirm("¿Desea eliminar este aviso?");

    if (!confirmacion) {
        return;
    }

    try {
        var res = await fetch(API_URL + "/notices/delete/" + codigo, {
            method: "DELETE"
        });

        if (res.ok) {
            showMessage("Aviso eliminado correctamente");
            clearNoticeForm();
            loadNotices();
        } else {
            var errorMessage = await getErrorMessage(res);
            showMessage(errorMessage, "error");
        }

    } catch (error) {
        console.error(error);
        showMessage("Error de conexión con la API", "error");
    }
}