// ---------Responsive-navbar-active-animation-----------
/*function test(){
    var tabsNewAnim = $('#navbarSupportedContent');
    var selectorNewAnim = $('#navbarSupportedContent').find('li').length;
    var activeItemNewAnim = tabsNewAnim.find('.active');
    var activeWidthNewAnimHeight = activeItemNewAnim.innerHeight();
    var activeWidthNewAnimWidth = activeItemNewAnim.innerWidth();
    var itemPosNewAnimTop = activeItemNewAnim.position();
    var itemPosNewAnimLeft = activeItemNewAnim.position();
    $(".hori-selector").css({
      "top":itemPosNewAnimTop.top + "px", 
      "left":itemPosNewAnimLeft.left + "px",
      "height": activeWidthNewAnimHeight + "px",
      "width": activeWidthNewAnimWidth + "px"
    });
    $("#navbarSupportedContent").on("click","li",function(e){
      $('#navbarSupportedContent ul li').removeClass("active");
      $(this).addClass('active');
      var activeWidthNewAnimHeight = $(this).innerHeight();
      var activeWidthNewAnimWidth = $(this).innerWidth();
      var itemPosNewAnimTop = $(this).position();
      var itemPosNewAnimLeft = $(this).position();
      $(".hori-selector").css({
        "top":itemPosNewAnimTop.top + "px", 
        "left":itemPosNewAnimLeft.left + "px",
        "height": activeWidthNewAnimHeight + "px",
        "width": activeWidthNewAnimWidth + "px"
      });
    });
  }
  $(document).ready(function(){
    setTimeout(function(){ test(); });
  });
  $(window).on('resize', function(){
    setTimeout(function(){ test(); }, 500);
  });
  $(".navbar-toggler").click(function(){
    setTimeout(function(){ test(); });
  });
*/
  /* Demo purposes only */
$(".hover").mouseleave(
  function () {
    $(this).removeClass("hover");
  }
);

$(document).ready(function(){
  $("#food-nav").click(function(){
    $(".food-section").show();
    $(".all-contents").hide();
    $(".food-subpage").show();
    $(".dog-subpage").hide();
    $(".cat-subpage").hide();
    $(".bird-subpage").hide();
    $(".fish-subpage").hide();
    $(".turtle-subpage").hide();
    $(".entire-supply-bar").hide();

   
  });
  $("#supply-nav").click(function(){
    $("entire-food-bar").hide();
    $(".all-contents").hide();
    $(".supply-section").show();
    $(".supply-subpage").show();
    $(".dog-supply-subpage").show();
   
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
 




