function setFooterStyle() {
    var docHeight = $(window).height();
    var footerHeight = $('#footer').outerHeight();
    var footerTop = $('#footer').position().top + footerHeight;
    if (footerTop < docHeight) {
        $('#footer').css('margin-top', (docHeight - footerTop) + 'px');
    } else {
        $('#footer').css('margin-top', '');
    }
    $('#footer').removeClass('invisible');
}

function setInitialLanguage() {
    if (navigator.language.startsWith('es') || navigator.language.startsWith('ca')) {
        setLanguage('cat');
        //$('.lang-cat').removeClass('hidden');
        //$('.lang-eng').addClass('hidden');
    }
}

function setLanguage(language) {
    all_languages = ['cat', 'eng'];
    all_languages.forEach(function(element) {
         if (element != language) {
             $('.lang-'+element).addClass('hidden');
         } 
    });
    $('.lang-'+language).removeClass('hidden');
}

function hideChicagoSection(section) {
    $('.chicago-'+section+'-original').removeClass('hidden');
    $('.chicago-'+section).addClass('hidden');
}

function showChicagoSection(section) {
    $('.chicago-'+section+'-original').addClass('hidden');
    $('.chicago-'+section).removeClass('hidden');
}
