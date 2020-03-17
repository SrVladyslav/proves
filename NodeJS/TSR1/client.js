const zmq = require('zeromq')
let req = zmq.socket('req');
req.connect('tcp://localhost:97990')
req.on('message', (msg)=> {
	console.log('resp: '+msg)
	process.exit(0);
})
req.send('Hola')
//req.send(['a','b','c'])