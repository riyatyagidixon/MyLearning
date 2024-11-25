const fs = require('fs')

fs.readFile('index.js', 'utf-8', function (err, data) {
    console.log(data)
})

// Same as readFile there is a writefile function which is used to write the content in your file but there is a drawback it wipe out the entire data and then write the new content
// instead of writeFile we can use appendFile to add new content in existing one.
// To delete a file simply we just use "unlink" 