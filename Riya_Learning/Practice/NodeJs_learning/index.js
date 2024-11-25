var http = require("http")

http.createServer(function (req, res) {

    res.write(200, { 'Content-Type': 'text/html' })
    res.end("Welcome back !!")

}).listen(8080)