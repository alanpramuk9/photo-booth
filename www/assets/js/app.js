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

$.ajax({
    url: "startphotoshoot.php",
    type: "post",
    data: personInfo,
    success: function(data){
      console.log(JSON.parse(data))
    }
});