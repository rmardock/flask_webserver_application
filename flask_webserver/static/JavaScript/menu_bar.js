/* JavaScript file for menu bar */

$(function() {
    // Hide menu bar on page load
    $("#menu_wrapper").hide();
    // When menu button is clicked
    $(".menu_button_wrapper").click(function() {
        // If menu is collapsed
        if($(".menu_button_wrapper").hasClass("collapsed")) {
            // Change class of divs for CSS transition
            $(".bar1").addClass("change");
            $(".bar2").addClass("change");
            $(".bar3").addClass("change");
            // Change wrapper class
            $(".menu_button_wrapper").removeClass("collapsed");
            $(".menu_button_wrapper").addClass("expanded");
            // Code to open menu
            $("#collapsedmenu_button_wrapper").hide();
            $("div.services_wrapper").hide();
            $("#headerWrapper").hide();
            $("#menu_wrapper").animate({width: "toggle"});
            return;
        }
        // If menu is expanded
        if($(".menu_button_wrapper").hasClass("expanded")) {
            // Change class of divs for CSS transition
            $(".bar1").removeClass("change");
            $(".bar2").removeClass("change");
            $(".bar3").removeClass("change");
            // Change wrapper class
            $(".menu_button_wrapper").removeClass("expanded");
            $(".menu_button_wrapper").addClass("collapsed");
            // Code to close menu
            $("#menu_wrapper").animate({width: "toggle"});
            $("div.services_wrapper").show(450);
            $("#headerWrapper").show(450);
            $("#collapsedmenu_button_wrapper").show(450);
            return;
        }
    });
});