function sendMessage(){

let input = document.getElementById("chat-input");
let message = input.value;

fetch("/chatbot",{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body:JSON.stringify({message:message})
})

.then(res=>res.json())
.then(data=>{

let chatbox = document.getElementById("chat-box");

chatbox.innerHTML += "<p><b>You:</b> "+message+"</p>";
chatbox.innerHTML += "<p><b>AI:</b> "+data.response+"</p>";

input.value="";

});

}