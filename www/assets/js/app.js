function getUrlVar(q) {
  return (window.location.search.match(new RegExp('[?&]' + q + '=([^&]+)')) || [, null])[1]
}

// show photo preview
if (getUrlVar('preview')) {
  var previewImgPath = "./camera-shots/" + getUrlVar('preview')
  document.body.innerHTML += '<img src="' + previewImgPath + '"/>';
}

var personInfo = {
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

// startover
$('.btn-finish').click(function () {
  $carousel.flickity( 'select', 0 )
})

$(document).keypress(function (e) {
  if ( e.which==13 ) {
    $carousel.flickity('next')
  }
})

$('.start-photo-shoot').click(function () {
  $.ajax({
      url: "startphotoshoot.php",
      type: "post",
      data: personInfo,
      success: function(data){
        console.log(JSON.parse(data))
        // show photo preview
      }
  })
})
