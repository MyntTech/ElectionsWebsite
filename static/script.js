function validateLogin() {
    // Basic validation
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    if (username === "" || password === "") {
        alert("Please enter both username and password.");
    } else {
        // Simulate a successful login (replace this with actual authentication logic)
        alert("Login successful! Redirecting to the dashboard...");
        // You might want to redirect the user to another page here.
    }
}

