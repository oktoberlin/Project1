from rest_framework import serializers
from community.models import Post

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['judul', 'isi_konten', 'upload_gambar', 'date_posted', 'author', 'pk']