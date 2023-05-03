var day = document.querySelectorAll(".day");
const shortTime = document.getElementById("shortTime");
const midTime = document.getElementById("midTime");
const longTime = document.getElementById("longTime");

const midTimeNow = document.getElementById("midTimeNow");
const longTimeNow = document.getElementById("longTimeNow");
const shortTimeNow = document.getElementById("shortTimeNow");

function setdates(days){
   console.log("chill")
   var d = new Date();
   var days= days;
   var value_date = new Date(d);
   value_date.setDate(d.getDate() + days+1);

   var interest_end_date = new Date(d);
   interest_end_date.setDate(d.getDate() + days +1);



   $('#iInterestPeriod').html( days  + "<b> day(s)</b>");

   $('#iStakeDate').text(d.toLocaleString() );

   $('#iValueDate').text(value_date.toLocaleString());
   
   $('#iInterestendDate').text(interest_end_date.toLocaleString() );


   sub_stake_date = document.getElementById("id_stake_date");
   sub_value_date = document.getElementById("id_value_date");
   sub_interest_end_date = document.getElementById("id_interest_end_date");  
   sub_interest_period = document.getElementById("id_interest_period"); 
   sub_stock_name = document.getElementById("id_stock_name");
   

   sub_stake_date.value = d.getTime() / 1000;
   sub_value_date.value = value_date.getTime() / 1000;
   sub_interest_end_date.value = interest_end_date.getTime() / 1000;
   sub_interest_period.value = days;
   sub_stock_name.value = $('#TokenName').text();
   




   // sub_stake_date.value = now_stake_date;
   console.log(sub_stake_date.value);


}

day.forEach((day)=>{
    day.addEventListener("click", ()=>{
        day.classList.toggle("clicked");
      
        if (day.id === "midTime"){
         if (day.classList.contains("clicked")){
            shortTime.classList.remove("clicked");
            longTime.classList.remove("clicked");
            document.getElementById("midInt").style.display = "block";
           document.getElementById("shortInt").style.display = "none";
           document.getElementById("longInt").style.display = "none";
           setdates(14);
         //   var d = new Date();
         //   $('#iStakeDate').text(d.toISOString());
           

        
         };
        
         }
         else if (day.id === "shortTime"){
            if (day.classList.contains("clicked")){
               midTime.classList.remove("clicked");
               longTime.classList.remove("clicked");
               document.getElementById("shortInt").style.display = "block";
               document.getElementById("midInt").style.display = "none";
               document.getElementById("longInt").style.display = "none";
               setdates(7);
            };
            }
             
         else if (day.id === "longTime"){
            if (day.classList.contains("clicked")){
               shortTime.classList.remove("clicked");
               midTime.classList.remove("clicked");
               document.getElementById("longInt").style.display = "block";
               document.getElementById("shortInt").style.display = "none";
               document.getElementById("midInt").style.display = "none";
               setdates(30);
              
               };
           
             }
             




         else if (day.id === "midTimeNow"){
            if (day.classList.contains("clicked")){

               var now_time_div = day.parentNode;
               now_time_div.querySelector('.shortTimeNowcl').classList.remove("clicked");
               now_time_div.querySelector('.longTimeNowcl').classList.remove("clicked");
              

              
               var now_int_div = day.parentNode.parentNode.parentNode.parentNode;
               now_int_div.querySelector('.intNow .shortIntNowcl').style.display = "none";
               now_int_div.querySelector('.intNow .midIntNowcl').style.display = "block";
               now_int_div.querySelector('.intNow .longIntNowcl').style.display = "none";


            };
            }

        
          else if (day.id === "shortTimeNow"){
            if (day.classList.contains("clicked")){
               var now_time_div = day.parentNode;
               now_time_div.querySelector('.longTimeNowcl').classList.remove("clicked");
               now_time_div.querySelector('.midTimeNowcl').classList.remove("clicked");
               
               
               var now_int_div = day.parentNode.parentNode.parentNode.parentNode;
               

               now_int_div.querySelector('.intNow .shortIntNowcl').style.display = "block";
               now_int_div.querySelector('.intNow .midIntNowcl').style.display = "none";
               now_int_div.querySelector('.intNow .longIntNowcl').style.display = "none";
            
               };
           
             }
            else if (day.id === "longTimeNow"){
               if (day.classList.contains("clicked")){
               var now_time_div = day.parentNode;
               now_time_div.querySelector('.shortTimeNowcl').classList.remove("clicked");
               now_time_div.querySelector('.midTimeNowcl').classList.remove("clicked");
               

               var now_int_div = day.parentNode.parentNode.parentNode.parentNode;
               
               now_int_div.querySelector('.intNow .shortIntNowcl').style.display = "none";

               now_int_div.querySelector('.intNow .midIntNowcl').style.display = "none";

               now_int_div.querySelector('.intNow .longIntNowcl').style.display = "block";
              
                  };
              
                }
          else{
            if (day.classList.contains("clicked")){
               midTime.classList.remove("clicked");
               longTime.classList.remove("clicked");
               const day_value = document.getElementById("shortInt");
               document.getElementById("midInt").style.display = "none";
               document.getElementById("longInt").style.display = "none";
               day_value.style.display = "block";
            };
          
          }

           
 
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

