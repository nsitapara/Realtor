from django.db import models

class ListOfCities(models.Model):
    city = models.TextField()
    def __str__(self):
        return f"{self.city}"


class HousingQueryData(models.Model):
    query_id = models.AutoField(primary_key=True)
    datetime = models.DateTimeField(auto_now_add=True)
    city = models.TextField(blank=True,null=True)
    total_records = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return f"{self.datetime} , {self.city} , {self.total_records}"

class HouseDataPoint(models.Model):
    link = models.ForeignKey(HousingQueryData, null=True, on_delete=models.SET_NULL)
    property_id = models.TextField(blank=True,null=True)
    listing_id = models.BigIntegerField(blank=True,null=True)
    rdc_web_url = models.TextField(blank=True,null=True)
    city = models.TextField(blank=True,null=True)
    line = models.TextField(blank=True,null=True)
    postal_code = models.TextField(blank=True,null=True)
    state_code  = models.TextField(blank=True,null=True)
    state = models.TextField(blank=True,null=True)
    county = models.TextField(blank=True,null=True)
    time_zone = models.TextField(blank=True,null=True)
    neighborhood_name = models.TextField(blank=True,null=True)
    prop_type = models.TextField(blank=True,null=True)
    prop_status = models.TextField(blank=True,null=True)
    price = models.IntegerField(blank=True,null=True)
    baths_full = models.IntegerField(blank=True,null=True)
    baths = models.FloatField(blank=True,null=True)
    beds = models.IntegerField(blank=True,null=True)
    size = models.IntegerField(blank=True,null=True)
    units = models.TextField(blank=True,null=True)
    agents = models.TextField(blank=True,null=True)
    office = models.TextField(blank=True,null=True)
    last_update = models.TextField(blank=True,null=True)
    client_display_flags = models.TextField(blank=True,null=True)
    lot_size = models.IntegerField(blank=True,null=True)
    lot_size_units = models.TextField(blank=True,null=True)
    mls = models.TextField(blank=True,null=True)
    data_source_name = models.TextField(blank=True,null=True)
    presentation_status = models.TextField(blank=True,null=True)
    price_change = models.IntegerField(blank=True,null=True)
    is_new_listing = models.TextField(blank=True,null=True)

    def __str__(self):
        return f"{self.line} , {self.city} , {self.state_code}"