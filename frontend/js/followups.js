var followUpForm = document.getElementById("followUpForm");
var seguimientoEditando = null;

if (followUpForm) {
    followUpForm.addEventListener("submit", async function (e) {
        e.preventDefault();

        var codigo_seguimiento = document.getElementById("codigoSeguimiento").value;
        var codigo_aviso = document.getElementById("codigoAvisoSeguimiento").value;
        var estado = document.getElementById("estadoSeguimiento").value;
        var observacion = document.getElementById("observacion").value;
        var fecha_actualizacion = document.getElementById("fechaActualizacion").value;
        var responsable = document.getElementById("responsable").value;

        var followUpData = {
            codigo_seguimiento: codigo_seguimiento,
            codigo_aviso: codigo_aviso,
            estado: estado,
            observacion: observacion,
            fecha_actualizacion: fecha_actualizacion,
            responsable: responsable
        };

        var url = API_URL + "/follow-ups/add";
        var method = "POST";

        if (seguimientoEditando !== null) {
            url = API_URL + "/follow-ups/update/" + seguimientoEditando;
            method = "PUT";
        }

        try {
            var res = await fetch(url, {
                method: method,
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(followUpData)
            });

            if (res.ok) {
                showMessage("Seguimiento guardado correctamente");
                clearFollowUpForm();
                loadFollowUps();
            } else {
                var errorMessage = await getErrorMessage(res);
                showMessage(errorMessage, "error");
            }

        } catch (error) {
            console.error(error);
            showMessage("Error de conexión con la API", "error");
        }
    });

    loadNoticeOptions();
    loadFollowUps();
}

async function loadNoticeOptions() {
    var select = document.getElementById("codigoAvisoSeguimiento");

    if (!select) {
        return;
    }

    try {
        var res = await fetch(API_URL + "/notices/list");
        var data = await res.json();

        select.innerHTML = `<option value="">Seleccione un aviso</option>`;

        data.forEach(function (notice) {
            select.innerHTML += `
                <option value="${notice.codigo}">
                    ${notice.codigo} - ${notice.tipo_dano}
                </option>
            `;
        });

    } catch (error) {
        console.error(error);
    }
}

async function loadFollowUps() {
    var tableBody = document.getElementById("followUpsTable");

    if (!tableBody) {
        return;
    }

    try {
        var res = await fetch(API_URL + "/follow-ups/list");

        if (!res.ok) {
            throw new Error("Error al cargar seguimientos");
        }

        var data = await res.json();

        tableBody.innerHTML = "";

        data.forEach(function (follow) {
            var row = `
                <tr>
                    <td>${follow.codigo_seguimiento}</td>
                    <td>${follow.codigo_aviso}</td>
                    <td>${follow.estado}</td>
                    <td>${follow.observacion}</td>
                    <td>${follow.fecha_actualizacion}</td>
                    <td>${follow.responsable}</td>
                    <td>
                        <button class="action-btn edit-btn"
                            onclick="editFollowUp('${follow.codigo_seguimiento}', '${follow.codigo_aviso}', '${follow.estado}', '${follow.observacion}', '${follow.fecha_actualizacion}', '${follow.responsable}')">
                            Editar
                        </button>

                        <button class="action-btn delete-btn"
                            onclick="deleteFollowUp('${follow.codigo_seguimiento}')">
                            Eliminar
                        </button>
                    </td>
                </tr>
            `;

            tableBody.innerHTML += row;
        });

    } catch (error) {
        console.error(error);
        showMessage("No se pudieron cargar los seguimientos", "error");
    }
}

function editFollowUp(codigo_seguimiento, codigo_aviso, estado, observacion, fecha_actualizacion, responsable) {
    seguimientoEditando = codigo_seguimiento;

    document.getElementById("codigoSeguimiento").value = codigo_seguimiento;
    document.getElementById("codigoAvisoSeguimiento").value = codigo_aviso;
    document.getElementById("estadoSeguimiento").value = estado;
    document.getElementById("observacion").value = observacion;
    document.getElementById("fechaActualizacion").value = fecha_actualizacion;
    document.getElementById("responsable").value = responsable;

    document.getElementById("codigoSeguimiento").disabled = true;

    showMessage("Modo edición activado");
}

function clearFollowUpForm() {
    seguimientoEditando = null;

    document.getElementById("followUpForm").reset();
    document.getElementById("codigoSeguimiento").disabled = false;
}

async function searchFollowUp() {
    var codigo = document.getElementById("searchCodigoSeguimiento").value.trim();
    var tableBody = document.getElementById("followUpsTable");

    if (!codigo) {
        showMessage("Digite el código del seguimiento", "error");
        return;
    }

    try {
        var res = await fetch(API_URL + "/follow-ups/search/" + codigo);

        if (!res.ok) {
            throw new Error("Seguimiento no encontrado");
        }

        var follow = await res.json();

        tableBody.innerHTML = `
            <tr>
                <td>${follow.codigo_seguimiento}</td>
                <td>${follow.codigo_aviso}</td>
                <td>${follow.estado}</td>
                <td>${follow.observacion}</td>
                <td>${follow.fecha_actualizacion}</td>
                <td>${follow.responsable}</td>
                <td>
                    <button class="action-btn edit-btn"
                        onclick="editFollowUp('${follow.codigo_seguimiento}', '${follow.codigo_aviso}', '${follow.estado}', '${follow.observacion}', '${follow.fecha_actualizacion}', '${follow.responsable}')">
                        Editar
                    </button>

                    <button class="action-btn delete-btn"
                        onclick="deleteFollowUp('${follow.codigo_seguimiento}')">
                        Eliminar
                    </button>
                </td>
            </tr>
        `;

    } catch (error) {
        console.error(error);
        tableBody.innerHTML = "";
        showMessage("Seguimiento no encontrado", "error");
    }
}

async function deleteFollowUp(codigo) {
    var confirmacion = confirm("¿Desea eliminar este seguimiento?");

    if (!confirmacion) {
        return;
    }

    try {
        var res = await fetch(API_URL + "/follow-ups/delete/" + codigo, {
            method: "DELETE"
        });

        if (res.ok) {
            showMessage("Seguimiento eliminado correctamente");
            clearFollowUpForm();
            loadFollowUps();
        } else {
            var errorMessage = await getErrorMessage(res);
            showMessage(errorMessage, "error");
        }

    } catch (error) {
        console.error(error);
        showMessage("Error de conexión con la API", "error");
    }
}