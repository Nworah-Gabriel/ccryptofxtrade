//packages
var modal = document.querySelector(".modal-bg")
var usermodal = document.querySelector(".usermodal-bg")
var exit = document.querySelector(".close")
var exit2 = document.querySelector(".close")
var button = document.querySelectorAll(".card-body button")
var edit = document.querySelectorAll(".editbtn")
var usercard = document.querySelector(".usercard")


button.forEach((bn)=>{
    bn.addEventListener("click", ()=>{
       modal.classList.add("bg-active")
    })
})

exit.addEventListener("click", ()=>{
    modal.classList.remove("bg-active")
 })
exit2.addEventListener("click", ()=>{
    usercard.classList.add("op")
    usermodal.classList.remove("bg-active")
    
    
 })



 edit.forEach((ed)=>{
     ed.addEventListener("click", ()=>{
        usermodal.classList.add("bg-active")
        usercard.classList.remove("op")
     })
 })