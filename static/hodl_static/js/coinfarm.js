var day = document.querySelectorAll(".day")
day.forEach((day)=>{
    day.addEventListener("click", ()=>{
        day.classList.toggle("clicked")
    })
})

var stakebtn = document.querySelectorAll(".stake");
var bg = document.querySelector(".stake-bg");
var du = document.querySelector(".dura");
var exit = document.querySelector(".close")


stakebtn.forEach((stake) =>{
   stake.addEventListener("click", ()=>{
      bg.classList.add("bg-active");
      du.classList.remove("op")
   })
   
})

exit.addEventListener("click", ()=>{
   bg.classList.remove("bg-active")
   du.classList.add("op")
})


var tab = document.querySelector(".tab1")
var tab2 = document.querySelector(".tab2")
var defi = document.querySelector(".defistaking")
var stake = document.querySelector(".staking")

tab.addEventListener("click", ()=>{
   defi.classList.remove("stake-active")  
   tab.classList.add("line")
   tab2.classList.remove("line")
   stake.classList.remove("stake-deactive")
})

tab2.addEventListener("click", ()=>{
   tab.classList.remove("line")
   tab2.classList.add("line")
   defi.classList.add("stake-active")
   stake.classList.add("stake-deactive")
      
})

