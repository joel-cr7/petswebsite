$(".hover").mouseleave(
  function () {
    $(this).removeClass("hover");
  }
);

$(document).ready(function(){
  $("#dog-nav").click(function(){
    $(".all-contents").hide();
    $(".dog-subpage").show();
    $(".cat-subpage").hide();
    $(".bird-subpage").hide();
    $(".fish-subpage").hide();

   
  });
  $("#cat-nav").click(function(){
    $(".all-contents").hide();
    $(".dog-subpage").hide();
    $(".cat-subpage").show();
    $(".bird-subpage").hide();
    $(".fish-subpage").hide();
   
  });
  $("#fish-nav").click(function(){
    $(".all-contents").hide();
    $(".dog-subpage").hide();
    $(".cat-subpage").hide();
    $(".bird-subpage").hide();
    $(".fish-subpage").show();

   
  });
  $("#bird-nav").click(function(){
    $(".all-contents").hide();
    $(".dog-subpage").hide();
    $(".cat-subpage").hide();
    $(".bird-subpage").show();
    $(".fish-subpage").hide();

   
  });

  /*$("#toys-nav").click(function(){
    $(".food-section").show();
    $(".all-contents").hide();
    $(".food-subpage").show();
    $(".dog-subpage").hide();
    $(".cat-subpage").hide();
    $(".bird-subpage").hide();
    $(".fish-subpage").hide();
    $(".turtle-subpage").hide();
   
  });
*/

  $("#dog-food").click(function(){
    $(".dog-subpage").show();
    $(".food-subpage").hide();
    $(".cat-subpage").hide();
    $(".bird-subpage").hide();
    $(".fish-subpage").hide();
    $(".turtle-subpage").hide();
  })

  $("#cat-food").click(function(){
    $(".cat-subpage").show();
    $(".food-subpage").hide();
    $(".dog-subpage").hide();
    $(".bird-subpage").hide();
    $(".fish-subpage").hide();
    $(".turtle-subpage").hide();

  })
  $("#bird-food").click(function(){
    $(".bird-subpage").show();
    $(".food-subpage").hide();
    $(".dog-subpage").hide();
    $(".cat-subpage").hide();
    $(".fish-subpage").hide();
    $(".turtle-subpage").hide();
  })
  $("#fish-food").click(function(){
    $(".fish-subpage").show();
    $(".food-subpage").hide();
    $(".dog-subpage").hide();
    $(".cat-subpage").hide();
    $(".bird-subpage").hide();
    $(".turtle-subpage").hide();
  })
  $("#turtle-food").click(function(){
    $(".turtle-subpage").show();
    $(".food-subpage").hide();
    $(".dog-subpage").hide();
    $(".cat-subpage").hide();
    $(".bird-subpage").hide();
    $(".fish-subpage").hide();
  })
});
 