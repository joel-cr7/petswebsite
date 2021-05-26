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


// Javascript logic for cart
var updateBtns = document.getElementsByClassName('update-cart')

for(var i=0; i<updateBtns.length; i++){
  updateBtns[i].addEventListener('click', function(){
    var productId = this.dataset.product
    var action = this.dataset.action
    console.log('productId: ',productId, 'action: ',action)
    console.log('USER: ',user)
    if (user === 'AnonymousUser'){
      console.log('Not logged in')
    }
    else{
      updateUserOrder(productId, action)
    }
  })
}

function updateUserOrder(productId, action){
  console.log('User is logged in')

  var url='/update_item/'

  fetch(url, {
    method:'POST',
    headers:{
      'Content-Type':'application/json',
      'X-CSRFToken':csrftoken,
    },
    body:JSON.stringify({'productId':productId, 'action':action})
  })

  .then((response) => {
    return response.json()
  })

  .then((data) => {
    console.log('data: ',data)
    location.reload()
  })

}

function alert_message(){
  alert("Please Login or Signup to continue shopping !!");
}