//var restFactory = require('./restfactory.js');
var user = restFactory.factory("http://127.0.0.1:8000/api", "users");
user.list(onListSuccess, onListFailure);
function onListSuccess(status, response){
    console.log(status);
    console.log('List success');
    console.log(response);
}
function onListFailure(status, response){
    console.log(status);
    console.log('List failure');
}

user.retrieve(1, onRetrieveSuccess, onRetrieveFailure);
function onRetrieveSuccess(status, response){
    console.log(status);
    console.log('Retrieve success');
    console.log(response);
}
function onRetrieveFailure(status, response){
    console.log(status);
    console.log('Retrieve failure');
}
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

var headers = {
    'X-CSRFToken': csrftoken
};
var params = {
    email: 'newtest@test.com',
    username: 'newtest',
    groups: ""
};
user.create(params, headers, onCreateSuccess, onCreateFailure);
function onCreateSuccess(status, response){
    console.log(status);
    console.log('Create success');
    console.log(response);
}
function onCreateFailure(status, response){
    console.log(status);
    console.log('Create failure');
}
user.destroy(3, headers, onDestroySuccess, onDestroyFailure);
function onDestroySuccess(status, response){
    console.log(status);
    console.log('Destroy success');
    console.log(response);
}
function onDestroyFailure(status, response){
    console.log(status);
    console.log('Destroy failure');
}
var params = {
    username: 'GG',
};
user.update(1, params, headers, true, onUpdateSuccess, onUpdateFailure);
function onUpdateSuccess(status, response){
    console.log(status);
    console.log('Update success');
    console.log(response);
}
function onUpdateFailure(status, response){
    console.log(status);
    console.log('Update failure');
}
console.log('done');
