$(document).ready(function() {
    // fix width of account button to be the same as the dropdown
    var accBut = $('#account_button');
    var dropdown = $('#account_dropdown');
    if (accBut && dropdown) {
        if (accBut.width() + 20 > dropdown.width())
            dropdown.css('width', accBut.width() + 20);
        else
            accBut.css('width', dropdown.width() - 20);
    }

    // login dialog box
    $(function() {
        var login_dialog = $('#login_dialog_box');
        login_dialog.dialog({
            autoOpen: false,
            width: 350,
            resizable: false,
            modal: true
        });
        
        var login_submit = $('#login_dialog_submit_button');
        login_submit.jqxButton();
        login_submit.click(function(e) {
            var valid_login = false;
            $.ajax({
                type:'GET',
                async: false,
                url: '/account/login/',
                contentType: 'application/x-www-form-urlencoded',
                data: {
                    'get_action': 'check_valid_login',
                    'email': login_dialog.find('#id_email').val(),
                    'password': login_dialog.find('#id_password').val()
                },
                success: function(data) {
                    valid_login = data.is_valid;
                }
            });
            if (!valid_login) {
                login_dialog.find('.error').css('display', 'block');
                e.preventDefault();
            }
        });
        
        var login_cancel = $('#login_dialog_cancel_button');
        login_cancel.jqxButton();
        login_cancel.click(function(e) {
            e.preventDefault();
            login_dialog.dialog( 'close' );
        });

        $( '#login_button' ).click(function() {
            login_dialog.dialog( 'open' );
        });
    });

    // signup dialog box
    $(function() {
        var signup_dialog = $('#signup_dialog_box');
        var signup_dialog_form = $('#signup_dialog_form');
        var signup_is_validated = false;
        signup_dialog.dialog({
            autoOpen: false,
            width: 350,
            resizable: false,
            modal: true
        });

        $( '#signup_button' ).click(function() {
            signup_dialog.dialog( 'open' );
            signup_dialog_form.jqxValidator('hide');
        });

        var signup_submit = $('#signup_dialog_submit_button');
        signup_submit.jqxButton();
        signup_submit.click(function(e) {
            signup_dialog_form.jqxValidator('validate');
            if (!signup_is_validated)
                e.preventDefault();
        });

        var signup_cancel = $('#signup_dialog_cancel_button');
        signup_cancel.jqxButton();
        signup_cancel.click(function(e) {
            e.preventDefault();
            signup_dialog.dialog( 'close' );
            signup_dialog_form.jqxValidator('hide');
        });

        signup_dialog_form.jqxValidator({
            focus: false,
            rules: [
                { input: '#signup_dialog_form #id_email', message: 'Your E-mail is required', action: 'keyup, blur', rule: 'required' },
                { input: '#signup_dialog_form #id_email', message: 'Invalid e-mail address', action: 'keyup', rule: 'email' },
                {
                    input: '#signup_dialog_form #id_email', message: 'An account is already associated with this email address',
                        action: 'keyup', rule: function (input) {
                            var result = false;
                            $.ajax({
                                type:'GET',
                                async: false,
                                url: '/account/signup/',
                                contentType: 'application/x-www-form-urlencoded',
                                data: {
                                    'get_action': 'is_email_unique',
                                    'email_in_question': input.val().trim()
                                },
                                success: function(data) {
                                    result = data.is_unique;
                                }
                            });
                            return result;
                        }
                },
                { input: '#signup_dialog_form #id_first_name', message: 'Your first name is required', action: 'keyup, blur', rule: 'required' },
                { input: '#signup_dialog_form #id_first_name', message: 'Your first name must contain only letters', action: 'keyup', rule: 'notNumber' },
                { input: '#signup_dialog_form #id_last_name', message: 'Your last name is required', action: 'keyup, blur', rule: 'required' },
                { input: '#signup_dialog_form #id_last_name', message: 'Your last name must contain only letters', action: 'keyup', rule: 'notNumber' },
                { input: '#signup_dialog_form #id_password1', message: 'Password is required', action: 'keyup, blur', rule: 'required' },
                { input: '#signup_dialog_form #id_password1', message: 'Your password must be between 8 and 30 characters', action: 'keyup, blur', rule: 'length=8,30' },
                { input: '#signup_dialog_form #id_password2', message: 'Password is required', action: 'keyup, blur', rule: 'required' },
                {
                    input: '#signup_dialog_form #id_password2', message: 'Passwords don\'t match',
                        action: 'keyup, focus', rule: function (input) {
                            // call commit with false, when you are doing server validation
                            // and you want to display a validation error on this field.
                            return input.val() === signup_dialog_form.find('#id_password1').val();
                        }
                }
            ],
            onError: function() {signup_is_validated = false;},
            onSuccess: function() {signup_is_validated = true;}
        });
    });

    // accounts dropdown menu
    $(function() {
        var acc = $('#account_button_dropdown');
        if (acc) {
            var dropdown = $('#account_dropdown');

            acc.mouseenter(function() {
                dropdown.slideDown(200);
            });

            acc.mouseleave(function() {
                dropdown.css('display', 'none');
            });
        }
    });

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        crossDomain: false, // obviates need for sameOrigin test
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type)) {
                var csrftoken = $.cookie('csrftoken');
                xhr.setRequestHeader('X-CSRFToken', csrftoken);
            }
        }
    });
});