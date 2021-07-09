$(".toconsultation").click(function(){
	window.location = "/consultation";
});

function CollapseBurger(){
	document.getElementById("burger-items").style.display = "none";
	document.getElementById("burger-menu").innerHTML = "menu";
}

function ExpandBurger(){
	document.getElementById("burger-items").style.display = "block";
	document.getElementById("burger-menu").innerHTML = "close";
}

$("#burger").click(function(){
	if(document.getElementById("burger-items").style.display == "block"){
		CollapseBurger();
	}else{
		ExpandBurger();
	}
});

$(".burger-item").click(function(){
	CollapseBurger();
});

$(".burger-collapsable-item").click(function(){
	var inner_ul = this.getElementsByTagName('ul')[0];
	if(inner_ul.style.display == "block"){
		inner_ul.style.display = "none";
	}else{
		inner_ul.style.display = "block";
	}
});