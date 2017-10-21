<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Photo booth</title>
  <link rel="stylesheet" href="https://npmcdn.com/flickity@2/dist/flickity.css">
  <link rel="stylesheet" href="./assets/css/style.css"> </head>

<body>
  <div class="main-carousel">
    <div class="carousel-cell first">
      <div class="outer">
        <div class="inner">
          <h1>Photo Booth</h1>
          <a class="btn btn-start">Get Started</a>
        </div>
      </div>
    </div>
    <div class="carousel-cell">
      <div class="outer">
        <div class="inner">
          <label for="firstName">First Name</label>
          <input type="text" name="firstName">
          <a class="arrow-next">&#8594;</a>
        </div>
      </div>
    </div>
    <div class="carousel-cell">
      <div class="outer">
        <div class="inner">
          <label for="lastName">Last Name</label>
          <input type="text" name="lastName">
          <a class="arrow-next">&#8594;</a>
        </div>
      </div>
    </div>
    <div class="carousel-cell">
      <div class="outer">
        <div class="inner">
          <label for="email">Email</label>
          <input type="email" name="email">
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
    <div class="carousel-cell last">
      <div class="outer">
        <div class="inner">
          <div>
            <img src="./camera-shots/08a2811b-7dbb-4be7-be0d-9efc63bcfab2.gif" class="img-preview">
          </div>
          <div>
            <a class="btn btn-finish">Start Over
              <span id="count-down">19</span>
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>
  <script src="https://unpkg.com/jquery@3.2.1/dist/jquery.js"></script>
  <script src="https://npmcdn.com/flickity@2/dist/flickity.pkgd.js"></script>
  <script src="assets/js/app.js"></script>
</body>

</html>