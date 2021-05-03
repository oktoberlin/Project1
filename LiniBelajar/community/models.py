from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
from ckeditor.fields import RichTextField


class Post(models.Model):
    judul = models.CharField(max_length=100, blank=True)
    isi_konten = RichTextField(blank=True, null=True)
    upload_gambar = models.ImageField(upload_to='foto-post', blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.judul

    def get_absolute_url(self):
        return reverse('community:post-detail', kwargs={'pk': self.pk})

    # def upload_image(self, filename):
    #    return 'post/{}/{}'.format(self.title, filename)

    def post_save():
        super().post_save()

        img_post = Image.open(self.image.path)

        if img_post.height > 500 or img_post.width > 500:
            height = 500
            width = 500
            output_size = (height, width)
            img_post.thumbnail(output_size)
            img_post.post_save(self.upload_gambar.path)
