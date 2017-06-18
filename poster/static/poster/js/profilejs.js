/**
 * Created by MANOHAR on 17-06-2017.
 */
// This just toggles the follow/following of the button
$('a.follow').click(function () {
  $(this).toggleClass('followed');

  if($(this).hasClass('followed')) {
    $(this).text('Followed');
    $('ul li:last-child').html('325<span>Followers</span>');
  }
  else {
    $(this).text('Follow Nick');
    $('ul li:last-child').html('324<span>Followers</span>');
  }
});

//Photos used

//bg http://www.flickr.com/photos/masud/3344695759/
//http://www.flickr.com/photos/andre-batista/378977890/sizes/q/in/photostream/
//http://dribbble.com/shots/959364-Message-Widget-FREE-PSD?list=popular&offset=104
//http://farm4.staticflickr.com/3183/2291622444_422cf7eaf5_q.jpg

$('.poloroid div.name').click(function(){
  $('.poloroid div.name').toggleClass('up');
});
$('.poloroid div.img').click(function(){
  $('.poloroid div.name').toggleClass('up');
});
// Credits - AnimatedHeaderBackgrounds Demo 2 by Rachel Smith - Thanks to Codrops

(function() {
    console.log("Howdy..!! Mr.XXX \n This is Inspired by Codrops\n and Chromebook Login\n and Google I/O 2014 Sandbox (google.com/events/io/sandbox)\t and Curiosity");
    var width, height, largeHeader, canvas, ctx, circles, target, animateHeader = true;

    // Main
    initHeader();
    addListeners();

    function initHeader() {
        width = window.innerWidth;
        height = window.innerHeight;
        target = {x: 0, y: height};
        canvas = document.getElementById('demo-canvas');
        canvas.width = width;
        canvas.height = height;
        ctx = canvas.getContext('2d');

        // create particles
        circles = [];
        for(var x = 0; x < width*0.5; x++) {
            var c = new Circle();
            circles.push(c);
        }
        animate();
    }

    // Event handling
    function addListeners() {
        window.addEventListener('scroll', scrollCheck);
        window.addEventListener('resize', resize);
    }

    function scrollCheck() {
        if(document.body.scrollTop > height) animateHeader = false;
        else animateHeader = true;
    }

    function resize() {
        width = window.innerWidth;
        height = window.innerHeight;
        // largeHeader.style.height = height+'px';
        canvas.width = width;
        canvas.height = height;
    }

    function animate() {
        if(animateHeader) {
            ctx.clearRect(0,0,width,height);
            for(var i in circles) {
                circles[i].draw();
            }
        }
        requestAnimationFrame(animate);
    }

    // Canvas manipulation
    function Circle() {
        var _this = this;

        // constructor
        (function() {
            _this.pos = {};
            init();
        })();

        function init() {
            _this.pos.x = Math.random()*width;
            _this.pos.y = height+Math.random()*100;
            _this.alpha = 0.1+Math.random()*0.3;
            _this.scale = 0.1+Math.random()*0.3;
            _this.velocity = Math.random();
        }

        this.draw = function() {
            if(_this.alpha <= 0) {
                init();
            }
            _this.pos.y -= _this.velocity;
            _this.alpha -= 0.0005;
            ctx.beginPath();
            ctx.arc(_this.pos.x, _this.pos.y, _this.scale*10, 0, 2 * Math.PI, false);
            ctx.fillStyle = 'rgba(255,255,255,'+ _this.alpha+')';
            ctx.fill();
        };
    }

})();