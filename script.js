function validateForm(formId) {
    const form = document.forms[formId];
    const user = form["username"].value.trim();
    const pass = form["password"].value.trim();

    if (user === "" || pass === "") {
        alert("Please fill in both fields.");
        return false;
    }
    return true;
}
