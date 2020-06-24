var canvas = document.querySelector('#canvass');
var ctx= canvas.getContext("2d");

canvas.width = 800;
canvas.height = 800;
var rect = canvas.getBoundingClientRect()
console.log(rect)
ctx.fillStyle = "rgb(0,0,0)";
ctx.rect(0,0,800,800)
ctx.fill();

var painting = false;

window.addEventListener("mousedown", (event)=>
{
    painting = true;
    ctx.beginPath();
})
window.addEventListener("mouseup", (event)=>
{
    painting = false;
    ctx.beginPath();
})

window.addEventListener("mousemove", (event)=>
{
    if(painting==true)
    {
        
        ctx.lineWidth = 50;
        ctx.lineCap = 'round';
        ctx.strokeStyle = "rgb(255,255,255)";


        ctx.lineTo(event.offsetX, event.offsetY);
        // console.log(event)
        ctx.stroke();

    }
    


})



// *****************************button

var dataurl = undefined;
var conbtn = document.querySelector("#convert");

var url = document.getElementById('url11')

conbtn.addEventListener("click", ()=>
{
    dataurl = canvas.toDataURL("image/jpeg");
    url.value = dataurl;
    console.log(url.value)
    
})

