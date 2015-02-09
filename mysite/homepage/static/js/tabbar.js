/**
 * Created by mhelvey on 2/6/15.
 */
   $(function() {
      $("ul.tab-bar > li").click(function() {
        $(this).siblings('.tab-active').removeClass('tab-active');
        $(this).addClass('tab-active');
      });
    });