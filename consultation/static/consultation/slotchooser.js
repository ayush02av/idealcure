$("#slot-date").change(function() {
	if(document.getElementById($(this).val()) == null){
		document.getElementById("slot-time").setAttribute("placeholder", "No slots available for this day *");
		document.getElementById("slot-time").setAttribute("list", "");
	}
	else if(document.getElementById($(this).val()).children.length == 0){
		document.getElementById("slot-time").setAttribute("placeholder", "No slot left for this day *");
		document.getElementById("slot-time").setAttribute("list", "");
	}
	else{
		document.getElementById("slot-time").setAttribute("placeholder", "Pick your time *");
		document.getElementById("slot-time").setAttribute("list", $(this).val());
	}
	document.getElementById("slot-time").value = "";
});

$("#slot-time").change(function(){
	var flag = true;

	if(document.getElementById(document.getElementById("slot-time").getAttribute("list")) != null){
		var children = document.getElementById(document.getElementById("slot-time").getAttribute("list")).children;
		for(var i = 0; i < children.length; i++){
			if( $(this).val() == children[i].children[0].value){
				flag = false;
				break;
			}
		}
	}


	if(flag){
		document.getElementById("slot-time").setAttribute("placeholder", "Please choose a correct value *");
		document.getElementById("slot-time").value = "";
	}
});

$("#slot-time").focus(function(){
	document.getElementById("slot-time").value = "";
});