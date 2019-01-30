

let express = require("express");
let bodyParser = require("body-parser");
let app = express();

let Crypt = require('./lib/crypt');

// need it...  
app.use(bodyParser.urlencoded({ extended: false }));

app.post('/cmd5x', function (req, res) {
    let query_args = req.body.query_args;
    let salt = new Crypt().cmd5x(query_args);
    res.end(salt);
});


app.post('/get_time', function (req, res) {
    let salt = new Crypt().get_time();
    res.end(salt.toString());
});

app.post('/get_authKey', function (req, res) {
    let salt = new Crypt().get_authKey();
    res.end(salt);
});

app.post('/get_qc005', function (req, res) {
    let salt = new Crypt().get_qc005();
    res.end(salt);
});


app.listen(8888);