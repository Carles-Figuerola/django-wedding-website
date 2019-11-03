/*!
 * Start Bootstrap - Creative Bootstrap Theme (http://startbootstrap.com)
 * Code licensed under the Apache License v2.0.
 * For details, see http://www.apache.org/licenses/LICENSE-2.0.
 */

(function($) {
    "use strict"; // Start of use strict

    // jQuery for page scrolling feature - requires jQuery Easing plugin
    $('a.page-scroll').bind('click', function(event) {
        var $anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: ($($anchor.attr('href')).offset().top - 50)
        }, 1250, 'easeInOutExpo');
        window.history.pushState({}, document.title, $anchor.attr('href'));
        event.preventDefault();
    });

    // jQuery to change language from english <-> catalan
    $('a.enable-english').bind('click', function(event) {
        $('.language-english').removeClass("hidden");
        $('.language-catalan').addClass("hidden");
    });
    $('a.enable-catalan').bind('click', function(event) {
        $('.language-english').removeClass("hidden");
        $('.language-catalan').addClass("hidden");
    });
    $('a.enable-catalan').bind('click', function(event) {
        $('.language-catalan').removeClass("hidden");
        $('.language-english').addClass("hidden");
    });

    // Highlight the top nav as scrolling occurs
    // (specifically turns the links orange)
    $('body').scrollspy({
        target: '.navbar-fixed-top',
        offset: 51
    })

    // Closes the Responsive Menu on Menu Item Click
    $('.navbar-collapse ul li a').click(function() {
        $('.navbar-toggle:visible').click();
    });

    // Fit Text Plugin for Main Header
    $("h1").fitText(
        1.2, {
            minFontSize: '35px',
            maxFontSize: '65px'
        }
    );

    // Offset for Main Navigation - this turns the nav bar white
    $('#mainNav').affix({
        offset: {
            top: 100
        }
    })


})(jQuery); // End of use strict
