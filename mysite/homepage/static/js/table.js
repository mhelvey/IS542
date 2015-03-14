/**
 * Created by mhelvey on 3/13/15.
 */
$(function(){
    var container = $('#table_container');

    // previous button click on table
    $('#prev_page_button').off('click.page').on('click_page', function(){
        var page = parseInt(container.data('page'));
        container.data('page', Math.max(0, page-1));
        container.trigger('table_refresh');
    }); //click

    // next button click on table
    $('#next_page_button').off('click.page').on('click_page', function(){
        var page = parseInt(container.data('page'));
        container.data('page', Math.max(0, page+1));
        container.trigger('table_refresh');
    }); //click

    // handler to refresh table
    container.on('table_refresh', function(){
        $.ajax({
            url: '/homepage/table.get_table/' + container.data('page')
        }).success(function(data) {
            container.html(data);
        });
    }).trigger('table_refresh');

});//ready