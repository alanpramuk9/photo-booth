// function getUrlVar(q) {
//   return (window.location.search.match(new RegExp('[?&]' + q + '=([^&]+)')) || [, null])[1]
// }

// show photo preview
// if (getUrlVar('preview')) {
//   var previewImgPath = "./camera-shots/" + getUrlVar('preview')
//   document.body.innerHTML += '<img src="' + previewImgPath + '"/>';
// }
var counter,
personInfo = {
  firstName: 'Fred',
  lastName: 'Flintstone',
  phone: '731-555-7777',
  email: 'test@test.com',
  zipcode: '38301',
  age: '31'
}

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

// next slide
$('.btn-start, .arrow-next, .btn-start-photo-shoot').click(function () {
  $carousel.flickity('next')
})

// start over
$('.btn-finish').click(function () {
  location.reload()
})

$(document).keypress(function (e) {
  if ( e.which==13 ) {
    $carousel.flickity('next')
  }
})

$('.btn-start-photo-shoot').click(function () {
  setTimeout(function(){
    $carousel.flickity('next')
  }, 3000)

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