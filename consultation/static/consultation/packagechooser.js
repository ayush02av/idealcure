const initial_background = "initial";
const new_background = "lightblue";
const hover_background = "lightyellow";

function ChoosePackage(package){
	var other_packages = $(".package-card");
	other_packages.css("background-color", initial_background);

	var chosen_package = $("#"+package.id);
	chosen_package.css("background", new_background);

	var radio = package.getElementsByTagName('input')[0];
	radio.checked = true;
}

function ProceedToPayment(){
	$("#payment").css("display", "block");
}