$(document).ready(function () {
    $(".alien-modal-trigger").click(function (ev) { // for each edit contact url
        ev.preventDefault(); // prevent navigation
        var action = $(this).data("action"); // get the contact form action url
        var form_id = $(this).data("form_id"); // get the contact fom id
        var modal_id = $(this).data("modal_id"); // get the contact fom id
        $(document).bind('load_complete', set_action_attr);
        $(document).bind('load_start', load_modal);
        $(document).trigger("load_start");

        function load_modal() {
            $(modal_id).load(action, function () {
                // load the url into the modal
                $(this).modal('show'); // display the modal on url load
                $(document).trigger('load_complete');
            });
        }

        function set_action_attr() {
            $(form_id).attr("action", action);
        }

        return false; // prevent the click propagation
    });

    $('.alien-modal-submit').on('submit', function () {
        $.ajax({
            type: $(this).attr('method'),
            url: this.action,
            data: $(this).serialize(),
            context: this,
        });
        return false;
    });
    window.setTimeout(function () {
        $(".alert").fadeTo(500, 0).slideUp(500, function () {
            $(this).remove();
        });
    }, 4000);
});
