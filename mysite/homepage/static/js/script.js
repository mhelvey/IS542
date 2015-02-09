/**
 * Created by mhelvey on 2/9/15.
 */
$(function() {
  $("ul.tab-bar > li").click(function() {
    $(this).siblings('.tab-active').removeClass('tab-active');
    $(this).addClass('tab-active');
  });

    var top = $('.menu-float').offset().top - parseFloat($('.menu-float').css('marginTop').replace(/auto/, 100));

    $(window).scroll(function (event) {
        // what the y position of the scroll is
        // whether that's below the form
        if ($(this).scrollTop() >= top) {
          $('.menu-float').addClass('fixed');
        } else {
          $('.menu-float').removeClass('fixed');
        }
    });
});

