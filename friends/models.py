from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio= models.TextField(blank=True)
    profile_img = models.ImageField(upload_to='profile_img', default='images.png')
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return str(self.user)


    def __str__(self):  
        return self.user.username

class Share(models.Model):
    title = models.CharField(max_length=256)
    subtitle = models.CharField(max_length=256)
    body= models.TextField()
    image = models.ImageField(blank=True, null=True, upload_to="image/")
    created_on= models.DateTimeField(auto_now_add=True)
    likes =models.ManyToManyField(User, related_name="share_likes")
    author =models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_on']        

    def get_absolute_url(self):
        return reverse("share_list")

# Create your models here.
    # def get_absolute_url(self):
    #     return reverse("share_list", args=[self.id])