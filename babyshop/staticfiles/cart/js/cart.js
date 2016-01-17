var cServer = window.location.href;

// Adds specified goodie to cart
function add_to_cart(cart_url, goodie_id, goodie_quantity, callback=function(){}){
	data = {'id': goodie_id, 'quantity': goodie_quantity}
	json_data = JSON.stringify(data);
	console.log("Sending data " + json_data + " to url " + cart_url);
	
	// Get csrf token value
	csrftoken = getCookie("csrftoken");
	
	// Send data
	$.ajax({
		url: cart_url,
		type: "POST",
		contentType: "application/json",
		dataType: "json",
		data: json_data,
		error: function(error){
			console.log(error);
		},
		success: function(data){
			console.log(data);
			callback();
		},
	});
}

// Checks if given method is crsf safe
function csrfSafeMethod(method){
	// these HTTP methods dont require csrf protection
	return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

// Gets cookie value
function getCookie(name){
	var cookieValue = null;
	if (document.cookie && document.cookie != ''){
		var cookies = document.cookie.split(';');
		for (var i=0; i<cookies.length; i++){
			var cookie = jQuery.trim(cookies[i]);
			if (cookie.substring(0, name.length + 1) == (name + '=')){
				cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
				break;
			}
		}
	}
	return cookieValue;
}
