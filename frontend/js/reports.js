if (document.getElementById("totalNotices")) {
    loadReportNoticeOptions();
    loadGeneralStatistics();
    loadNoticesByType();
}

async function loadGeneralStatistics() {
    try {
        var res = await fetch(API_URL + "/reports/general-statistics");

        if (!res.ok) {
            throw new Error("Error al cargar estadísticas");
        }

        var data = await res.json();

        document.getElementById("totalNotices").textContent = data.total;
        document.getElementById("pendingNotices").textContent = data.pendientes;
        document.getElementById("inProgressNotices").textContent = data.en_proceso;
        document.getElementById("resolvedNotices").textContent = data.resueltos;

        showMessage("Estadísticas cargadas correctamente");

    } catch (error) {
        console.error(error);
        showMessage("No se pudieron cargar las estadísticas", "error");
    }
}

async function loadNoticesByType() {
    var tableBody = document.getElementById("typesReportTable");

    if (!tableBody) {
        return;
    }

    try {
        var res = await fetch(API_URL + "/reports/notices-by-type");

        if (!res.ok) {
            throw new Error("Error al cargar reporte por tipo");
        }

        var data = await res.json();

        tableBody.innerHTML = "";

        for (var tipo in data) {
            var row = `
                <tr>
                    <td>${tipo}</td>
                    <td>${data[tipo]}</td>
                </tr>
            `;

            tableBody.innerHTML += row;
        }

    } catch (error) {
        console.error(error);
        showMessage("No se pudo cargar el reporte por tipo", "error");
    }
}

async function loadReportNoticeOptions() {
    var select = document.getElementById("codigoAvisoReporte");

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

async function loadFollowUpsReport() {
    var codigoAviso = document.getElementById("codigoAvisoReporte").value;
    var tableBody = document.getElementById("followUpsReportTable");

    if (!codigoAviso) {
        showMessage("Seleccione un aviso", "error");
        return;
    }

    try {
        var res = await fetch(API_URL + "/reports/follow-ups-by-notice/" + codigoAviso);

        if (!res.ok) {
            throw new Error("Error al cargar reporte de seguimientos");
        }

        var data = await res.json();
        var seguimientos = data.seguimientos;

        tableBody.innerHTML = "";

        if (seguimientos.length === 0) {
            tableBody.innerHTML = `
                <tr>
                    <td colspan="6">Este aviso no tiene seguimientos registrados</td>
                </tr>
            `;

            showMessage("El aviso seleccionado no tiene seguimientos", "error");
            return;
        }

        seguimientos.forEach(function (follow) {
            var row = `
                <tr>
                    <td>${follow.codigo_seguimiento}</td>
                    <td>${follow.codigo_aviso}</td>
                    <td>${follow.estado}</td>
                    <td>${follow.observacion}</td>
                    <td>${follow.fecha_actualizacion}</td>
                    <td>${follow.responsable}</td>
                </tr>
            `;

            tableBody.innerHTML += row;
        });

        showMessage("Reporte cargado correctamente");

    } catch (error) {
        console.error(error);
        showMessage("No se pudo cargar el reporte de seguimientos", "error");
    }
}