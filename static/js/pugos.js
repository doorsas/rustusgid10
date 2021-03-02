// There is no JS in this animation.
// The following just controls the slider for testing speed.


var scrubber = document.getElementById('speed');
var yinyang = document.getElementsByClassName('yinyang')[0];
var yin = document.getElementsByClassName('yin')[0];
var yang = document.getElementsByClassName('yang')[0];

scrubber.addEventListener('change', () => {
  var speed = parseInt(scrubber.max)+1-scrubber.value;
  var speed_half = speed/2;

  yinyang.style.animationDuration = speed + 's';
  yin.style.animationDuration = speed_half + 's';
  yang.style.animationDuration = speed_half + 's';
});