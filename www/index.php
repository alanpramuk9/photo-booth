<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Photo booth</title>
  <link rel="stylesheet" href="./assets/js/vendor/flickity/flickity.css">
  <link rel="stylesheet" href="./assets/css/style.css">
</head>

<body>
  <div class="main-carousel">
    <div class="carousel-cell first">
      <div class="outer">
        <div class="inner">
          <img id="bgImg" width="100%">
          <h1>Show your support for innovation in TN</h1>
          <a class="btn btn-start">Take A Selfie</a>
        </div>
      </div>
    </div>
    <div class="carousel-cell">
      <div class="outer">
        <div class="inner input">
          <label for="firstName">First Name</label>
          <input type="text" name="firstName">
          <a class="arrow-next">&#8594;</a>
        </div>
      </div>
    </div>
    <div class="carousel-cell">
      <div class="outer">
        <div class="inner input">
          <label for="lastName">Last Name</label>
          <input type="text" name="lastName">
          <a class="arrow-next">&#8594;</a>
        </div>
      </div>
    </div>
    <div class="carousel-cell">
      <div class="outer">
        <div class="inner input">
          <label for="email">Email</label>
          <input type="email" name="email">
          <a class="arrow-next">&#8594;</a>
        </div>
      </div>
    </div>
    <div class="carousel-cell">
      <div class="outer">
        <div class="inner input">
          <label for="age">Age</label>
          <input type="number" name="age">
          <a class="arrow-next">&#8594;</a>
        </div>
      </div>
    </div>
    <div class="carousel-cell">
      <div class="outer">
        <div class="inner input">
          <label for="zipcode">Zipcode</label>
          <input type="text" name="zipcode">
          <a class="arrow-next">&#8594;</a>
        </div>
      </div>
    </div>
    <div class="carousel-cell">
      <div class="outer">
        <div class="inner">
          <h1>Start your photoshoot.</h1>
          <p>Please stand on
            <strong>X</strong>. We'll create a GIF from 4 pics.</p>
          <a class="btn btn-start-photo-shoot">Take 4 Photos</a>
        </div>
      </div>
    </div>
    <div class="carousel-cell">
      <div class="outer">
        <div class="inner">
          <h1>Stand on the <strong>X</strong></h1>
          <p>Camera preview starting...</p>
        </div>
      </div>
    </div>
    <div class="carousel-cell">
      <div class="outer">
        <div class="inner">
          <h1>Loading</h1>
          <p id="type-block">Creating jobs...</p>
        </div>
      </div>
    </div>
    <div class="carousel-cell last">
      <div class="outer">
        <div class="inner">
          <div>
            <img src="" alt="gif goes here" class="img-preview">
          </div>
          <div>
            <p>We'll soon email your photoshoot.</p>
            <a class="btn btn-finish">Start Over
              (<span id="countdown">19</span>)
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>
  <script src="./assets/js/vendor/jquery.js"></script>
  <script src="./assets/js/vendor/flickity/flickity.js"></script>
  <script src="assets/js/app.js"></script>

  <script>
    /**************
    Slide show
    **************/
    <?php
    $dir = './camera-shots/';
    $images_array = glob($dir.'*.jpg');
    $js_array = json_encode($images_array);
    echo "var js_img_array = ". $js_array . ";\n";
    ?>
    // Array of images which you want to show: Use path you want.
    var images = js_img_array;

    // remove overlays from array for slideshow
    images = $.grep(images, function(val) {
      return val.indexOf("overlay") === -1;
    })
    // show the slideshow
    doSlideshow();

    function doSlideshow(){
      $('#bgImg')
      // .animate({opacity: 0}, 0)
      .attr('src',images[Math.floor(Math.random() * images.length)])
      // .animate({opacity: 1}, 900)
      setTimeout(doSlideshow,4000);
    }
  </script>
</body>

</html>
