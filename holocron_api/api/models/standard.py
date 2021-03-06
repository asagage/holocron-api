from django.db import models
from django.db.models.signals import post_save
from django.template.defaultfilters import slugify
from Ad_Network import Ad_Network
from django_pandas.managers import DataFrameManager


class Program(models.Model):
    program_id = models.AutoField(primary_key=True)
    program_name = models.CharField(max_length=100, unique=True)
    program_description = models.CharField(max_length=140)
    created_by = models.CharField(max_length=100)
    program_notes = models.CharField(max_length=140, blank=True)
    start_date = models.DateField('Start Date', blank=True, null=True)
    end_date = models.DateField('End Date', blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.program_name


class Campaign(models.Model):
    campaign_id = models.AutoField(primary_key=True)
    campaign_name = models.CharField(max_length=100, unique=True)
    campaign_description = models.CharField(max_length=140)
    program = models.ForeignKey(Program, on_delete=models.PROTECT)
    created_by = models.CharField(max_length=100)
    campaign_notes = models.CharField(max_length=140, blank=True)
    start_date = models.DateField('Start Date', blank=True, null=True)
    end_date = models.DateField('End Date', blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.campaign_name


class Tactic(models.Model):
    tactic_id = models.AutoField(primary_key=True)
    tactic_key = models.CharField(max_length=100, blank=True, null=True,
                                  unique=True)
    tactic_name = models.CharField(max_length=100)
    tactic_description = models.CharField(max_length=140)
    campaign = models.ForeignKey(Campaign, default=1, on_delete=models.PROTECT)
    created_by = models.CharField(max_length=100)
    tactic_notes = models.CharField(max_length=140, blank=True)
    start_date = models.DateField('Start Date', blank=True, null=True)
    end_date = models.DateField('End Date', blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tactic_key


# method for updating the key to match the id if it is null/blank
def update_key(sender, *args, **kwargs):
    i = kwargs['instance']
    if i.tactic_key is None or i.tactic_key == "":
        i.tactic_key = i.tactic_id
        i.save()
    else:
        i2 = slugify(i.tactic_key)
        if i.tactic_key != i2:
            i.tactic_key = i2
            i.save()
        else:
            pass


# register the signal
post_save.connect(update_key, sender=Tactic)


class Medium(models.Model):
    medium_key = models.SlugField(max_length=100, primary_key=True)
    medium_name = models.CharField(max_length=100, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.medium_key


class Source(models.Model):
    source_key = models.SlugField(max_length=100, primary_key=True)
    source_name = models.CharField(max_length=100, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.source_key


class Creative(models.Model):
    creative_id = models.AutoField(primary_key=True)
    creative_name = models.CharField(max_length=100)
    creative_description = models.CharField(max_length=140)
    created_on = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.creative_name


class Placement(models.Model):
    placement_id = models.AutoField(primary_key=True)
    placement_name = models.CharField(max_length=100, unique=True)
    placement_url = models.CharField(max_length=250)
    placement_description = models.CharField(max_length=140, blank=True, null=True)
    tactic = models.ForeignKey(Tactic, on_delete=models.PROTECT)
    medium = models.ForeignKey(Medium, on_delete=models.PROTECT)
    source = models.ForeignKey(Source, on_delete=models.PROTECT)
    creative = models.ForeignKey(Creative, blank=True, null=True, on_delete=models.SET_NULL)
    catid = models.IntegerField(blank=True, null=True)
    page_cat = models.CharField(max_length=100, blank=True, null=True)
    page_id = models.CharField(max_length=100, blank=True, null=True)
    promo_uid = models.IntegerField(blank=True, null=True)
    ad_network = models.ForeignKey(Ad_Network, blank=True, null=True, on_delete=models.SET_NULL)
    jira_ticket = models.CharField(max_length=20, blank=True, default="")
    start_date = models.DateField('Start Date', blank=True, null=True)
    end_date = models.DateField('End Date', blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = DataFrameManager()

    def __str__(self):
        return str(self.placement_id)
