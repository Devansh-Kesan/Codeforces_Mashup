// document.getElementById("login-form").addEventListener("submit",function (event) {
//     event.preventDefault();

//     const username = document.getElementById("username").value;
//     const password = document.getElementById("password").value;



//     // console.log(username);
//     fetch("http://127.0.0.1:5000/run-python-script", {
//         method: "POST",
//         headers: {
//             "Content-Type": "application/json"
//         },
//         body: JSON.stringify({ username, password })
//     })
//     .then(response => response.json())
//     .then(result => console.log(result.message))
//     .catch(error => console.error("Error:", error));
    
// })



// document.getElementById("automatebutton").addEventListener("click", function() {
//     // Call the API endpoint
//     console.log("Button clicked!");

//     fetch('http://127.0.0.1:5000/run-python-script')
//         .then(response => response.text())
//         .then(result => console.log(result))
//         .catch(error => console.error('Error:', error));
// });



// ###########

document.getElementById("login-form").addEventListener("submit", function (event) {
    event.preventDefault();
    console.log("Button Clicked")

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const name = document.getElementById("Name").value;
    const duration = document.getElementById("duration").value;

    const p1 = document.getElementById("p1").value;
    const p2 = document.getElementById("p2").value;
    const p3 = document.getElementById("p3").value;

    console.log(username);

    // Send data to Flask endpoint
    fetch("http://127.0.0.1:5000/run-python-script", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ username, password , name , duration, p1 , p2 , p3 })
    })
    .then(response => response.json())
    .then(result => console.log(result.message))
    .catch(error => console.error("Error:", error));
});