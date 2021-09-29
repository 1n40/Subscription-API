// Function to send a post request to start a subscription
function buy() {
    let x = document.getElementById("op").value
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("POST", "http://127.0.0.1:5000/buy", false); // false for synchronous request
    xmlHttp.send(x);
    return xmlHttp.responseText;
}


// Function to get balance from the server
function bal() {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", "http://127.0.0.1:5000/balance", false); // false for synchronous request
    xmlHttp.send(null);
    return xmlHttp.responseText
}


// Function to cancel the subscription
function cancel() {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("POST", "http://127.0.0.1:5000/cancel", false); // false for synchronous request
    xmlHttp.send(null);
}

// Function to add money to the wallet
function add() {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("POST", "http://127.0.0.1:5000/add", false); // false for synchronous request
    xmlHttp.send(null);
}

// An interval function which executes our bal function to get balance 
var interval = setInterval(function () {
    document.getElementById("wallet").innerHTML = bal()
}, 2000)
