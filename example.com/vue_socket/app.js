var http = require("http");
var url = require('url');
var fs = require('fs');
var server = http.createServer(function(request, response){
 var path = url.parse(request.url).pathname;
 switch(path){
  case '/':
    response.writeHead(200, {'Content-Type': 'text/html'});
    response.write('<h1>Hey, have you heard about our <a href="/signup.html">signup page</a></h1>');
    response.end();
    break;
  case '/signup.html':
    fs.readFile(__dirname + path, function(error, data){
      if (error){
        response.writeHead(404);
        response.write("opps this doesn't exist - 404");
        response.end();
      }
      else{
        response.writeHead(200, {"Content-Type": "text/html"});
        response.write(data, "utf8");
        response.end();
      }
    });
    break;
  default:
    response.writeHead(404);
    response.write("opps this doesn't exist - 404");
    response.end();
    break;
 }
});
server.listen(7001);

var io = require('socket.io').listen(server);

//io.set('log level', 1);

io.sockets.on('connection',function(socket){
  setInterval(function(){
    socket.emit('stream',{'title':"A new tile via Socket.IO!"});
  }, 1000);
})
