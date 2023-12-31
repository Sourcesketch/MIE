$(function() {

    'use strict';

    // Form

    var contactForm = function() {

        if ($('#contactForm').length > 0) {
            $("#contactForm").validate({
                rules: {
                    name: "required",
                    email: {
                        required: true,
                        email: true
                    },
                    phone: "required"



                },
                messages: {
                    name: "Please enter your name",
                    email: "Please enter a valid email address",
                    phone: "Please enter a valid phone number"

                },
                /* submit via ajax */
                submitHandler: function(form) {
                    var $submit = $('.submitting'),
                        waitText = 'Submitting...';

                    $.ajax({
                        type: "POST",
                        url: "http://127.0.0.1:5000/send_email",
                        data: $(form).serialize(),

                        beforeSend: function() {
                            $submit.css('display', 'block').text(waitText);
                        },
                        success: function(msg) {
                            if (msg == 'OK') {
                                $('#form-message-warning').hide();
                                setTimeout(function() {
                                    $('#contactForm').fadeOut();
                                }, 1000);
                                setTimeout(function() {
                                    $('#form-message-success').fadeIn();
                                }, 1400);

                            } else {
                                $('#form-message-warning').html(msg);
                                $('#form-message-warning').fadeIn();
                                $submit.css('display', 'none');
                            }
                        },
                        error: function() {
                            $('#form-message-warning').html("Something went wrong. Please try again.");
                            $('#form-message-warning').fadeIn();
                            $submit.css('display', 'none');
                        }
                    });
                }

            });
        }
    };
    contactForm();

});