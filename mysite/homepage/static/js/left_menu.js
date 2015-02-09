/**
 * Created by mhelvey on 2/9/15.
 */
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