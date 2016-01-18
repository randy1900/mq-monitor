var app = angular.module("mq", []);
app.controller("queue", function($scope, $http) {

	$scope.subQueue = function(index) {
		queue = $('#queue-' + index).text()
		mailList = []
		mails = $('#mailList-' + index).val().trim().split(',')
		for(i = 0; i < mails.length; ++i) {
			mailList[i] = mails[i].trim()
		}
		msgTotalMax = $('#msgTotalMax-' + index).val().trim()
		$http.post('/mq/sub', {addr: $('select').find("option:selected").text(), queue: queue, mailList: mailList, msgTotalMax}).
			then(function(res) {
				$('#button-' + index).text('已订阅')
			}, function(res) {
				
			})
	};
});