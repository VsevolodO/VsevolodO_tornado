const WebSocket = require('ws');
const ws = new WebSocket("ws://localhost:9000/");
const port = document.getElementById("port");
const user = document.getElementById("user");

ws.onopen = function(){
    ws.send('hello');
    
};

ws.onmessage = function(data){
    data = JSON.parse(data.data);
    user.innerHTML = data.user;
    port.innerHTML = data.port;
};



