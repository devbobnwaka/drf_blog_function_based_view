from rest_framework import serializers

from .models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)
    class Meta:
        model = BlogPost
        fields = (
            'user', 
            'title', 
            'blog_content',
        )

    # def create(self, validated_data):
    #     print('create')
    #     user = None
    #     request = self.context.get("request")
    #     user = request.user
    #     blog_post = BlogPost.objects.create(user=user, **validated_data)
    #     return blog_post