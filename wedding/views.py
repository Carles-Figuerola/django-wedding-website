from django.conf import settings
from django.shortcuts import render
from guests.save_the_date import SAVE_THE_DATE_CONTEXT_MAP


def home(request):
    query_params = request.GET
    debug = False
    if 'debug' in query_params:
        if query_params['debug'].lower() == "true":
            debug = True
    mode = ""
    if 'mode' in query_params:
        mode = query_params['mode']
    return render(request, 'home.html', context={
        'save_the_dates': SAVE_THE_DATE_CONTEXT_MAP,
        'support_email': settings.DEFAULT_WEDDING_REPLY_EMAIL,
        'expedia_coupon': 'VENTUREOUT',
        'hcom_coupon': 'FNFQ118:AF5JU5',
        'hcom_coupon_url': 'https://www.hotels.com/',
        'debug': debug,
        'mode': mode
    })

def barcelona(request):
    query_params = request.GET
    debug = False
    if 'debug' in query_params:
        if query_params['debug'].lower() == "true":
            debug = True
    mode = ""
    if 'mode' in query_params:
        mode = query_params['mode']
    return render(request, 'barcelona.html', context={
        'save_the_dates': SAVE_THE_DATE_CONTEXT_MAP,
        'support_email': settings.DEFAULT_WEDDING_REPLY_EMAIL,
        'expedia_coupon': 'VENTUREOUT',
        'hcom_coupon': 'FNFQ118:AF5JU5',
        'hcom_coupon_url': 'https://www.hotels.com/',
        'debug': debug,
        'mode': mode
    })
