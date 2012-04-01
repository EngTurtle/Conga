$(document).ready(function () {
    $("#course-list").hide();
    $("#course-button a").toggle(function (e) {
        $("#course-list").slideDown("normal");
        $("#course-button").addClass("selected");
        Shadow.add("#content");
        e.preventDefault();
    }, function (e) {
        $("#course-list").slideUp("normal");
        $("#course-button").removeClass("selected");
        e.preventDefault();
        Shadow.remove();
    });
    // $("#filter").focus();
});

Shadow = {
    id: "es-c-shadow",
    add : function(q) {
        var shadow = document.createElement("div");
        shadow.id = this.id;
        shadow.className = "shadow-white";
        $(shadow).appendTo(q).hide().fadeIn("fast");
    },
    remove: function() {
        $("#"+ this.id).fadeOut("fast",function(){$(this).remove()});
    }
}