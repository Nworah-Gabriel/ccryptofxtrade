var depositModal = document.querySelector(".deposit-modal")
var withdrawModal  = document.querySelector(".withdraw-modal")
var swapModal  = document.querySelector(".swap-modal")
var createModal  = document.querySelector(".create-modal")
var optionModal  = document.querySelector(".option-modal")

var depositBtn = document.querySelectorAll(".deposit")
var withdrawBtn = document.querySelectorAll(".withdraw")
var swapBtn = document.querySelectorAll(".swap")
var createBtn = document.querySelectorAll(".create")
var optionBtn = document.querySelectorAll(".option")

var closeBtn = document.querySelectorAll(".close")
var walletmodal = document.querySelector(".walletmodals")


function scrollUp(){
    return $("html, body").animate({
        scrollTop: 50
    }, 50), !1
}


depositBtn.forEach((deposit) => {
   
    deposit.addEventListener("click", () =>{
        scrollUp()
        depositModal.classList.add("display")
        optionModal.classList.remove("display")
        swapModal.classList.remove("display")
        withdrawModal.classList.remove("display")
        createModal.classList.remove("display")
        walletmodal.classList.add("modal-show")
        
      
        
    })
});

createBtn.forEach((deposit) => {
   
    create.addEventListener("click", () =>{
        scrollUp()
        depositModal.classList.remove("display")
        optionModal.classList.remove("display")
        createModal.classList.add("display")
        swapModal.classList.remove("display")
        withdrawModal.classList.remove("display")
        walletmodal.classList.add("modal-show")
        
      
        
    })
});
withdrawBtn.forEach((withdraw) => {
    withdraw.addEventListener("click", () =>{
        scrollUp()
        withdrawModal.classList.add("display")
        depositModal.classList.remove("display")
        swapModal.classList.remove("display")
        createModal.classList.remove("display")
        optionModal.classList.remove("display")
        walletmodal.classList.add("modal-show")
    })
});
swapBtn.forEach((swap) => {
   swap.addEventListener("click", () =>{
    scrollUp()
   swapModal.classList.add("display")
   depositModal.classList.remove("display")
   withdrawModal.classList.remove("display")
   optionModal.classList.remove("display")
   createModal.classList.remove("display")
   walletmodal.classList.add("modal-show")
    })
});
optionBtn.forEach((option) => {
    option.addEventListener("click", () =>{
        scrollUp()
        optionModal.classList.add("display")
        depositModal.classList.remove("display")
        swapModal.classList.remove("display")
        withdrawModal.classList.remove("display")
        createModal.classList.remove("display")
        walletmodal.classList.add("modal-show")
    })
});

closeBtn.forEach((btn) =>{

   closing(btn)
  
})


 function closing(closeIcon) {
    closeIcon.addEventListener("click", ()=> {
        depositModal.classList.remove("display")
        withdrawModal.classList.remove("display")
        swapModal.classList.remove("display")
        optionModal.classList.remove("display")
        walletmodal.classList.remove("modal-show")

    })
 }

 


var coinButton = document.getElementById("coinBtn")
var coinButton2 = document.getElementById("coinBtn2")

// for your price
var cbtnp = document.getElementById("coinBtnp")
var cbtnp2 = document.getElementById("coinBtnp2")

var chooseCoin = document.querySelectorAll(".choose-coin")
var chooseCoinTo = document.querySelectorAll(".choose-coin-to")

var coinName = document.querySelectorAll(".coinName")
var coinName2 = document.querySelectorAll(".coinName2")

coinButton.addEventListener("click", ()=>{
    pickCoin(chooseCoin)
    pickCoin(chooseCoinTo)
    
})

coinButton2.addEventListener("click", ()=>{
    pickCoin(chooseCoin)
    pickCoin(chooseCoinTo)
    
})

cbtnp.addEventListener("click", ()=>{
  pickCoin(chooseCoin)
  pickCoin(chooseCoinTo)
})
cbtnp2.addEventListener("click", ()=>{
  pickCoin(chooseCoin)
  pickCoin(chooseCoinTo)
})


function pickCoin(pickedCoin){
    pickedCoin.forEach(coinpicked => {
        coinpicked.addEventListener("click", ()=>{
            if(pickedCoin == chooseCoin){
                coinButton.innerHTML = coinpicked.innerHTML
                coinButton.appendChild(chev);
                cbtnp.innerHTML = coinpicked.innerHTML
                cbtnp.appendChild(chev);
                coinName.forEach(coinname => {
                    coinname.innerText = coinpicked.innerText
                });
                
            }else{
                coinButton2.innerHTML = coinpicked.innerHTML
                coinButton2.appendChild(chev);
                cbtnp2.innerHTML = coinpicked.innerHTML
                cbtnp2.appendChild(chev);
                coinName2.forEach(coinname => {
                    coinname.innerText = coinpicked.innerText
                });
                
            }
        })
    })

    var chev = document.createElement("i")
    chev.classList.add("fa", "fa-chevron-right")
    chev.style.fontSize = ".9rem"

}


