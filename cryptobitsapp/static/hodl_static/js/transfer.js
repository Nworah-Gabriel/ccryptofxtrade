var transbtn = document.querySelector(".transfer");
var bgo = document.querySelector(".trans-bg");
var exito = document.querySelector(".exito");
var fin = document.querySelector(".finish");

transbtn.addEventListener("click", ()=>{
    bgo.classList.add("bg-active");
    fin.classList.remove("op")
 })

exito.addEventListener("click", ()=>{
    bgo.classList.remove("bg-active")
    fin.classList.add("op")
 })

