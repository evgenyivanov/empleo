function palabra_cl(){
  $("#palabra_clave").css({"color":"black", "font-style": "normal"});

}

function fnt(arg){

if (arg != '##'){
var ar = arg;
window.pg=arg;
} else {
  ar = window.pg;

}
var areal = $("#areal").val();
var tipo = $("#tipo").val();
var palabra_clave = $("#palabra_clave").val();
if (document.getElementsByName('sr')[0].checked){
 var sr = 1;
} else {
 var sr=2;
}

$.post("/next_page/", {

pages: ar,
areal: areal,
type: tipo,
palabra_clave: palabra_clave,
sr: sr,
 },
 function(data) {

  $("#next_page").html(data);

}
);

  
}



