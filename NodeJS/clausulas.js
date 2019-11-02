// *** fibo1.js
// sincronas
/*function fibo(n) {
 return (n<2) ? 1 : setTimeout(function(x){fibo(n-2) + fibo(n-1)}(n),1)
 }
function fact(n) {
 return (n<2) ? 1 : setTimeout(function(x){n * fact(n-1)}(n), 1	)
}
console.log('Iniciando ejecución...')
console.log('fibo(40) =', fibo(40))
console.log('lanzado cálculo fibonacci...')
console.log('fact(10) =', fact(10))
console.log('lanzado cálculo factorial...')

//asincronas
//// *** fibo2.js
function fibo(n) { return (n<2) ? 1 : fibo(n-2) + fibo(n-1) }
function fibo_back1(n,cb) {
 let m = fibo(n)
 cb('fibonacci('+n+') = '+m)
}
function fact(n) { return (n<2) ? 1 : n * fact(n-1) }
function fact_back1(n,cb) {
 let m = fact(n)
 cb('factorial('+n+') = '+m)
 }
console.log('Iniciando ejecución...')
setTimeout( function(){
 fibo_back1(40, console.log)
}, 2000 )
console.log('lanzado cálculo fibonacci...')
setTimeout( function(){
 fact_back1(10, console.log)
}, 1000 )
console.log('lanzado cálculo factorial...')

function f(v,...s){
	for(let i in arguments){
		console.log(arguments[i])
	}
	console.log("--------------------------------")

	for(let i in s){
		console.log(s[i]()
	}
}

f("hola",()=>{console.log("funcion ejecutada")})*/

/*function writing(x){
	console.log("Writing after " + x + " seconds")
	return ()=>0
}
setTimeout(writing(6),6000)
setTimeout(writing,3000)
console.log("Program completed!")

x = writing(5)
console.log(x)

y = writing
console.log(y)

function creaFunc() {
 let nombre = "Mozilla"
 return () => {console.log(nombre)}
}
let miFunc = creaFunc
a = miFunc()
b = a 
b()

var hola
console.log(hola)
// server.js
const zmq = require('zeromq')
const rp = zmq.socket('rep')
let port = process.argv[2]
rp.bind('tcp://127.0.0.1:'+port)
rp.on('message', function(msg) {
let j = parseInt(msg)
rp.send([msg,(j*3).toString()])
})*/

s = "Hola que tal?"

/*console.log(s.slice(2))
var h = setInterval(()=>{
	console.log("hola")
}, 1000)*/
/*function mod(t){
	console.log("DEntro +" + t)
	return (m)=>{
		console.log("Escribiendo " + t +":"+  m)
	}
}
var i
for( i = 0; i < 5; i++){
	var t = "texto "+ i
	setTimeout(mod(t),1000)
	setTimeout(function(){
		mod(t)
	},1000)
}*/
/*const http = require('http')
const hostname = '127.0.0.1'
const port = 5000
const server = http.createServer((req, res) => {
 // res is a ServerResponse.
 // Its setHeader() method sets the response header.
 res.statusCode = 200
 res.setHeader('Content-Type', 'text/plain')
 // The end() method is needed to communicate that both the header
 // and body of the response have already been sent. As a result, the response can
 // be considered complete. Its optional argument may be used for including the
 res.write("holaaa")
 // last part of the body section.
 res.end('Hello World\n')
})
// listen() is used in an http.Server in order to start listening for
// new connections. It sets the port and (optionally) the IP address.
server.listen(port, hostname, () => {
 console.log('Server running at http://'+hostname+':'+port+'/')
})*/
/*
function writing(x) {
  return ()=> console.log("---\nWriting after " + x + " seconds")
}

var i
for( i = 0; i <5; i++){
	(setTimeout((h)=>{
		console.log(h)
	},1000))(i)
}
*/

//Uso de operaciones asíncronas, aquí modeladas con la función setTimeout.
//Note el valor de i asociado a las ejecuciones de las temporizaciones.
//Uso de la sentencia let.
function test(a,b,c){
	console.log(a+b+c)
}

test(1,"Hola")
test(()=>{return 1}(),2,3)