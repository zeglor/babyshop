var cServer = window.location.href;

// adds specified goodie to cart
function add_to_cart(goodie_id, quanitity, price){
	
	//!!
	data = {'goodie_id': 1}
	
	$.ajax({
		url: "{% url 'add_to_cart_async' %}",
		type: "POST",
		contentType: "application/json",
		dataType: "json",
		error: function(error){
			console.log(error);
		},
		success: function(data){
			console.log(data);
		},
	});
}
