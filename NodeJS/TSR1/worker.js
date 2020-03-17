const zmq = require('zeromq')
let req = zmq.socket('req')
let latido = zmq.socket('req')
req.identity='Worker1'+process.pid
req.connect('tcp://localhost:97992')
req.connect('tcp//127.0.0.1:97996')
req.on('message', (c,sep,msg)=> {
	setTimeout(()=> {
		req.send([c,'','resp'])
	}, 1000)
})
req.send(['','',''])


//enviamos que estamos vivos wey
latido.on('message', (m)=>{
	latido.send(['Im here stupid.'])
})
