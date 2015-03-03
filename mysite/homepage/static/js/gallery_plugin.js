/**
 * Created by mhelvey on 3/3/15.
 */

(function ( $ ) {
    $.fn.gallery = function(options){

        options = $.extend(true, {
            option: 'value'
        }, options);

        $(this).hover(function(){
            $(this).children("img").toggleClass("rollover", 100);
            $(this).children("span").toggleClass("display-span");
        });

        //$(this).hover()
        //    .children("img").toggleClass("rollover", 100);
        //$(this).hover()
        //    .children("span").toggleClass("display-span");
        //
        return this;
    };
}( jQuery ));