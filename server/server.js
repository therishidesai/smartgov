var express = require('express'),
    app = express(),
    bodyParser = require('body-parser'),
    redis = require('redis'),
    client = redis.createClient(6379, 'smartgov-redis'),
    request = require('request');


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

router.get('/getLatestBills', function(req, res){ 
    request('https://congress.api.sunlightfoundation.com/bills?fields=bill_id,introduced_on,official_title,short_title,nicknames,popular_title,nicknames,summary,urls,history,sponsor,keywords&per_page=50&history.active=true', function(err, result, body){
	if(err){
	    console.log(err);
	    res.send(err);
	}else{
	    console.log(body);
	    res.send(body);
	}
    }); 
});


app.use('/server', router);

app.listen(3001, function() {
    console.log('I\'m Listening...');
});
