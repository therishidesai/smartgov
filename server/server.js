var express = require('express'),
    app = express(),
    bodyParser = require('body-parser'),
    redis = require('redis'),
    client = redis.createClient(6379, 'smartgov-redis');


client.on("connect", function(){
    console.log("connected")
})

app.use(bodyParser());
app.use(bodyParser.urlencoded({
    extended: true
}));
app.use(bodyParser.json());

var router = express.Router(); // get an instance of the express Router

router.get('/', function(req, res) {
    res.json({
        message: 'Welcome to Smartgov!'
    });
});


app.use('/server', router);

app.listen(3001, function() {
    console.log('I\'m Listening...');
});
