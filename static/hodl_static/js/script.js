
        var swiper = new Swiper('.myswiper', {
          navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
          },
          autoplay: true,
          loop: true,
          longSwipes: true,
          longSwipesRatio: 9000,
    
        });



    var swiper = new Swiper('.textslide', {
      navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
      },
      autoplay: true,
      loop: true,
      longSwipes: true,
      longSwipesRatio: 9000,
      direction:'vertical',
      allowTouchMove: false,
      speed:300
      

    });




    var swiper = new Swiper('.flipswipe', {
      navigation: {
        nextEl: '.next',
        prevEl: '.prev',
      },
      effect: "flip",
      grabCursor: true,
      autoplay: false,
      loop: false,
      longSwipes: true,
      longSwipesRatio: 9000,
      allowTouchMove: false,
      speed:1000

    });


    var prev = document.getElementById("flipprev")
    var next = document.getElementById("flipnext")

    prev.addEventListener("click", ()=> {
        next.classList.remove("color")
        prev.classList.add("color")

    })
    next.addEventListener("click", ()=> {
       next.classList.add("color")
       prev.classList.remove("color")

    })


    // about nav side

    $(".p-link").click(()=>{
        // $(".purpose").toggleClass("none")
        $(".p-link").addClass("navcol")
        $(".v-link").removeClass("navcol")
        $(".g-link").removeClass("navcol")

        $(".purpose").removeClass("none")
        $(".values").addClass("none")
        $(".guaran").addClass("none")

    })

    $(".v-link").click(()=>{
        $(".p-link").removeClass("navcol")
        $(".g-link").removeClass("navcol")
        $(".v-link").addClass("navcol")

        $(".purpose").addClass("none")
        $(".values").removeClass("none")
        $(".guaran").addClass("none")


    })

    $(".g-link").click(()=>{
        $(".g-link").addClass("navcol")
        $(".p-link").removeClass("navcol")
        $(".v-link").removeClass("navcol")

        $(".purpose").addClass("none")
        $(".values").addClass("none")
        $(".guaran").removeClass("none")
    })


 
    window.addEventListener("scroll", function(){
  
   $(".navbar2").toggleClass("headerfixed", $(this).scrollTop() > 90)
  
  });
  
 
    window.addEventListener("scroll", function(){
  
   $(".navbar1").toggleClass("navbar11", $(this).scrollTop() > 90)
  
  });
  
 
