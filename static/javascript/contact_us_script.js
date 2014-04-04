$(document).ready(function () {
    var contact_submit = $('#contact_form_submit_button');
    contact_submit.jqxButton();
    contact_submit.click(function(e) {
        contact_form.jqxValidator('validate');
        e.preventDefault();
        if (contact_is_validated) {
            $.ajax({
                type:'POST',
                url: '/contact_us/',
                contentType: 'application/x-www-form-urlencoded',
                data: {
                    'post_action': 'submit_comment',
                    'name': contact_form.find('#name_input').val().trim(),
                    'email': contact_form.find('#email_input').val().trim(),
                    'comment': contact_form.find('#comment_input').val().trim()
                },
                success: function() {
                    contact_form.find('#success_message').css('display', 'block');
                    contact_form.find('#name_input').val('');
                    contact_form.find('#email_input').val('');
                    contact_form.find('#comment_input').val('');
                }
            });
        }
    });

    var contact_form = $('#contact_form');
    var contact_is_validated = false;

    contact_form.jqxValidator({
        rules: [
            { input: '#contact_form #name_input', message: 'Your name is required', action: 'keyup, blur', rule: 'required' },
            { input: '#contact_form #name_input', message: 'Your name must contain only letters', action: 'keyup', rule: 'notNumber' },
            { input: '#contact_form #email_input', message: 'Your E-mail is required', action: 'keyup, blur', rule: 'required' },
            { input: '#contact_form #email_input', message: 'Invalid e-mail address', action: 'keyup', rule: 'email' },
            { input: '#contact_form #comment_input', message: 'Comment is required', action: 'keyup, blur', rule: 'required' }
        ],
        onError: function() {contact_is_validated = false;},
        onSuccess: function() {contact_is_validated = true;}
    });
});