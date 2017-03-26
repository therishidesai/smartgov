app.controller('latestBillsViewController', ['$scope', '$http', function($scope, $http){ 
    $scope.latestBills=[];
    var getLatestBills = function(){
	$http.get('http://localhost/server/getAnalyzedBills').then(
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
