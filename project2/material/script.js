const container=document.getElementById("snow-container");
function createSnowflake(){
    const snowflake=document.createElement("div");
    snowflake.classList.add("snowflake");
    snowflake.style.left=Math.random()*99+"%";
    container.appendChild(snowflake);

    setTimeout(()=>{
        snowflake.remove();
    },5000);
}
  
  setInterval(createSnowflake,150);