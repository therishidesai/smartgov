app.controller('chatViewController', ['$scope', '$resource',function($scope, $resource){
    var Chat = $resource('/api/supportChat');
    var socket = io.connect('https://blueberryhome-support-chat.herokuapp.com/');
    
    $scope.selectedUser = null;
    
    $scope.getPhoneMessages = function(chat){
        $scope.selectedUser = chat.userPhoneNum;
        $scope.messages = chat.messages;
    };

    $scope.messages = [];
    var updateChats = function(){
        Chat.query(function(results){
            $scope.chats = results;    
        });
    };
    
    updateChats();

    socket.on('newChat', function(){
        $scope.chats = [];
        updateChats();                       
    });
    
    socket.on('updateChat', function(message){
        if($scope.selectedUser == message.phone){
            $scope.messages.push({from:message.from, body:message.body});    
        }
        updateChats();
    });
    $scope.chats = [];

    $scope.sendMessage = function(){
        Chat.save({phone:$scope.selectedUser, messageFrom:'Blueberry Support', messageBody:$scope.supportMessage},
            function(response){
                $scope.supportMessage='';
                console.log(response);
            });
    };
        
}]);
