function toggleFaq(id){
	ans = document.getElementById(id).getElementsByClassName("ans")[0];
	icon = document.getElementById(id).getElementsByClassName("material-icons")[0];

	if( ans.style.display != "block" ){
		ans.style.display = "block";
		icon.innerHTML = 'expand';
	}
	else{
		ans.style.display = "none";
		icon.innerHTML = 'compress';
	}

}