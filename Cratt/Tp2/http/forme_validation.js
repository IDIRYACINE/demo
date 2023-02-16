function validateEmail() {
    let emailRegex = /^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$/;
    let emailElement = document.getElementsByName("email").item(0);
    let email = emailElement.value;
    let emailValid = emailRegex.test(email);

    let verificationResult = {
        element: emailElement,
        name:"email"
    }
    if (!emailValid) {
        document.getElementById("emailError").innerHTML = "Invalid email";
        verificationResult.valid = false
        return verificationResult;
    }
    else {
        document.getElementById("emailError").innerHTML = "";
        verificationResult.valid = true

        return verificationResult;
    }
}

function validateFirstName() {
    let nameRegex = /^[a-zA-Z]+$/;
    let nameElement = document.getElementsByName("nom").item(0);
    let name = nameElement.value;
    let nameValid = nameRegex.test(name);

    let verificationResult = {
        element: nameElement,
        name:"firstName"
    }

    if (!nameValid) {
        document.getElementById("nameError").innerHTML = "Name must contain only letters";
        verificationResult.valid = false;
        return verificationResult;
    } else {
        document.getElementById("nameError").innerHTML = "";
        verificationResult.valid = true;
        return verificationResult;
    }
}


function validateLastName() {
    let nameRegex = /^[a-zA-Z]+$/;
    let nameElement = document.getElementsByName("prenom").item(0);
    let name = nameElement.value;
    let nameValid = nameRegex.test(name);

    let verificationResult = {
        element : nameElement,
        name : "lastName"
    }

    if (!nameValid) {
        document.getElementById("nameError").innerHTML = "Name must contain only letters";
        verificationResult.valid = false;
        return verificationResult;
    } else {
        document.getElementById("nameError").innerHTML = "";
        verificationResult.valid = true;
        return verificationResult;
    }
}

function validateAge() {
    let ageRegex = /^([0-9]{1,2})$/;
    let ageElement = document.getElementsByName("age").item(0);
    let age = ageElement.value;
    let ageValid = ageRegex.test(age);

    let verificationResult = {
        element : ageElement,
        name : "age"
    }
    if (!ageValid) {
        document.getElementById("ageError").innerHTML = "Age must be between 0 and 99";
        verificationResult.valid = false;
        return verificationResult;
    } else {
        document.getElementById("ageError").innerHTML = "";
        verificationResult.valid = true;
        return verificationResult;
    }
}

function postFormDataToServer(event) {
    let validationCallbacks = [validateAge , validateEmail,validateFirstName,validateLastName]

    let submit = true;
    validationCallbacks.forEach(callback => {
        callbackResult = callback.apply();
        if(callbackResult.valid === false){
            submit = false;
            callbackResult.element.focus()
        }
    });

    console.log(submit)
    if(submit === false){
        alert("error occured on some fields")
        event.preventDefault();
    }
}