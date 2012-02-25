$(document).ready(function() {
    $("#course-list").hide();
    $("#course-button a").toggle(function(e) {
        $("#course-list").slideDown("normal");
        e.preventDefault();
    },
    function(e) {
        $("#course-list").slideUp("normal");
        e.preventDefault();
    })
});