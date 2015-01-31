(function e(t,n,r){function s(o,u){if(!n[o]){if(!t[o]){var a=typeof require=="function"&&require;if(!u&&a)return a(o,!0);if(i)return i(o,!0);var f=new Error("Cannot find module '"+o+"'");throw f.code="MODULE_NOT_FOUND",f}var l=n[o]={exports:{}};t[o][0].call(l.exports,function(e){var n=t[o][1][e];return s(n?n:e)},l,l.exports,e,t,n,r)}return n[o].exports}var i=typeof require=="function"&&require;for(var o=0;o<r.length;o++)s(r[o]);return s})({1:[function(require,module,exports){
/*!
 * easyajax.js v0.0.1
 * https://github.com/chenkuochen/easyajax.js
 *
 * Copyright 2014 Chen-Kuo Chen
 * Released under the MIT license
 */


var easyAjax = (function(){
    var _config;
    function init(config){
        _config = config;
        easyAjax(_config.method, _config.url, _config.params, _config.success, _config.failure);
    }
    function easyAjax(method, url, params, success, failure){ //only deal with json
        var httpRequest;
        if (window.XMLHttpRequest){
            httpRequest = new XMLHttpRequest();
        } else if (window.ActiveXObject) {
            try {
                    httpRequest = new ActiveXObject("Msxml2.XMLHTTP");
            } catch (exception) {
                try {
                    httpRequest = new ActiveXObject("Microsoft.XMLHTTP");
                } catch (exception2) {}
            }
        }
        if (!httpRequest || (!(/^http:.*/.test(url)) && !(/^https:.*/.test(url)))) {
            console.log(url);
            return false;
        }
        httpRequest.onreadystatechange = function(){
            try {
                if (4 === httpRequest.readyState) {
                    if (200 === httpRequest.status && success) {
                        success(httpRequest.status, JSON.parse(httpRequest.responseText));
                    } else if (failure) {
                        failure(httpRequest.status, JSON.parse(httpRequest.responseText));
                    }
                }
            } catch (exception) {}
        };
        if ('POST' === method || 'PUT' === method || 'PATCH' === method) {
            httpRequest.open(method, url);
            setHeader(httpRequest);
            httpRequest.setRequestHeader('Content-Type', 'application/json');
            httpRequest.send(JSON.stringify(params));
        } else if ('GET' === method) {
            var getParams = "?";
            for (var key in params) {
                getParams += key + '=' + params[key] + '&';
            }
            httpRequest.open(method, url + getParams.substring(0, getParams.length - 1));
            setHeader(httpRequest);
            httpRequest.send();
        } else {
            httpRequest.open(method, url);
            setHeader(httpRequest);
            httpRequest.send();
        }
    }
    function setHeader(xhr){
        for (var key in _config.headers) {
            xhr.setRequestHeader(key, _config.headers[key]);
        }
    }
    return {
        ajax : init
    };
}());
module.exports = easyAjax;

},{}],2:[function(require,module,exports){
var restFactory = require('./restfactory.js');
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

},{"./restfactory.js":3}],3:[function(require,module,exports){
var easyAjax = require('./easyajax.js');
/*
 * URL layout:
 *   => Tailing trash is designed for integration with Django Restframework.
 * list         /api/resources/        GET
 * retrieve     /api/resources/id/     GET
 * create       /api/resources/        POST with params
 * destroy      /api/resources/id/     DELETE
 *
 * */


var restFactory = (function(){
    var _apiURL;
    var _resource;
    function resourceList(onSuccess, onFailure){ 
        easyAjax.ajax({
            method: 'GET',
            url: _apiURL + '/' + _resource + '/',
            success: onSuccess,
            failure: onFailure 
        });
    }
    function resourceRetrieve(id, onSuccess, onFailure){ 
        easyAjax.ajax({
            method: 'GET',
            url: _apiURL + '/' + _resource + '/' + id + '/',
            success: onSuccess,
            failure: onFailure 
        });
    }
    function resourceCreate(params, extraHeaders, onSuccess, onFailure){ 
        easyAjax.ajax({
            method: 'POST',
            url: _apiURL + '/' + _resource + '/',
            params: params,
            headers: extraHeaders,
            success: onSuccess,
            failure: onFailure 
        });
    }
    function resourceDestroy(id, extraHeaders,  onSuccess, onFailure){ 
        easyAjax.ajax({
            method: 'DELETE',
            url: _apiURL + '/' + _resource + '/' + id + '/',
            headers: extraHeaders,
            success: onSuccess,
            failure: onFailure 
        });
    }
    function resourceUpdate(id, params, extraHeaders, isPartial, onSuccess, onFailure){ 
        easyAjax.ajax({
            method: isPartial?'PATCH':'PUT',
            url: _apiURL + '/' + _resource + '/' + id + '/',
            params: params,
            headers: extraHeaders,
            success: onSuccess,
            failure: onFailure 
        });
    }

    function createRestObject(apiURL, resource){
        if (!(/^http:.*/.test(apiURL)) && !(/^https:.*/.test(apiURL))) {
            return;
        }
        _apiURL = apiURL;
        _resource = resource;
        return {
            list : resourceList,
            retrieve : resourceRetrieve,
            create : resourceCreate,
            destroy : resourceDestroy,
            update : resourceUpdate
        };
    }
    return {
        factory : createRestObject
    };
}());
module.exports = restFactory;

},{"./easyajax.js":1}]},{},[2]);
