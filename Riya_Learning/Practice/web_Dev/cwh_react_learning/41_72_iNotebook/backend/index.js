console.log("moongose working")

const db = require("./db");
var cors = require('cors')
const express = require('express')
const app = express()
const port = 5000

app.use(cors())
app.use(express.json())

//Available Routes
app.use('/api/auth', require('./routes/auth'))
app.use('/api/notes', require('./routes/notes'))


app.listen(port, () => {
    console.log(`iNotebook backend listening on https://localhost: ${port}`)
})

