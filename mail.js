
const firebaseConfig = {
    apiKey: "AIzaSyCMqLttSQT9iR9WEAnEGD-6EWCfwtHfBQI",
    authDomain: "my-first-projectsrv.firebaseapp.com",
    databaseURL: "https://my-first-projectsrv-default-rtdb.firebaseio.com",
    projectId: "my-first-projectsrv",
    storageBucket: "my-first-projectsrv.appspot.com",
    messagingSenderId: "725600835240",
    appId: "1:725600835240:web:1e93f7076e0fe257a7549d"
};

// initialize firebase
firebase.initializeApp(firebaseConfig);

// reference your database
var contactFormDB = firebase.database().ref("contactForm");

document.getElementById("contactForm").addEventListener("submit", submitForm);
document.getElementById("confirmPassword").addEventListener("input", validatePasswords);

function submitForm(e) {
    e.preventDefault();

    var name = getElementVal("name");
    var emailid = getElementVal("emailid");
    var phone = getElementVal("phone");
    var password = getElementVal("password");
    var confirmPassword = getElementVal("confirmPassword");
    var msgContent = getElementVal("msgContent");

    // Validation for password and confirm password
    if(password !== confirmPassword) {
        alert("Passwords do not match. Please try again.");
        return;
    }

    saveMessages(name, emailid, phone, password, msgContent);

    //   enable alert
    document.querySelector(".alert").style.display = "block";

    //   remove the alert
    setTimeout(() => {
        document.querySelector(".alert").style.display = "none";
    }, 3000);

    //   reset the form
    document.getElementById("contactForm").reset();
    document.querySelector(".tick").style.display = "none"; // hide tick after form reset
}

const saveMessages = (name, emailid, phone, password, msgContent) => {
    var newContactForm = contactFormDB.push();

    newContactForm.set({
        name: name,
        emailid: emailid,
        phone: phone,
        password: password,
        msgContent: msgContent,
    });
};

const getElementVal = (id) => {
    return document.getElementById(id).value;
};

function validatePasswords() {
    var password = document.getElementById("password").value;
    var confirmPassword = document.getElementById("confirmPassword").value;
    var tick = document.querySelector(".tick");

    if (password === confirmPassword && confirmPassword !== "") {
        tick.style.display = "block";
    } else {
        tick.style.display = "none";
    }
}