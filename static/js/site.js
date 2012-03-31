$(document).ready(function () {
    $("#course-list").hide();
    $("#course-button a").toggle(function (e) {
        $("#course-list").slideDown("normal");
        $("#course-button").addClass("selected");
        e.preventDefault();
    }, function (e) {
        $("#course-list").slideUp("normal");
        $("#course-button").removeClass("selected");
        e.preventDefault();
    });
    // $("#filter").focus();
});