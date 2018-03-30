$(document).ready(function () {
    $(".alien-modal-trigger").click(function (ev) { // for each edit contact url
        ev.preventDefault(); // prevent navigation
        var url = $(this).data("form"); // get the contact form url
        console.log(url);

        $(document).bind('load_complete', set_action_attr);
        $(document).bind('load_start', load_modal);
        $(document).trigger("load_start");

        function load_modal() {
            $("#EditList").load(url, function () {
                // load the url into the modal
                $(this).modal('show'); // display the modal on url load
                $(document).trigger('load_complete');
            });
        }

        function set_action_attr() {
            $("#edit-form").attr("action", url);
        }

        return false; // prevent the click propagation
    });

    $('.alien-modal-submit').on('submit', function () {
        $.ajax({
            type: $(this).attr('method'),
            url: this.action,
            data: $(this).serialize(),
            context: this,
            success: function (data, status) {
                $('#EditList').html(data);
            }
        });
        return false;
    });
    window.setTimeout(function () {
        $(".alert").fadeTo(500, 0).slideUp(500, function () {
            $(this).remove();
        });
    }, 4000);
});
