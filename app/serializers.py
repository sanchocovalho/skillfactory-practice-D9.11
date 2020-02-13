from .models import Post, Category, PostAuthor
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

class AuthorSerializer(serializers.ModelSerializer):  
    class Meta:
        model = PostAuthor
        fields = ['username', 'first_name', 'last_name']
        extra_kwargs = {
            'username': {'validators': []},
        }

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']

    def create(self, validated_data):
        if not Category.objects.filter(title=validated_data['title']).exists():
            slug = Category.get_slug_by_name(validated_data['title'])
            return Category.objects.create(slug=slug, **validated_data)
        else:
            return Category.objects.get(title=validated_data['title'])

class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(required=False)
    category = CategorySerializer(required=False)

    class Meta:
        model = Post
        fields = '__all__'

    def create(self, validated_data):
        author = validated_data.pop('author')
        if author['username']:
            if PostAuthor.objects.filter(username=author['username']).exists():
                validated_data['author'] = PostAuthor.objects.filter(username=author['username'])[0]
            else:
                validated_data['author'] = PostAuthor.objects.create_user(
                    username=author['username'],
                    first_name=author['first_name'],
                    last_name=author['last_name'],
                    password=author['username'].upper()
                    )

        category = validated_data.pop('category')
        if category['title']:
            if not Category.objects.filter(title=category['title']).exists():
                cat = {}
                cat['title'] = category['title']
                cat['slug'] = Category.get_slug_by_name(category['title'])
                Category.objects.create(**cat)
            validated_data['category'] = Category.objects.filter(title=category['title'])[0]
        else:
            validated_data['category'] = None

        if 'slug' not in validated_data or not validated_data['slug']:
            validated_data['slug'] = Category.get_slug_by_name(validated_data['title'])

        return Post.objects.create(**validated_data)
