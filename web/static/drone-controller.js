var up = false,
right = false,
down = false,
left = false,

maxDeg = 30,
minDeg = -30,
initDeg = 0,
deg = 0,

maxX = window.innerHeight * 0.15 - 172/2,
minX = -(window.innerHeight * 0.15) - 172/2,
initX = 0 - 172/2,
x = 0 - 172/2,

centerLineMargin = -5000

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
  sendDroneCommands(up, down, left, right)
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
  sendDroneCommands(up, down, left, right)
}
function updateStatusWithResponse(statusResponse) {
  var droneResponse = JSON.parse(statusResponse);

  var droneSpeedDiv = document.getElementById("drone-speed");
  var droneDirectionDiv = document.getElementById("drone-drive-direction");
  var droneSteeringDiv = document.getElementById("drone-steering-direction");
  var droneConnectionStatusDiv = document.getElementById("drone-connection-status");

  droneSpeedDiv.textContent = droneResponse.speed;
  droneDirectionDiv.textContent = droneResponse.driveDirection;
  droneSteeringDiv.textContent = droneResponse.steeringDirection;
  droneConnectionStatusDiv.textContent = droneResponse.isConnected;
}
function sendDroneCommand(direction){
  var xhr = new XMLHttpRequest();
  xhr.open("GET", "http://localhost:5000/"+direction, true);
  xhr.onload = function (e) {
    if (xhr.readyState === 4) {
      if (xhr.status === 200) {
        updateStatusWithResponse(xhr.response);
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
function sendDroneCommands(up, down, left, right) {
  if (up) {
    sendDroneCommand("forward")
  }
  else if (down) {
    sendDroneCommand("reverse")
  }
  else {
    sendDroneCommand("stop")
  }

  if (left) {
    sendDroneCommand("left")
  }
  else if (right) {
    sendDroneCommand("right")
  }
  else {
    sendDroneCommand("straight")
  }
}
function gameLoop(){
  var car = document.getElementById('car')
  var road = document.getElementById('road')
  var roadCenterLine = document.getElementById('road-center-line')

  if (down && !(x > maxX)) {
    x = x + 10
  }
  if (up && !(x < minX)) {
    x = x - 10
  }

  if (!(deg < minDeg) && down && right) {
    deg = deg - 2.5
  }
  else if (!(deg > maxDeg) && down && left) {
    deg = deg + 2.5
  }
  else if (!(deg > maxDeg) && right && !(down && right)) {
    deg = deg + 2.5
  }
  else if (!(deg < minDeg) && left && !(down && left)) {
    deg = deg - 2.5
  }

  if(!(left || right) && deg != initDeg) {
    if (deg > initDeg) { deg = deg - Math.min(2.5, deg) }
    else if (deg < initDeg) { deg = deg + Math.min(2.5, Math.abs(deg)) }
  }

  if(!(up || down) && x != initX) {
    if (x > initX) { x = x - Math.min(10, x - initX) }
    else { x = x + Math.min(10, initX - x) }
  }

  car.style.marginTop = x+'px'

  if (deg < 0) {
    road.style.transform = 'rotate(+'+ (360 + deg) +'deg)'
  }
  else {
    road.style.transform = 'rotate(+'+ deg +'deg)'
  }

  if (up) {
    centerLineMargin = centerLineMargin >= -500 ? -5000 : centerLineMargin + 3;
  }
  else if (down) {
    centerLineMargin = centerLineMargin <= -9500 ? -5000 : centerLineMargin - 3;
  }
  roadCenterLine.style.marginTop = centerLineMargin+'px';

  window.requestAnimationFrame(gameLoop)
}
function sendConnectCommand() {
  var xhr = new XMLHttpRequest();
  xhr.open("GET", "http://localhost:5000/connect", true);
  xhr.onload = function (e) {
    if (xhr.readyState === 4) {
      if (xhr.status === 200) {
        updateStatusWithResponse(xhr.response);
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
function sendDisconnectCommand() {
  var xhr = new XMLHttpRequest();
  xhr.open("GET", "http://localhost:5000/disconnect", true);
  xhr.onload = function (e) {
    if (xhr.readyState === 4) {
      if (xhr.status === 200) {
        updateStatusWithResponse(xhr.response);
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
window.requestAnimationFrame(gameLoop)
window.setInterval( function() { sendDroneCommands(up, down, left, right); }, 1000)
sendDroneCommands(up, down, left, right)

window.onload = (event) => {
  document.getElementById("connect-button").addEventListener("click", sendConnectCommand);
  document.getElementById("disconnect-button").addEventListener("click", sendDisconnectCommand);
};