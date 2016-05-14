var app = require('express')()
var n = 0
app.get('/', function(req, res){
	n = n + 1
	console.log(n)
	res.send("yee")
})

app.listen(3000, function(){
	console.log("ello")
})