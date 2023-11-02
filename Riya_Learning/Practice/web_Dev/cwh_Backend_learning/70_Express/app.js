const express = require("express");
const path = require("path");
const app = express();
const fs = require("fs");
const port = 3000;

// EXPRESS SPECIFIC STUFF
app.use('/static', express.static('static'))  // For Serving static files
app.use(express.urlencoded())

// PUG SPECIFIC STUFF
app.set('view engine', 'pug');  // Set the template engine for pug
app.set('views', path.join(__dirname, 'views'));  // Set the views directory

// ENDPOINTS
app.get('/', (req, res) => {
    const con = 'This is the best tutorial of pug';
    const params = { 'title': 'PubG is the best game', content: con };
    res.status(200).render('index.pug', params);
})

app.post('/', (req, res) => {
    let name = req.body.name
    let age = req.body.age
    let gender = req.body.gender
    let address = req.body.address
    let more = req.body.more

    let outputToWrite = `The name of the client is ${name}, ${age} years old, ${gender}, residing at ${address}, more about him/her ${more}`
    fs.writeFileSync('output.txt', outputToWrite)
    const params = { 'message': 'Your form has been submitted successfully' }
    res.status(200).render('index.pug', params);
})


// START THE SERVER
app.listen(port, () => {
    console.log(`The appliication started successfully on port ${port}`);
})


// Our pug demo end point
// app.get('/', (req, res) => {
//     res.status(200).render('demo', { title: 'Hey Riya', message: 'Hello there! and Thanks to telling me how to use pug ! ' })
//   })

// app.get("/", (req, res)=> {
//     res.send("This is home page of my first express app with riya");
// });

// app.get("/about", (req, res)=> {
//     res.send("This is about page of my first express app with riya");
// });

// app.post("/", (req, res)=> {
//     res.send("This is home page of my first express app with riya");
// });

// app.get("/this", (req, res)=> {
//     res.status(404).send("Page not found!");
// });