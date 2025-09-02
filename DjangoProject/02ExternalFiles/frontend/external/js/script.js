document.getElementById("regForm").addEventListener("submit", function (e) {
    e.preventDefault();

    let valid = true;

    let name = document.getElementById("name").value.trim();
    let email = document.getElementById("email").value.trim();
    let password = document.getElementById("password").value.trim();

    // Reset errors
    document.getElementById("nameError").innerText = "";
    document.getElementById("emailError").innerText = "";
    document.getElementById("passwordError").innerText = "";

    if (name === "") {
        document.getElementById("nameError").innerText = "Name is required";
        valid = false;
    }
    if (email === "" || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
        document.getElementById("emailError").innerText = "Valid email is required";
        valid = false;
    }
    if (password.length < 6) {
        document.getElementById("passwordError").innerText = "Password must be at least 6 characters";
        valid = false;
    }

    if (valid) {
        alert("Registration Successful!");
        document.getElementById("regForm").reset();
    }
});