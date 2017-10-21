// function getUrlVar(q) {
//   return (window.location.search.match(new RegExp('[?&]' + q + '=([^&]+)')) || [, null])[1]
// }

// show photo preview
// if (getUrlVar('preview')) {
//   var previewImgPath = "./camera-shots/" + getUrlVar('preview')
//   document.body.innerHTML += '<img src="' + previewImgPath + '"/>';
// }
var counter,
personInfo = {}

var $carousel = $('.main-carousel')

$carousel.flickity({
  // options
  cellAlign: 'center',
  contain: true,
  setGallerySize: false,
  prevNextButtons: false,
  pageDots: false,
  draggable: false
})

function nextSlide () {
  // change slide
  $carousel.flickity('next')
  // focus on input in this slide,
  // and wait for next slide to show
  setTimeout(function(){
    if($('.carousel-cell.is-selected :input')[0])
    $('.carousel-cell.is-selected :input')[0].select()
  }, 200)
}

// next slide
$('.btn-start, .arrow-next, .btn-start-photo-shoot').click(function () {
  nextSlide()
})

// next slide w/ ENTER key
$(document).keypress(function (e) {
  if ( e.which==13 ) {
    if($('.carousel-cell.is-selected .btn-start-photo-shoot').length === 1) {
      $('.btn-start-photo-shoot').click()
    } else {
      nextSlide()
    }
  }
})

// start over
$('.btn-finish').click(function () {
  location.reload()
})

// start the photo shoot
$('.btn-start-photo-shoot').click(function () {
  setTimeout(function(){
    $carousel.flickity('next')
  }, 3000)

  // get inputs data
  personInfo.firstName = $( "input[name='firstName']" ).val()
  personInfo.lastName = $( "input[name='lastName']" ).val()
  personInfo.email = $( "input[name='email']" ).val()
  personInfo.zipcode = $( "input[name='zipcode']" ).val()
  personInfo.age = $( "input[name='age']" ).val()

  // // check email
  // checkEmail(personInfo.email)

  $.ajax({
      url: "startphotoshoot.php",
      type: "post",
      data: personInfo,
      success: function(data){
        console.log(JSON.parse(data))
        var previewImgPath = "./camera-shots/" + JSON.parse(data).replace(/["']/g, "")
        // show photo preview
        $('.img-preview').attr('src',previewImgPath)
        $carousel.flickity('next')
        counter = setInterval(timer, 1000)
      }
  })
})

/*
* Text Type
* @link https://jsfiddle.net/chancesmith/xrw41k76/
 */
currentTurn = 0;
textArray = [
  "Creating jobs...",
  "Attending raves...",
  "Writing grants...",
  "Making memories..."
];

function startTyping(index, destinationParam) {
  text = textArray[index];
  currentChar = 1;
  destination = destinationParam;
  type();
}

function type() {
  if (document.getElementById) {
    var dest = document.getElementById(destination);
    if (dest) {
      dest.innerHTML = text.substr(0, currentChar);
      currentChar++
      if (currentChar > text.length) {
        currentChar = 1;
        currentTurn++;
        // // ONCE
        // if (currentTurn <= textArray.length - 1) {
        //   setTimeout("startTyping(currentTurn, 'type-block')", 1700);
        // }
        // or
        // FOREVER
        if (currentTurn > textArray.length - 1) {
          currentTurn = 0;
        }
        setTimeout("startTyping(currentTurn, 'type-block')", 1700);
      } else {
        setTimeout("type()", 70);
      }
    }
  }
}

startTyping(0,'type-block');

//////////
// Count down div
//////////
var count = 19
function timer()
{
  count=count-1;
  if (count <= 0)
  {
     clearInterval(counter)
     location.reload()
     return;
  }
  document.getElementById("countdown").innerHTML=count
}

// /////////
// // validate inputs
// /////////
// function checkEmail(email) {
//   var filter = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;

//   if (!filter.test(email.value)) {
//     alert('Please provide a valid email address');
//     email.focus;
//     return false;
//   }
// }