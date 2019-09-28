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
function writing(x) {
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
console.log("root(2) =", Math.sqrt(2)) 