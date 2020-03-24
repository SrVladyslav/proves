const zmq = require('zeromq')
let req=[], workers=[]
let sc = zmq.socket('dealer') // backend broker 1
let st = zmq.socket('dealer') // backend broker 1 clients
let sw = zmq.socket('router') // frontend workers
let latido = zmq.socket('router') //comprueba que todos los workers estan vivos
let deathWorkers = [] 
let aliveWorkers = []
let contadorClientesLibres = 0
let TTL = 2000

var totalPeticionesAtendidas = 0
var cont = []

sc.connect('tcp://localhost:97991') //broker1
st.connect('tcp://localhost:97993') //broker1 time and clients
//latido.bind('tcp://*:97996')
sw.bind('tcp://*:97992') //workers
//resend method
function resend(w, c, m){
	return function(){
		deathWorkers[w] = true
		if(workers.length > 0){
			console.log("Reenviando la peticion")
			sw.send([w,'',c,'',request])
			aliveWorkers[w] = setTimeout(()=>{
				resend(w, c, m)
			}, TTL)
		}
	}
}

//recibir la informacion del broker 1 y distribuirla al primer worker libre
sc.on('message', (sep,c, sep2, request)=>{
	if(workers.length > 0 ){
		totalPeticionesAtendidas++
		console.log("Cliente:" + c +"Ha llegado vivo")
		var w = workers.shift()
		sw.send([w,'',c,'',request])
		aliveWorkers[w] = setTimeout(()=>{
			resend(w, c, request)
		}, TTL)
	}
})

st.on('message', (m)=>{//console.log(m)
})

//recibir respuesta del worker que ejecuto el trabajo y reenviarla al broker 1
sw.on('message', (w,sep,c,sep2,response)=>{
	console.log("w: "+w+"--sep: "+sep+"--c: "+c+"--sep2: "+sep2 + "--response: "+response)
	if(deathWorkers[w]) return
	totalPeticionesAtendidas++
	if(c==''){
		workers.push(w)
		console.log("NUEVO WORKER SE CONCETO WEY")
		return;
	}else{
		workers.push(w)
	} 
	sc.send([c,'',response])//manda al broker 1 la informacion procesada

	if(!cont[w]){
		cont[w] = 0
	}else{
		cont[w] ++
	}
})

st.on('message',(clientes) => {
	contadorClientesLibres = clientes
})

setInterval(()=>{
	st.send(workers.length) //mando la canitdad de workers que tengo
},10)


setInterval(()=>{
	console.log("Total peticiones atendidas: " + totalPeticionesAtendidas + " || Clientes: "+ contadorClientesLibres)
	cont.forEach((i)=>{
		console.log("Workers: "+ cont[i])
	})
},5000)