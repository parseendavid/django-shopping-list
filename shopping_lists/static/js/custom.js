$(document).ready(function () {
    $(".alien-modal-trigger").click(function (ev) { // for each edit contact url
        ev.preventDefault(); // prevent navigation
        var action = $(this).data("action");
        var form_id = $(this).data("form_id");
        var modal_id = $(this).data("modal_id");
        $(modal_id).load(action, function () {
            // load the url into the modal
            $(modal_id).modal('toggle');
            $(form_id).attr("action", action)
        });
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
