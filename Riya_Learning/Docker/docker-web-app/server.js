const express = require('express');
const app = express();
app.use(express.json());

const cources = [
    {id : 7,  name : 'physics'},
    {id : 5,  name : 'chemistry'},
    {id : 3,  name : 'math'}
];

app.get('/' , (req, res) => {
    console.log("response back to client");
    res.send('hello world');
})

app.get('/api/cources', (req,res) => {
    console.log("books sent to client");
    res.send( cources);
})


app.get('/api/cources/:id', (req,res) => {
    console.log("book with id sent to client");
    const cource = cources.find( c => c.id === parseInt(req.params.id) )
    if (!cource) res.status(404).send("not found")
    res.send(cource)
})

app.delete('/api/cources/:id', (req, res) => {
    console.log("Calling Delete RestAPI");
    //console.log("My request is = ", req);
    let index = cources.findIndex(c => c.id === parseInt(req.params.id))
    console.log("index = ", index);
    if(index == -1)
        res.status(404).send("Invalid ID "+req.params.id);
    //delete cources[index]; // it will leave hole in memory
    cources.splice(index);
    res.send(cources)
})

app.patch('/api/cources/:id', (req, res) => {
    console.log("Calling Patch RestAPI");
    //console.log("My request is = ", req);
    let index = cources.findIndex(c => c.id === parseInt(req.params.id))
    console.log("index = ", index);
    if(index == -1)
        res.status(404).send("Invalid ID "+req.params.id);
    console.log("Body is ", req.body);
    if(req.body) {
        cources[index].id = req.body.id;
        cources[index].name = req.body.name;
    }   
    res.send(cources)
})


app.get('/api/cources/:id/search/?', (req,res) => {
    console.log(req.params);
    console.log("path "+req.path);
    console.log('query ' + req.query);
    console.log('baseUrl ' + req.baseUrl);
    console.log('headers ' + req.headers);
    console.log('hostname ' + req.quehostnamery);
    console.log('httpVersion ' + req.httpVersion);
    console.log('httpVersionMajor ' + req.httpVersionMajor);
    console.log('httpVersionMinor ' + req.httpVersionMinor);
    console.log('ip ' + req.ip);
    console.log('ips ' + req.ips);
    console.log('originalUrlreq ' + req.originalUrlreq);

    for ( key in req.query)
    {
        console.log(key, req.query[key]);
    }
    res.send('abc');
})

app.post('/api/cources/', (req, res) => {
    console.log("indside post API");
    console.log(req.body);

    function rollinglist(item) {
        obj = new Object();
        if(item.id) {
            console.log("id available");
            obj.id = item.id;
        }
        if(item.name) {
            console.log("name available");
            obj.name = item.name;
        }
        console.log(obj);
        cources.push(obj);
    }

    if(Array.isArray(req.body)) {
        req.body.forEach(rollinglist);
    } else {
        rollinglist(req.body);
    }
    res.send(cources);
});


app.listen(3333, console.log('listening at port 3333 ...'));

