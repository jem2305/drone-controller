var up = false,
right = false,
down = false,
left = false,

maxDeg = 30,
minDeg = -30,
initDeg = 0,
deg = 0,

maxX = window.innerWidth/2-130/2 + 150,
minX = window.innerWidth/2-130/2 - 150,
initX = window.innerWidth/2-130/2,
x = window.innerWidth/2-130/2,

maxY = window.innerHeight/2-130/2 + 150,
minY = window.innerHeight/2-130/2 - 150,
initY = window.innerHeight/2-130/2,
y = window.innerHeight/2-130/2

document.addEventListener('keydown',press)
function press(e){
  if (e.keyCode === 38 /* up */ || e.keyCode === 87 /* w */ || e.keyCode === 90 /* z */){
    up = true
  }
  if (e.keyCode === 39 /* right */ || e.keyCode === 68 /* d */){
    right = true
  }
  if (e.keyCode === 40 /* down */ || e.keyCode === 83 /* s */){
    down = true
  }
  if (e.keyCode === 37 /* left */ || e.keyCode === 65 /* a */ || e.keyCode === 81 /* q */){
    left = true
  }
}
document.addEventListener('keyup',release)
function release(e){
  if (e.keyCode === 38 /* up */ || e.keyCode === 87 /* w */ || e.keyCode === 90 /* z */){
    up = false
  }
  if (e.keyCode === 39 /* right */ || e.keyCode === 68 /* d */){
    right = false
  }
  if (e.keyCode === 40 /* down */ || e.keyCode === 83 /* s */){
    down = false
  }
  if (e.keyCode === 37 /* left */ || e.keyCode === 65 /* a */ || e.keyCode === 81 /* q */){
    left = false
  }
}
function sendDroneCommand(direction){
  var xhr = new XMLHttpRequest();
  xhr.open("GET", "http://localhost:5000/"+direction, true);
  xhr.onload = function (e) {
    if (xhr.readyState === 4) {
      if (xhr.status === 200) {
        console.log(xhr.responseText);
      } else {
        console.error(xhr.statusText);
      }
    }
  };
  xhr.onerror = function (e) {
    console.error(xhr.statusText);
  };
  xhr.send(null); 
}
function gameLoop(){
  var div = document.querySelector('img')
  if(up) {
    sendDroneCommand("forward")
  }
  if(down) {
    sendDroneCommand("backward")
  }
  if(left) {
    sendDroneCommand("left")
  }
  if(right) {
    sendDroneCommand("right")
  }

  if (up && !(y < minY)){
    y = y - 10
  }
  if (down && !(y > maxY)){
    y = y + 10
  }

  if (right && (up || down) && !(x > maxX)) {
    x = x + 10
  }
  if (left && (up || down) && !(x < minX)) {
    x = x - 10
  }

  if (((!down && right) || (down && left)) && !(deg > maxDeg)){
    deg = deg + 5
  }
  if (((!down && left) || (down && right)) && !(deg < minDeg)){
    deg = deg - 5
  }

  if(!(left || right) && deg != initDeg) {
    if (deg > initDeg) { deg = deg - Math.min(10, deg) }
    else if (deg < initDeg) { deg = deg + Math.min(10, Math.abs(deg)) }

  }

  if(!(left || right || up || down) && x != initX) {
    if (x > initX) { x = x - Math.min(10, x - initX) }
    else { x = x + Math.min(10, initX - x) }
  }


  if(!(up || down) && y != initY) {
    if (y > initY) { y = y - Math.min(10, y - initY) }
    else { y = y + Math.min(10, initY - y) }
  }

  div.style.left = x+'px'
  div.style.top = y+'px'

  if (deg < 0) {
    div.style.transform = 'rotate(+'+ (360 + deg) +'deg)'
  }
  else {
    div.style.transform = 'rotate(+'+ deg +'deg)'
  }
  window.requestAnimationFrame(gameLoop)
}
window.requestAnimationFrame(gameLoop)