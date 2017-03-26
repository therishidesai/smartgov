app.controller('latestBillsViewController', ['$scope', '$http', function($scope, $http){ 
    
    var getLatestBills = function(){
	$http.get('http://localhost/server/getLatestBills').then(
	    function(res){
		console.log(res);
		$scope.latestBills = res.data.results;
	    },
	    function(err){
		console.log(err);
	    }
	);	
    }

    getLatestBills();
}]);
