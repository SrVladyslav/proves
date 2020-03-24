const zmq = require('zeromq')
const so = zmq.socket('req')

//connecting to the server
so.bind("tcp://127.0.0.1:5000");
so.on('message', function(intro, count){
	if(count.toString() == 'info'){
		so.send(['INFORMATION OF SERVER'])
	}else{
		so.send(['Hello', count])
	}
});