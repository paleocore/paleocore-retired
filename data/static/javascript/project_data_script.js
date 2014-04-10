$(document).ready(function() {
    var search_data_table = $('#search_data_table');

    var input = $('#search_box');
    input.jqxInput({placeHolder: 'Enter Search', height: 25, width: 200, minLength: 1});

    var button = $('#search_box_button');
    button.jqxButton({width: 45});
    button.click(function() {
        var val = input.val;
        var csrftoken = $.cookie('csrftoken');

        var url = window.location.href;
        var beginning_project_name_index = url.indexOf('/data/')+6;
        var end_project_name_index = url.indexOf('/', beginning_project_name_index);
        var project_name = url.substring(beginning_project_name_index, end_project_name_index);
        $.ajax({
            type:'POST',
            url: '/data/' + project_name,
            contentType: 'application/x-www-form-urlencoded',
            data: {
                'csrf_token': csrftoken,
                'post_action': 'search_box_query',
                'query': val
            },
            success: function(data) {
                var data_inside = data.substring(data.indexOf('>') + 1, data.lastIndexOf('<'));
                search_data_table.html(data_inside);
            }
        });
    });
});