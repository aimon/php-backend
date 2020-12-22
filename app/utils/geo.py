from django.db import models
from django.db.models.expressions import RawSQL


def get_locations_nearby_coords_func(queryset, latitude, longitude, max_distance=None):
    """
    Return objects sorted by distance to specified coordinates
    which distance is less than max_distance given in kilometers
    """
    # Great circle distance formula
    gcd_formula = "6371 * acos(least(greatest(\
    cos(radians(%s)) * cos(radians(latitude)) \
    * cos(radians(longitude) - radians(%s)) + \
    sin(radians(%s)) * sin(radians(latitude)) \
    , -1), 1))"
    distance_raw_sql = RawSQL(gcd_formula, (latitude, longitude, latitude))
    qs = queryset.all().annotate(distance=distance_raw_sql).order_by("distance")
    if max_distance is not None:
        qs = qs.filter(distance__lt=max_distance)

    return qs


get_locations_nearby_coords = get_locations_nearby_coords_func
