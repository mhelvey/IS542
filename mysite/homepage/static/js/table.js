/**
 * Created by mhelvey on 3/13/15.
 */
$(function(){
    var container = $('#table_container');
    console.log("function")
    // previous button click on table
    $('#prev_page_button').off('click.page').on('click.page', function(){
        var page = parseInt(container.data('page'));
        container.data('page', Math.max(0, page-1));
        container.trigger('table_refresh');
    }); //click

    // next button click on table
    $('#next_page_button').off('click.page').on('click.page', function(){
        var page = parseInt(container.data('page'));
        console.log("next");
        container.data('page', page+1);
        console.log(container.data('page'))
        container.trigger('table_refresh');
    }); //click

    // handler to refresh table
    container.on('table_refresh', function(){
        $.ajax({
            url: '/homepage/table/page/' + container.data('page'),
            context: container
        }).success(function(data) {
            //container.html(data);
            var html = '<table class="table table-bordered table-striped"><tr><th>First Name</th><th>Last Name</th><th>Email</th></tr>';
            console.log(data);
            $.each( data.users, function() {
                var row = '<tr>';
                row += '<td>' + this[0] + '</td>';
                row += '<td>' + this[1] + '</td>';
                row += '<td>' + this[2] + '</td>';
                row += '</tr>';
                html += row;
            });
            html += '</table>'
            this.html( html );
        });
        console.log('yo')
    }).trigger('table_refresh');

});//ready