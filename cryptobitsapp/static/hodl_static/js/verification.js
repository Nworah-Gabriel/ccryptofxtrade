var basicbtn = document.querySelector("#basicbtn");
var bg = document.querySelector(".veri-bg");
var exit = document.querySelector(".close")
var submit = document.querySelector(".verify-submit")

basicbtn.addEventListener("click", ()=>{
    bg.classList.add("bg-active");
    submit.classList.remove("op")
})

exit.addEventListener("click", ()=>{
    bg.classList.remove("bg-active")
    submit.classList.add("op")
 })

//  intermmediate
 var interbtn = document.querySelector("#interbtn");
var interbg = document.querySelector(".inter-bg");
var closes = document.querySelector(".inter-modal .close")
var submits = document.querySelector(".inter-modal .verify-submit")

interbtn.addEventListener("click", ()=>{
    interbg.classList.add("bg-active");
    submits.classList.remove("op")
})

closes.addEventListener("click", ()=>{
    interbg.classList.remove("bg-active")
    submit.classList.add("op")
 })


//  advanced
var advabtn = document.querySelector("#advabtn");
var advabg = document.querySelector(".adva-bg");
var clos = document.querySelector(".adva-modal .close")
var sub = document.querySelector(".adva-modal .verify-submit")

advabtn.addEventListener("click", ()=>{
    advabg.classList.add("bg-active");
    sub.classList.remove("op")
})

clos.addEventListener("click", ()=>{
    advabg.classList.remove("bg-active")
    sub.classList.add("op")
 })