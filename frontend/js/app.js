var API_URL = "http://127.0.0.1:8000/api";

var messageBox = document.getElementById("messageBox");

function showMessage(text, type = "success") {
    messageBox = document.getElementById("messageBox");

    if (!messageBox) {
        return;
    }

    messageBox.textContent = text;
    messageBox.classList.remove("hidden");

    if (type === "success") {
        messageBox.style.backgroundColor = "#22c55e";
    } else {
        messageBox.style.backgroundColor = "#dc2626";
    }

    messageBox.style.color = "white";

    setTimeout(function () {
        messageBox.classList.add("hidden");
    }, 3000);
}

async function getErrorMessage(res) {
    try {
        var data = await res.json();

        if (data.detail) {
            return data.detail;
        }

        return "Ocurrió un error";
    } catch (error) {
        return "Ocurrió un error";
    }
}

function logout() {
    localStorage.removeItem("token");
    localStorage.removeItem("usuario");
}

var loginForm = document.getElementById("loginForm");

if (loginForm) {
    loginForm.addEventListener("submit", async function (e) {
        e.preventDefault();

        var correo = document.getElementById("loginCorreo").value;
        var contrasena = document.getElementById("loginContrasena").value;

        var loginData = {
            correo: correo,
            contrasena: contrasena
        };

        try {
            var res = await fetch(API_URL + "/auth/login", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(loginData)
            });

            if (res.ok) {
                var data = await res.json();

                localStorage.setItem("token", data.token);
                localStorage.setItem("usuario", JSON.stringify(data.user));

                showMessage("Inicio de sesión correcto");

                setTimeout(function () {
                    window.location.href = "pages/users.html";
                }, 700);
            } else {
                var errorMessage = await getErrorMessage(res);
                showMessage(errorMessage, "error");
            }

        } catch (error) {
            console.error(error);
            showMessage("Error de conexión con la API", "error");
        }
    });
}