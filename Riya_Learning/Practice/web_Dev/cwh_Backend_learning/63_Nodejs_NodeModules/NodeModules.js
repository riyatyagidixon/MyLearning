const fs = require("fs");
// const text = fs.readFileSync("./display.txt", "utf-8");

let text = fs.readFileSync("./display.txt", "utf-8");
text = text.replace("Javascript", " node js");

console.log("The content of file is ");
console.log(text);

console.log("creating a new file...");
fs.writeFileSync("./file.txt", text);