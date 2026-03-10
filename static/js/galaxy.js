const scene = new THREE.Scene();

const camera = new THREE.PerspectiveCamera(
75,
window.innerWidth/window.innerHeight,
0.1,
1000
);

const renderer = new THREE.WebGLRenderer();

renderer.setSize(window.innerWidth,window.innerHeight);

document.getElementById("galaxy").appendChild(renderer.domElement);


const starsGeometry = new THREE.BufferGeometry();

const starCount = 10000;

const positions = new Float32Array(starCount * 3);

for(let i=0;i<starCount*3;i++){

positions[i]=(Math.random()-0.5)*2000;

}

starsGeometry.setAttribute(
'position',
new THREE.BufferAttribute(positions,3)
);

const starsMaterial = new THREE.PointsMaterial({

color:0x8a2be2,
size:2

});

const starField = new THREE.Points(
starsGeometry,
starsMaterial
);

scene.add(starField);

camera.position.z = 500;


function animate(){

requestAnimationFrame(animate);

starField.rotation.y += 0.0005;

renderer.render(scene,camera);

}

animate();