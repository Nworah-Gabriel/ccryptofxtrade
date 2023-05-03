const prevBtn = document.querySelectorAll(".btn-prev");
const nextBtn = document.querySelectorAll(".btn-next");
const progress = document.getElementById("progress");
const steps =  document.querySelectorAll(".steps");
const progressSteps = document.querySelectorAll(".progress-step");

let stepsNum = 0;

nextBtn.forEach( (btn) => {
    btn.addEventListener("click", () =>{
        stepsNum++;
        updateSteps();
        updateProgressBar();
    })
})

prevBtn.forEach( (btn) => {
    btn.addEventListener("click", () =>{
        stepsNum--;
        updateSteps();
        updateProgressBar();
    })
})

function updateSteps(){
   
    steps.forEach((step) => {
        step.classList.contains("step-active") &&
        step.classList.remove("step-active")
    })

    steps[stepsNum].classList.add("step-active");

   
}

function updateProgressBar(){

    progressSteps.forEach ((progressStep, idx) => {

        if(idx < stepsNum +1){
            progressStep.classList.add("progress-step-active")
        }else{
            progressStep.classList.remove("progress-step-active")
        }
    })

    const progressActive = document.querySelectorAll(".progress-step-active");

    progress.style.width = ((progressActive.length -1)/(progressSteps.length -1) * 100 + "%"); 
    // we did the above because we want the progress to start from 0% since we are starting 
    // from state 1 (progress active is 1, (1-1)/(1-1) * 100% = 0)
}