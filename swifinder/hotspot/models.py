from django.db import models

# Create your models here.

# class ImageModel(models.Model):
#     model_pic = models.ImageField(upload_to = 'map_layouts/', deafult = 'map_layouts/None/no-img.jpg')
#

#t = Layout(layout_title="apartment1", layout_owner="zach", layout_size_x=650, layout_size_y=330)

class Layout(models.Model):
    layout_title = models.CharField(max_length=50)
    layout_owner = models.CharField(max_length=50)
    layout_image = models.FileField(upload_to='layouts/')

    def __str__(self):
        return "%s - %s" % (self.layout_title, self.layout_owner)
        #eventually foreign key to user

class Datapoints(models.Model):
    #left to right, top to bottom of grid
    grid_point = models.IntegerField()
    layout_x = models.IntegerField()
    layout_y = models.IntegerField()
    rssi = models.IntegerField()
    layout = models.ForeignKey(Layout, on_delete=models.CASCADE)

    def __str__(self):
        return "%s at %s" % (self.layout, self.grid_point)
