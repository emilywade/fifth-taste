
emailjs.init({
    publicKey: "orDbunfZEWG7sa4Ss",
});


function sendConfirmationEmail(form) {
    emailjs.send("service_n79jo81", "template_2exvx03", {
        "name" : form.name.value,
        "email" : form.email.value,
        "date" : form.date.value,
        "time" : form.time.value,
        "num_guests" : form.num_guests.value,
        "special_requests" : form.special_requests.value
    })
    .then(
        function(response) {
            console.log("SUCCESS", response);
        }, function(error) {
            console.log("FAILED", error);
        }
    )
}