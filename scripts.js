function submitForm() {
    // Get form values
    const name = document.getElementById('name').value;
    const address = document.getElementById('address').value;
    const postcode = document.getElementById('postcode').value;
    const phone = document.getElementById('phone').value;
    const email = document.getElementById('email').value;
    const loanAmount = document.getElementById('loanAmount').value;
    const loanPurpose = document.getElementById('loanPurpose').value;
    const loanDuration = document.getElementById('loanDuration').value;

    // Check if all fields are filled
    if (!name || !address || !postcode || !phone || !email || !loanAmount || !loanPurpose || !loanDuration) {
        alert("Please fill out all fields.");
        return;
    }

    // Construct URL with query parameters
    const url = `confirmation.html?name=${encodeURIComponent(name)}&address=${encodeURIComponent(address)}&postcode=${encodeURIComponent(postcode)}&phone=${encodeURIComponent(phone)}&email=${encodeURIComponent(email)}&loanAmount=${encodeURIComponent(loanAmount)}&loanPurpose=${encodeURIComponent(loanPurpose)}&loanDuration=${encodeURIComponent(loanDuration)}`;

    // Redirect to confirmation page
    window.location.href = url;
}

function clearForm() {
    document.getElementById('loanApplicationForm').reset();
}
