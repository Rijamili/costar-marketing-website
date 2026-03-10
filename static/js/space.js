const canvas = document.getElementById("space");
const ctx = canvas.getContext("2d");

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

let stars = [];

for (let i = 0; i < 200; i++) {

stars.push({
x: Math.random() * canvas.width,
y: Math.random() * canvas.height,
size: Math.random() * 2,
speed: Math.random() * 0.5
});

}

function animate(){

ctx.clearRect(0,0,canvas.width,canvas.height);

ctx.fillStyle = "white";

stars.forEach(star => {

star.y += star.speed;

if(star.y > canvas.height){
star.y = 0;
}

ctx.beginPath();
ctx.arc(star.x, star.y, star.size, 0, Math.PI * 2);
ctx.fill();

});

requestAnimationFrame(animate);

}

animate();