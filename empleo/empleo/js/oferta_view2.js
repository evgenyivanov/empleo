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
		
		 
function edite5(arg){

	$.ajax({
            type: 'POST',
            url: '/edite_oferta/',
            data: {
                id: arg,
                csrfmiddlewaretoken: getCookie('csrftoken')
                },
				success: function(data){


      $("#content").html(data);
					
   }
        });
	
	 }

function del3(arg){

	
	
	$.ajax({
            type: 'POST',
            url: '/delete_oferta/',
            data: {
                id: arg,
                csrfmiddlewaretoken: getCookie('csrftoken')
                },
				success: function(msg){
     document.location.href='/';
   }
        });
       

	
	}


function del2(arg){

$( "#dialog" ).dialog( "open" );
	}

function cl(){
	$( "#dialog" ).dialog( "close" );
}

	$(function() {

		$( "#dialog" ).dialog({
			autoOpen: false,
			width: 150,
			height: 100,


		});

		// Link to open the dialog
		$( "#dialog-link" ).click(function( event ) {
			$( "#dialog" ).dialog( "open" );
			//event.preventDefault();

		});

		

		// Hover states on the static widgets
		$( "#dialog-link, #icons li" ).hover(
			function() {
				$( this ).addClass( "ui-state-hover" );
			},
			function() {
				$( this ).removeClass( "ui-state-hover" );
			}
		);
			
			

		
			
	});
	



function chekin(){
fl=true;
	if (window.st=='2'){
	document.location.href='/';
		return false;
	}
	fl = true;
	if ($("#title").val() == ''){
	$("#title").css({"background-color":"pink"});
 fl = false;
	} else {
	$("#title").css({"background-color":"white"});
}
 

if ($("#description").val() == ''){
	$("#description").css({"background-color":"pink"});
	 fl = false;
} else {
$("#description").css({"background-color":"white"});
}
 

 if ($("#description").val() == ''){
	$("#description").css({"background-color":"pink"});
fl = false;
} else {
	$("#description").css({"background-color":"white"});
}
 


 if ($("#requisitos").val() == ''){
	$("#requisitos").css({"background-color":"pink"});
	 fl= false;
 } else {
	$("#requisitos").css({"background-color":"white"});
}
 
var obj=$("#contacto").val();
var n = obj.search("@");

if (obj == ''|| obj == 'example@example.com' || n == -1){
	$("#contacto").css({"background-color":"pink"});
	 fl= false;
}  else {

$("#contacto").css({"background-color":"white"});
}
 

 if ($("#firma").val() == ''){
	$("#firma").css({"background-color":"pink"});
fl = false;
} else {
	$("#firma").css({"background-color":"white"});
}
 

if (fl==true){

	$.ajax({
            type: 'POST',
            url: '/save_oferta/',
            data: {
                id: $("#id").val(),
				title: $("#title").val(),
				areal: $("#areal").val(),
				tipo: $("#tipo").val(),
				description: $("#description").val(),
				requisitos: $("#requisitos").val(),
				email: $("#contacto").val(),
				firma: $("#firma").val(),
				url: $("#url").val(),
                csrfmiddlewaretoken: getCookie('csrftoken')
                },
				success: function(msg){

					if (msg=='0'){
						document.location.href='/';
					}
     if (msg=='1'){
						document.location.href='/oferta_view/'+$("#id").val();
					}
   }
        });
	
}
return false;

}
 








