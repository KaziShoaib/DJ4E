import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Site, Category, States, Region, Iso


def run():
    fhand = open('unesco/whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Site.objects.all().delete()
    Category.objects.all().delete()
    States.objects.all().delete()
    Region.objects.all().delete()
    Iso.objects.all().delete()


    for row in reader:
        print(row)

        c, created = Category.objects.get_or_create(name=row[7])
        s, created = States.objects.get_or_create(name=row[8])
        r, created = Region.objects.get_or_create(name=row[9])
        #iso_flag = True
        """
        if row[10] == '':
            iso_flag = False
        else:
            i, created = Iso.objects.get_or_create(name=row[10])
        """
        i, created = Iso.objects.get_or_create(name=row[10])
        n = row[0]
        d = row[1]
        j = row[2]
        try:
            y = int(row[3])
        except:
            y = None
        long = float(row[4])
        lat = float(row[5])
        try:
            a = float(row[6])
        except:
            a = None

        #name,description,justification,year,longitude,latitude,
        #area_hectares,category,states,region,iso
        """
        if iso_flag is True:
            site = Site(name = n, description = d, justification = j, year = y, longitude = long, latitude = lat, area_hectares = a, category = c, states = s, region = r, iso = i)
        else:
            site = Site(name = n, description = d, justification = j, year = y, longitude = long, latitude = lat, area_hectares = a, category = c, states = s, region = r)
        """
        site = Site(name = n, description = d, justification = j, year = y, longitude = long, latitude = lat, area_hectares = a, category = c, states = s, region = r, iso = i)
        site.save()