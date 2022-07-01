const express = require("express");
const app = express();
const http = require("http");
const { dirname } = require("path");
const server = http.createServer(app);

app.use("/static", express.static("./static/"));
app.get("/", (req,res) => {
    res.sendFile(__dirname + "/index.html");
});
server.listen(8888, () => {
    console.log("Server listening on 8888");
});