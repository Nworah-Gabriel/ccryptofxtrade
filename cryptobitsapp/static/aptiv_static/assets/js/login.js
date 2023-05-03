var form = document.getElementById("signup");
var inputClose = document.querySelector(".input-close")
var pincode = document.querySelector(".pincode");
var number = document.querySelectorAll(".number")

customerNumber = form.elements["custNumber"]
password = form.elements["password"]


    customerNumber.addEventListener("input", () =>{
        pincode.classList.remove("hide")
        if (customerNumber.value == '' ){
            pincode.classList.add("hide")
        }
    })

 
    inputClose.addEventListener("click", ()=>{
        customerNumber.value = ""
        pincode.classList.add("hide")
    })

 
    // number.forEach(number => {
    //     number.addEventListener("click", () =>{
    //         password.value = parseInt(number.textContent)
    //     })
    // });