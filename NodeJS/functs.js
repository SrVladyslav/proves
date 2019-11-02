/*function saluda() {
 for (let i=0; i<arguments.length; i++) {
 	console.log("Hola, " + arguments[i])
 }
}
saluda("Ana", "Juan", "Isabel")*/


//una funcion recuerda el entorno en que se ha creado
/*function creaFunc(){
	let nombre = "Chrome"
	return ()=>{
		console.log(nombre)
	}
}
let miFunc = creaFunc()
miFunc()*/
/*function writing(x) {
 console.log("---\nWriting after " + x + " seconds")
}
function writingClosure(x) {
 //return function() {
 console.log("---\nWriting after " + x + " seconds")
 //}
}
setTimeout(function() {writing(6) }, 6000)
setTimeout(writing, 3000)
setTimeout(writingClosure(4) , 4000)
console.log("root(2) =", Math.sqrt(2)) */

const fs = require('fs')
fs.writeFileSync('data1.txt', 'Hello Node.js')
fs.writeFileSync('data2.txt', 'Hello guys!!')
fs.writeFileSync('data3.txt', 'Hello!!sdfghjksdfghjksdfghjksdfghjkfghj')
/*
function callback(err, data) {
	if(err) console.error('---\n' + err.stack)
	else console.log('---\nFile content is: \n' + data.toString())		
}

setTimeout(function(){
	fs.readFile('data3.txt', callback)
}, 3000)

setTimeout(function(){
	fs.readFile('data1.txt', callback)
}, 3000)

fs.readFile('data2.txt', callback)
fs.readFile('data3.txt', callback)
console.log('rooot(2)', Math.sqrt(2))*/

fs.readdir('.', function(err, files){
	let count = files.length
	let results = {}
	files.forEach(function(filename){
		fs.readFile(filename, function(err, data){
			console.log(filename,"has been read")
			results[filename] = data
			count --
			if(count <= 0){
				console.log('\nTOTAL:', files.length,'files have been read')
			}
		})
	})	
})
