var navSpeed = 0.8;

function fadeoutslide(slide, slide2, opacity=1){
	if (opacity > -1){
		opacity -= navSpeed;
		setTimeout(function(){fadeoutslide(slide, slide2, opacity)}, 100);
	}
	else{
		opacity = 0;
		slide.className = 'slide-inactive';
		fadeinslide(slide2);
	}
	slide.style.opacity = opacity;
}
function fadeinslide(slide, opacity=0){
	if(opacity == 0){
		slide.className = 'slide-active';
		slide.style.opacity = 0;
	}
	if (opacity < 2){
		opacity += navSpeed;
		setTimeout(function(){fadeinslide(slide, opacity)}, 100);
	}
	else{
		opacity = 1;
	}
	slide.style.opacity = opacity;
}
function navigate(operation){
	var slide_active = document.getElementsByClassName('slide-active')[0];
	var slide_to_be_active = document.getElementById( parseInt(slide_active.getAttribute('id')) + operation );

	if (slide_to_be_active != null && slide_to_be_active.className == "slide-inactive"){
		fadeoutslide(slide_active, slide_to_be_active);
	}
}

function checknavigation(){
	var slideshow_div = document.getElementById("slideshowdiv");
	var slide_active = document.getElementsByClassName('slide-active')[0];
	if (slide_active.getAttribute('id') == slideshow_div.children.length){
		fadeoutslide(slide_active, slideshow_div.children[0]);
	}
	else{
		navigate(1);
	}
	setTimeout(function(){
		checknavigation();
	}, 1000 * 5);
}

setTimeout(function(){
	checknavigation();
}, 1000 * 5);