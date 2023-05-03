var coin = document.getElementById("selectcoin")
var btc = document.getElementById("bitcoin")
var eth = document.getElementById("ethereum")
var dod = document.getElementById("dodge")
var bnb = document.getElementById("bnb")
var xrp = document.getElementById("xrp")
var bch = document.getElementById("bch")
// console.log(select.value)

function stat(){
    switch (coin.value) {
        case "btc":
         
            btc.classList.remove("see")
            eth.classList.add("see")
            dod.classList.add("see")
            bnb.classList.add("see")
            xrp.classList.add("see")
            bch.classList.add("see")
            break;
        case "eth":
            console.log("ethereum")
            btc.classList.add("see")
            eth.classList.remove("see")
            dod.classList.add("see")
            bnb.classList.add("see")
            xrp.classList.add("see")
            bch.classList.add("see")
            break;
        case "dod":
     
            btc.classList.add("see")
            eth.classList.add("see")
            dod.classList.remove("see")
            bnb.classList.add("see")
            xrp.classList.add("see")
            bch.classList.add("see")
            break;
        case "bnb":
      
            btc.classList.add("see")
            eth.classList.add("see")
            dod.classList.add("see")
            bnb.classList.remove("see")
            xrp.classList.add("see")
            bch.classList.add("see")
            break;
        case "xrp":
  
            btc.classList.add("see")
            eth.classList.add("see")
            dod.classList.add("see")
            bnb.classList.add("see")
            xrp.classList.remove("see")
            bch.classList.add("see")
            break;
        case "bch":
   
            btc.classList.add("see")
            eth.classList.add("see")
            dod.classList.add("see")
            bnb.classList.add("see")
            xrp.classList.add("see")
            bch.classList.remove("see")
            break;
    
        default:

            btc.classList.remove("see")
            eth.classList.add("see")
            dod.classList.add("see")
            bnb.classList.add("see")
            xrp.classList.add("see")
            bch.classList.add("see")
            break;
    }
}

stat()
