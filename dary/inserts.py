from dary.models import Category, Institution, Donation


def add_category():
    c1 = Category.objects.create(name='zabawki')
    c2 = Category.objects.create(name='ubrania')
    c3 = Category.objects.create(name='meble')
    c4 = Category.objects.create(name='AGD')
    c5 = Category.objects.create(name='inne')

def add_institution():
    # c1 = Category.objects.get(name='zabawki')
    # c2 = Category.objects.get(name='ubrania')
    # c3 = Category.objects.get(name='meble')
    # c4 = Category.objects.get(name='AGD')
    # c5 = Category.objects.get(name='inne')
    i1 = Institution.objects.create(name='AAA', description='opis1', type='fundacja')
    i2 = Institution.objects.create(name='BBB', description='opis2', type='organizacja pozarządowa')
    i3 = Institution.objects.create(name='CCC', description='opis3', type='zbiórka lokalna')
    i4 = Institution.objects.create(name='DDD', description='opis4', type='organizacja pozarządowa')
    i5 = Institution.objects.create(name='EEE', description='opis1', type='fundacja')

def add_donation():

    i1 = Institution.objects.get(name='AAA')
    i2 = Institution.objects.get(name='BBB')
    i3 = Institution.objects.get(name='CCC')
    i4 = Institution.objects.get(name='DDD')
    i5 = Institution.objects.get(name='EEE')


    d1 = Donation.objects.create(quantity=20, institution=i2, adress='Ludna 7', phone_number=606754445, city='Warszawa',zip_code='00950', pick_up_comment='comment_1')

    d2 = Donation.objects.create(quantity=2, institution=i1, adress='Ludna 8', phone_number=606754443,
                                 city='Warszawa', zip_code='00950', pick_up_comment = 'comment_2')
    d3 = Donation.objects.create(quantity=9, institution=i3, adress='Ludna 12', phone_number=606734443,
                                 city='Warszawa', zip_code='00950', pick_up_comment = 'comment_3')
    d4 = Donation.objects.create(quantity=12, institution=i2, adress='Ludna 3', phone_number=606724443,
                                 city='Warszawa', zip_code='00950', pick_up_comment = 'comment_4')
    d5 = Donation.objects.create(quantity=4, institution=i3, adress='Ludna 10',phone_number=606724445,
                                 city='Warszawa',zip_code='00950', pick_up_comment='comment_5')
    d6 = Donation.objects.create(quantity=16, institution=i4, adress='Ludna 11', phone_number=606254443,
                                 city='Warszawa', zip_code='00950', pick_up_comment = 'comment_6')
    d7 = Donation.objects.create(quantity=30, institution=i2, adress='Ludna 1', phone_number=603734443,
                                 city='Warszawa', zip_code='00950', pick_up_comment = 'comment_7')
    d8 = Donation.objects.create(quantity=12, institution=i2, adress='Ludna 3', phone_number=604724443,
                                 city='Warszawa', zip_code='00950', pick_up_comment = 'comment_8')
    d9 = Donation.objects.create(quantity=7, institution=i5, adress='Ludna 34', phone_number=605724443,
                                 city='Warszawa', zip_code='00950', pick_up_comment = 'comment_9')

# add_category()
# add_institution()
# add_donation()