from .models import Post, Category, PostAuthor
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from django.contrib import messages

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
        title = validated_data['title']
        if not Category.objects.filter(title=title).exists():
            slug = Category.get_slug_by_name(title)
            return Category.objects.create(slug=slug, **validated_data)
        else:
            return Category.objects.get(title=title)

class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(required=False)
    category = CategorySerializer(required=False)

    class Meta:
        model = Post
        fields = '__all__'

    def create(self, validated_data):
        author = validated_data.pop('author')
        username = author['username']
        if username:
            if PostAuthor.objects.filter(username=username).exists():
                validated_data['author'] = PostAuthor.objects.filter(username=username)[0]
            else:
                password = ''
                passkey = username
                if len(passkey) <= 8:
                    passkey += passkey
                for char in passkey:
                    if char in ['a','e','i','j','o','u','y']:
                        password += char.upper()
                    else:
                        password += char.lower()
                validated_data['author'] = PostAuthor.objects.create_user(
                    username=username,
                    first_name=author['first_name'],
                    last_name=author['last_name'],
                    password=password
                    )

        category = validated_data.pop('category')
        title = category['title']
        if title:
            if not Category.objects.filter(title=category['title']).exists():
                cat = {}
                cat['title'] = title
                cat['slug'] = Category.get_slug_by_name(title)
                Category.objects.create(**cat)
            validated_data['category'] = Category.objects.filter(title=title)[0]
        else:
            validated_data['category'] = None

        if 'slug' not in validated_data or not validated_data['slug']:
            validated_data['slug'] = Category.get_slug_by_name(validated_data['title'])

        return Post.objects.create(**validated_data)
