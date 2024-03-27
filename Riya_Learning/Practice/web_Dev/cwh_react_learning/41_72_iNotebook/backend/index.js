console.log("moongose working")

const db = require("./db");
const express = require('express')
const app = express()
const port = 3000

app.use(express.json())

//Available Routes
app.use('/api/auth', require('./routes/auth'))
app.use('/api/notes', require('./routes/notes'))

app.get('/', (req, res) =>
    res.send('Hello Riya!')
)


app.listen(port, () => {
    console.log(`Example app listening on https://localhost: ${port}`)
})

