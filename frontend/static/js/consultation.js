const slot_date = document.getElementById('slot-date');
const slot_time = document.getElementById('slot-time');

slot_date.addEventListener('change', function() {
    if (document.getElementById(this.value) == null) {
        slot_time.setAttribute("placeholder", "No slots available for this day *");
        slot_time.setAttribute("list", "");
    } else if (document.getElementById(this.value).children.length == 0) {
        slot_time.setAttribute("placeholder", "No slot left for this day *");
        slot_time.setAttribute("list", "");
    } else {
        slot_time.setAttribute("placeholder", "Pick your time *");
        slot_time.setAttribute("list", this.value);
    }
    slot_time.value = "";
});

slot_time.addEventListener('change', function() {
    var flag = true;

    if (document.getElementById(slot_time.getAttribute("list")) != null) {
        var children = document.getElementById(slot_time.getAttribute("list")).children;
        for (var i = 0; i < children.length; i++) {
            if (this.value == children[i].children[0].value) {
                flag = false;
                break;
            }
        }
    }

    if (flag) {
        slot_time.setAttribute("placeholder", "Please choose a correct value *");
        slot_time.value = "";
    }
});

slot_time.addEventListener("focus", function() {
    slot_time.value = "";
});
