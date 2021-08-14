var button = document.getElementsByClassName('right');
console.log("working");

document.getElementsByClassName('right').onclick = function() {
	alert("I am an alert box!");
	console.log("working: 2");
 	var container = document.getElementsByClassName('slideshow-container');
  	console.log("working: 3");
  	sideScroll(container, 'right', 25, 100, 10);
};

var back = document.getElementsByClassName('left');
back.onclick = function() {
  var container = document.getElementsByClassName('slideshow-container').scrollLeft -= 20;
  //sideScroll(container, 'left', 25, 10, 10);
};

function sideScroll(element, direction, speed, distance, step) {
  scrollAmount = 0;
  var slideTimer = setInterval(function() {
    if (direction == 'left') {
      element.scrollLeft -= step;
    } else {
      element.scrollLeft += step;
    }
    scrollAmount += step;
    if (scrollAmount >= distance) {
      window.clearInterval(slideTimer);
    }
  }, speed);
}
