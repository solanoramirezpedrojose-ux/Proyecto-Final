var userForm = document.getElementById("userForm");
var cedulaEditando = null;

if (userForm) {
    userForm.addEventListener("submit", async function (e) {
        e.preventDefault();

        var cedula = document.getElementById("cedula").value;
        var nombre = document.getElementById("nombre").value;
        var correo = document.getElementById("correo").value;
        var contrasena = document.getElementById("contrasena").value;
        var rol = document.getElementById("rol").value;

        var userData = {
            cedula: cedula,
            nombre: nombre,
            correo: correo,
            contrasena: contrasena,
            rol: rol
        };

        var url = API_URL + "/users/add";
        var method = "POST";

        if (cedulaEditando !== null) {
            url = API_URL + "/users/update/" + cedulaEditando;
            method = "PUT";
        }

        try {
            var res = await fetch(url, {
                method: method,
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(userData)
            });

            if (res.ok) {
                showMessage("Usuario guardado correctamente");
                clearUserForm();
                loadUsers();
            } else {
                var errorMessage = await getErrorMessage(res);
                showMessage(errorMessage, "error");
            }

        } catch (error) {
            console.error(error);
            showMessage("Error de conexión con la API", "error");
        }
    });

    loadUsers();
}

async function loadUsers() {
    var tableBody = document.getElementById("usersTable");

    if (!tableBody) {
        return;
    }

    try {
        var res = await fetch(API_URL + "/users/list");

        if (!res.ok) {
            throw new Error("Error al cargar usuarios");
        }

        var data = await res.json();

        tableBody.innerHTML = "";

        data.forEach(function (user) {
            var row = `
                <tr>
                    <td>${user.cedula}</td>
                    <td>${user.nombre}</td>
                    <td>${user.correo}</td>
                    <td>${user.rol}</td>
                    <td>
                        <button class="action-btn edit-btn"
                            onclick="editUser('${user.cedula}', '${user.nombre}', '${user.correo}', '${user.rol}')">
                            Editar
                        </button>
                        <button class="action-btn delete-btn"
                            onclick="deleteUser('${user.cedula}')">
                            Eliminar
                        </button>
                    </td>
                </tr>
            `;

            tableBody.innerHTML += row;
        });

    } catch (error) {
        console.error(error);
        showMessage("No se pudieron cargar los usuarios", "error");
    }
}

function editUser(cedula, nombre, correo, rol) {
    cedulaEditando = cedula;

    document.getElementById("cedula").value = cedula;
    document.getElementById("nombre").value = nombre;
    document.getElementById("correo").value = correo;
    document.getElementById("contrasena").value = "";
    document.getElementById("rol").value = rol;

    document.getElementById("cedula").disabled = true;

    showMessage("Modo edición activado");
}

function clearUserForm() {
    cedulaEditando = null;

    document.getElementById("userForm").reset();
    document.getElementById("cedula").disabled = false;
}

async function searchUser() {
    var cedula = document.getElementById("searchCedula").value.trim();
    var tableBody = document.getElementById("usersTable");

    if (!cedula) {
        showMessage("Digite una cédula", "error");
        return;
    }

    try {
        var res = await fetch(API_URL + "/users/search/" + cedula);

        if (!res.ok) {
            throw new Error("Usuario no encontrado");
        }

        var user = await res.json();

        tableBody.innerHTML = `
            <tr>
                <td>${user.cedula}</td>
                <td>${user.nombre}</td>
                <td>${user.correo}</td>
                <td>${user.rol}</td>
                <td>
                    <button class="action-btn edit-btn"
                        onclick="editUser('${user.cedula}', '${user.nombre}', '${user.correo}', '${user.rol}')">
                        Editar
                    </button>
                    <button class="action-btn delete-btn"
                        onclick="deleteUser('${user.cedula}')">
                        Eliminar
                    </button>
                </td>
            </tr>
        `;

    } catch (error) {
        console.error(error);
        tableBody.innerHTML = "";
        showMessage("Usuario no encontrado", "error");
    }
}

async function deleteUser(cedula) {
    var confirmacion = confirm("¿Desea eliminar este usuario?");

    if (!confirmacion) {
        return;
    }

    try {
        var res = await fetch(API_URL + "/users/delete/" + cedula, {
            method: "DELETE"
        });

        if (res.ok) {
            showMessage("Usuario eliminado correctamente");
            clearUserForm();
            loadUsers();
        } else {
            var errorMessage = await getErrorMessage(res);
            showMessage(errorMessage, "error");
        }

    } catch (error) {
        console.error(error);
        showMessage("Error de conexión con la API", "error");
    }
}