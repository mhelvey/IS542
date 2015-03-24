/**
 * Created by mhelvey on 3/3/15.
 */

$(function(){
    $('#id_uploadfile').off('change.uploader').on('change.uploader', function(){
        var fd = new FormData();
        var file = this.files[0];
        progressbar = $('.progress-bar');
        bar_width = 0;
        fd.append("uploadfile", file);
        $.ajax({
            url: '/homepage/uploader_upload',
            type: 'POST',
            contentType: false, //$ needs to leave the content type alone
            processData: false,
            data: fd,
            xhr: function() {
                var xhr = jQuery.ajaxSettings.xhr();
                if (xhr.upload) {
                    xhr.upload.addEventListener('progress', function(evt) {
                        if (evt.lengthComputable) {
                            //update the WUI
                            bar_width = ((evt.loaded/evt.totalSize) * 100);
                            progressbar.width(bar_width + '%');
                            console.log(evt);
                        }//if
                    }, false);//addEventListened
                }//if
                return xhr;
            },//xhr
            success: function(data) {
                //save the name to be uploaded with the main form
                $('#id_upload_fullname').val(data);
                console.log("Success");
                console.log(data);
            },//success
            error: function(err) {
                console.log("Error");
                console.log(err);
            }
        });//ajax

    });//change

    $('#id_uploadfile').closest('form').off('submit.uploader').on('submit.uploader', function(){
        $('#id_uploadfile').remove();
    }); //submit
});//ready