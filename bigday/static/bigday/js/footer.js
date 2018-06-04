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

function hideChicagoSection(section, language) {
    $('.chicago-'+section+'-'+language+'-original').removeClass('hidden');
    $('.chicago-'+section+'-'+language).addClass('hidden');
}

function showChicagoSection(section, language) {
    $('.chicago-'+section+'-'+language+'-original').addClass('hidden');
    $('.chicago-'+section+'-'+language).removeClass('hidden');
}

function noRSVPYet(language){
    }
