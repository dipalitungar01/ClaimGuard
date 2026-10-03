// =========================
// PROJECT INFORMATION
// =========================

const projectName = "ClaimGuard";
const version = "1.0";

console.log(projectName);
console.log(version);


// =========================
// REGISTER
// =========================

const registerForm = document.getElementById("registerForm");

if (registerForm) {

    registerForm.addEventListener("submit", async function(event) {

        event.preventDefault();

        const name = document.getElementById("name").value;
        const email = document.getElementById("email").value;
        const password = document.getElementById("password").value;

        try {

            const response = await fetch(
                "http://127.0.0.1:8000/users/",
                {
                    method: "POST",

                    headers: {
                        "Content-Type": "application/json"
                    },

                    body: JSON.stringify({
                        name: name,
                        email: email,
                        password: password
                    })
                }
            );

            const data = await response.json();

            if (response.ok) {

                alert("Registration successful! You can now login.");

                window.location.href = "login.html";

            } else {

                alert(data.detail || "Registration failed.");

            }

        } catch (error) {

            console.log(error);

            alert("Cannot connect to ClaimGuard server.");

        }

    });

}


// =========================
// LOGIN
// =========================

const loginForm = document.getElementById("loginForm");

if (loginForm) {

    loginForm.addEventListener("submit", async function(event) {

        event.preventDefault();

        const email = document.getElementById("email").value;
        const password = document.getElementById("password").value;

        try {

            const response = await fetch(
                "http://127.0.0.1:8000/users/login",
                {
                    method: "POST",

                    headers: {
                        "Content-Type": "application/json"
                    },

                    body: JSON.stringify({
                        email: email,
                        password: password
                    })
                }
            );

            const data = await response.json();

            if (response.ok) {

                alert("Login successful!");

                console.log(data);

                window.location.href = "dashboard.html";

            } else {

                alert(data.detail || "Invalid email or password.");

            }

        } catch (error) {

            console.log(error);

            alert("Cannot connect to ClaimGuard server.");

        }

    });

}

// =========================
// SHOW / HIDE PASSWORD
// =========================

const togglePassword = document.getElementById("togglePassword");

if (togglePassword) {

    togglePassword.addEventListener("click", function () {

        const password = document.getElementById("password");
        const eyeIcon = document.getElementById("eyeIcon");

        if (password.type === "password") {

            // Show password
            password.type = "text";

            // Add slash to eye
            eyeIcon.innerHTML = `
                <path
                    d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"
                    fill="none"
                    stroke="currentColor"
                    stroke-width="2"
                />

                <circle
                    cx="12"
                    cy="12"
                    r="3"
                    fill="none"
                    stroke="currentColor"
                    stroke-width="2"
                />

                <line
                    x1="3"
                    y1="3"
                    x2="21"
                    y2="21"
                    stroke="currentColor"
                    stroke-width="2"
                />
            `;

        } else {

            // Hide password
            password.type = "password";

            // Remove slash
            eyeIcon.innerHTML = `
                <path
                    d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"
                    fill="none"
                    stroke="currentColor"
                    stroke-width="2"
                />

                <circle
                    cx="12"
                    cy="12"
                    r="3"
                    fill="none"
                    stroke="currentColor"
                    stroke-width="2"
                />
            `;

        }

    });

}

// =========================
// FORGOT PASSWORD
// =========================

const forgotPasswordForm =
    document.getElementById("forgotPasswordForm");

if (forgotPasswordForm) {

    forgotPasswordForm.addEventListener("submit", async function(event) {

        event.preventDefault();

        const email =
            document.getElementById("email").value;

        try {

            const response = await fetch(
                "http://127.0.0.1:8000/users/forgot-password",
                {
                    method: "POST",

                    headers: {
                        "Content-Type": "application/json"
                    },

                    body: JSON.stringify({
                        email: email
                    })
                }
            );

            const data = await response.json();

            if (response.ok) {

                alert(data.message);

            } else {

                alert(data.detail);

            }

        } catch (error) {

            console.log(error);

            alert("Cannot connect to ClaimGuard server.");

        }

    });

}

// =========================
// RESET PASSWORD
// =========================

const resetPasswordForm =
    document.getElementById("resetPasswordForm");

if (resetPasswordForm) {

    resetPasswordForm.addEventListener(
        "submit",
        async function(event) {

            event.preventDefault();

            const email =
                document.getElementById("email").value;

            const newPassword =
                document.getElementById("newPassword").value;

            const confirmPassword =
                document.getElementById("confirmPassword").value;


            // Check passwords

            if (newPassword !== confirmPassword) {

                alert("Passwords do not match.");

                return;
            }


            try {

                const response = await fetch(
                    "http://127.0.0.1:8000/users/reset-password",
                    {
                        method: "POST",

                        headers: {
                            "Content-Type": "application/json"
                        },

                        body: JSON.stringify({
                            email: email,
                            new_password: newPassword
                        })
                    }
                );


                const data = await response.json();


                if (response.ok) {

                    alert("Password reset successful!");

                    window.location.href = "login.html";

                } else {

                    alert(data.detail);

                }


            } catch (error) {

                console.log(error);

                alert(
                    "Cannot connect to ClaimGuard server."
                );

            }

        }
    );

}