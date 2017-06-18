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


$(document).ready(function() {
		$(document).delegate('.open', 'click', function(event){
			$(this).addClass('oppenned');
			event.stopPropagation();
		})
		$(document).delegate('body', 'click', function(event) {
			$('.open').removeClass('oppenned');
		})
		$(document).delegate('.cls', 'click', function(event){
			$('.open').removeClass('oppenned');
			event.stopPropagation();
		});
	});