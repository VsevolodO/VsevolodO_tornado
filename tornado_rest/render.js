
const axios = require('axios')
const port = document.getElementById("port");
const user = document.getElementById("user");
axios.defaults.adapter = require('axios/lib/adapters/http');



axios({
    method: "get",
    url: "http://localhost:7000",
    responseType: 'xhr'
})
    .then((response) => {
        data = response.data
        user.innerHTML = data.user;
        port.innerHTML = data.port;
    });




