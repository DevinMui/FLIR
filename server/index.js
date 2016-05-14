var app = require('express')()
var n = 0
var value = false
var rotate = ""
app.get('/', function(req, res){
	n = n + 1
	console.log(n)
	res.send("yee")
})
app.get('/intrude', function(req, res){
	value = true
	res.send("done")
})
app.get('/no_intrude', function(req, res){
	value = false
	res.send("done")
})
app.get('/rotate_right', function(req, res){
	rotate = "right"
	res.send('rotate')
})
app.get('/rotate_left', function(req, res){
	rotate = "left"
	res.send('rotate')
})
app.get('/rotate_none', function(req, res){
	rotate = ""
	res.send('rotate')
})
app.get('/value', function(req, res){
	res.send([value, rotate])
})
app.listen(3000, function(){
	console.log("ello")
})