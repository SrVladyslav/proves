const net = require('net')
let server = net.createServer(
	function(c){
		console.log('Server connected!')
		c.write('Hi there!!! your server was connected perfectly')
		c.on('end', function(){
			console.log('Server disconnected')
		})

		c.on('error', function(){
			console.log('Fatala ERROR!')
		})

		c.on('data', function(data){
			console.log('The server has received new data!')
			if(data.toString() == "info"){
				c.write('Rely on the server pit, but be straight!!')
			}
		})
	}
)//END of net.createServer()
server.listen(5000, function(){
	console.log('server bounded')
})