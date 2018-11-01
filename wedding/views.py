from django.conf import settings
from django.shortcuts import render
from guests.save_the_date import SAVE_THE_DATE_CONTEXT_MAP


def home(request):
    return render(request, 'home.html', context={
        'save_the_dates': SAVE_THE_DATE_CONTEXT_MAP,
        'support_email': settings.DEFAULT_WEDDING_REPLY_EMAIL,
        'expedia_coupon': 'VOYAGEOCT',
        'hcom_coupon': 'FNFQ118:AF5JU5',
        'hcom_coupon_url': 'https://www.hotels.com/?rffrid=eml.hcom.UK.300.00.2018.10.30.src00.00.00.0000.0000.00.0000.DD00.kwrd=MER.AQ.TYU.eml.0.0.ff_booknow'
    })
