from django.db.models import Q, Count
from django.shortcuts import render, get_object_or_404
from advert.models import Ads, Category, State ,Offer,Lga



def is_valid_queryparam(param):
    return param != '' and param is not None


def filter(request):
    qs = Ads.objects.all()
    categories = Category.objects.all().count()
    states = State.objects.all().count()
    offers = Offer.objects.all()
    title_contains_query = request.GET.get('title_contains')
    title_or_author_query = request.GET.get('title_or_author')
    ad_price_min = request.GET.get('ad_price_min')
    ad_price_max = request.GET.get('ad_price_max')
    ad_area_min = request.GET.get('ad_area_min')
    ad_area_max = request.GET.get('ad_area_max')
    date_min = request.GET.get('date_min')
    date_max = request.GET.get('date_max')
    category = request.GET.get('category')
    state = request.GET.get('state')
    ad_offer = request.GET.get('ad_offer')
    reviewed = request.GET.get('reviewed')
    condition = request.GET.get('condition')
    building_age = request.GET.get('building_age')
    rent_period = request.GET.get('rent_period')
    ad_room = request.GET.get('ad_room')
    bedroom = request.GET.get('bedroom')
    bathroom= request.GET.get('bathroom')
    lot_size_min = request.GER.get('lot_size_min')
    lot_size_max = request.GER.get('lot_size_min')
    church = request.GET.get('church')
    school = request.GET.get('school ')
    mosque = request.GET.get('mosque')
    beach = request.GET.get('beach')
    market = request.GET.get('market')
    hospital = request.GET.get('hospital')
    resturant = request.GET.get('resturant')
    air_conditioning = request.GET.get('air_conditioning')
    parking = request.GET.get('parking')
    sewer = request.GET.get('sewer')
    water = request.GET.get('water')
    lawn = request.GET.get('lawn')
    swimming_pool = request.GET.get('swimming_pool')
    barbecue = request.GET.get('barbecue')
    tv_cable = request.GET.get('tv_cable')
    microwave = request.GET.get('microwave')
    wi_fi = request.GET.get('wi_fi')
    gym = request.GET.get('gem')

    if is_valid_queryparam(title_contains_query):
        qs = qs.filter(Q(title__icontains=title_or_author_query)
                       | Q(author__name__icontains=title_or_author_query)
                       ).distinct()

    if is_valid_queryparam(ad_price_min):
        qs = qs.filter(property_price__gte=ad_price_min)

    if is_valid_queryparam(ad_price_max):
        qs = qs.filter(property_price__lt=ad_price_max)


    if is_valid_queryparam(ad_area_min):
        qs = qs.filter(property_area__gte=ad_area_min)

    if is_valid_queryparam(ad_area_max):
        qs = qs.filter(property_area__lt=ad_area_max)

    if is_valid_queryparam(date_min):
        qs = qs.filter(publish_date__gte=date_min)

    if is_valid_queryparam(date_max):
        qs = qs.filter(publish_date__lt=date_max)

    if is_valid_queryparam(category) and category != 'Choose...':
        qs = qs.filter(category__name=category)

    if is_valid_queryparam(state) and state != 'Choose...':
        qs = qs.filter(state__name=state)

    if is_valid_queryparam(ad_offer) and state != 'Choose...':
        qs = qs.filter(property_offer__name=ad_offer)

    if is_valid_queryparam(condition) and condition != 'Choose...':
        qs = qs.filter(condition=condition)

    if is_valid_queryparam(building_age) and building_age != 'Choose...':
        qs = qs.filter(building_age=building_age)

    if is_valid_queryparam(rent_period) and rent_period != 'Choose...':
        qs = qs.filter(rent_period=rent_period)

    if is_valid_queryparam(ad_room) and ad_room != 'Choose...':
        qs = qs.filter(property_room=ad_room)

    if is_valid_queryparam(bedroom) and bedroom != 'Choose...':
        qs = qs.filter(bedroom=bedroom)

    if is_valid_queryparam(bathroom) and bathroom != 'Choose...':
        qs = qs.filter(bathroom=bathroom)

    if is_valid_queryparam(lot_size_min):
        qs = qs.filter(lot_size_min__gte=lot_size_min)

    if is_valid_queryparam(lot_size_max):
        qs = qs.filter(lot_size_max__lt=lot_size_max)

    if reviewed == 'on':
        qs = qs.filter(reviewed=True)

    if church == 'on':
        qs = qs.filter(church=True)

    if school == 'on':
        qs = qs.filter(school=True)

    if mosque == 'on':
        qs = qs.filter(mosque=True)

    if beach == 'on':
        qs = qs.filter(beach=True)

    if market == 'on':
        qs = qs.filter(market=True)

    if hospital == 'on':
        qs = qs.filter(hospital=True)

    if resturant == 'on':
        qs = qs.filter(resturant=True)

    if air_conditioning == 'on':
        qs = qs.filter(air_conditioning=True)

    if parking == 'on':
        qs = qs.filter(parking=True)

    if sewer == 'on':
        qs = qs.filter(sewer=True)

    if water == 'on':
        qs = qs.filter(water=True)

    if lawn == 'on':
        qs = qs.filter(lawn=True)

    if swimming_pool == 'on':
        qs = qs.filter(swimming_pool=True)

    if barbecue == 'on':
        qs = qs.filter(barbecue=True)

    if tv_cable == 'on':
        qs = qs.filter(tv_cable=True)

    if microwave == 'on':
        qs = qs.filter(microwave=True)

    if wi_fi == 'on':
        qs = qs.filter(wi_fi=True)

    if gym == 'on':
        qs = qs.filter(gym=True)

    # elif not_reviewed == 'on':
    #     qs = qs.filter(reviewed=False)

    context = {
        'queryset': qs,
        'categories': categories,
        'states':states,
        'offers':offers
    }
    return render(request, "search/other_search.html", context)


