const block_height = 500
const y_top = 80;
const y_bot = y_top + block_height;
const navigate_slide_time_interval = 5;

function x_percentage(mouse_event){
	var x_clicked_at = mouse_event.pageX;
	var window_width = $(window).width();
	return (x_clicked_at/window_width)*100;
}

function activate_navigation_button(button_id){
	document.getElementById(button_id).classList.add("active");
}

function deactivate_navigation_button(button_id){
	document.getElementById(button_id).classList.remove("active");
}

function navigate_slide(navigate_operation, stop_navigation=false){
	var current_slide = document.querySelector(".slide.active");
	var current_id = current_slide.getAttribute("id");
	
	var new_id = parseInt(current_id.replace("slide", ""))+parseInt(navigate_operation);
	var new_slide = document.getElementById("slide"+new_id);
	if(new_slide == null){
		if(navigate_operation == "1"){
			new_slide = document.getElementById("slide1");
		}else{
			new_slide = document.querySelectorAll(".slide");
			new_slide = new_slide[new_slide.length-1];
		}
	}
	current_slide.classList.remove("active");
	new_slide.classList.add("active");

	if(stop_navigation){
		Stop_Navigation();
	}
}

$(document).bind('mousemove',function(mouse_event){
	var x_pos = mouse_event.pageX;
	var y_pos = mouse_event.pageY;

	if(y_pos >= y_top && y_pos <= y_bot){
		if(x_percentage(mouse_event) <= 6){
			activate_navigation_button("nav-left");
			deactivate_navigation_button("nav-right");
		}else if(x_percentage(mouse_event) >= 94){
			activate_navigation_button("nav-right");
			deactivate_navigation_button("nav-left");
		}else{
			deactivate_navigation_button("nav-left");
			deactivate_navigation_button("nav-right");
		}
	}else{
		deactivate_navigation_button("nav-left");
		deactivate_navigation_button("nav-right");
	}
});

let navigate_slides = setInterval(Navigate_Slides, 1000 * navigate_slide_time_interval)

function Navigate_Slides(){
	navigate_slide(1);
}

function Start_Navigation(){
	var navigate_slides = setInterval(Navigate_Slides, 1000 * navigate_slide_time_interval)	
}

function Stop_Navigation(){
	clearInterval(navigate_slides);
	navigate_slides = setInterval(Navigate_Slides, 1000 * navigate_slide_time_interval);
}