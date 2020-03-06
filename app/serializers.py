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

    posts = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'title', 'posts']

    def create(self, validated_data):
        title = validated_data['title']
        if not Category.objects.filter(title=title).exists():
            slug = Category.get_slug_by_name(title)
            return Category.objects.create(slug=slug, **validated_data)
        else:
            if Post.objects.filter(category__title=title).exists():
                validated_data['posts'] = Post.objects.filter(category__title=title)
            else:
                validated_data['posts'] = None
            return Category.objects.get(title=title)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        if 'slug' not in validated_data or not validated_data['slug']:
            validated_data['slug'] = Category.get_slug_by_name(validated_data['title'])
        instance.slug = validated_data.get('slug', instance.slug)
        instance.save()
        return instance

class CategorySerializerField(serializers.PrimaryKeyRelatedField):

    def display_value(self, instance):
        return instance.title

class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(required=True)
    category = CategorySerializerField(queryset=Category.objects.all(), required=False)

    class Meta:
        model = Post
        fields = '__all__'

    def validatation(self, validated_data):
        if 'author' in validated_data:
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
        if 'category' in validated_data:
            validated_data['category'] = Category.objects.filter(title=validated_data['category'])[0]
        else:
            validated_data['category'] = None

        if 'slug' not in validated_data or not validated_data['slug']:
            validated_data['slug'] = Category.get_slug_by_name(validated_data['title'])

        return validated_data

    def create(self, validated_data):
        validated_data = self.validatation(validated_data)
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        validated_data = self.validatation(validated_data)
        instance.author = validated_data.get('author', instance.author)
        instance.category = validated_data.get('category', instance.category)
        instance.title = validated_data.get('title', instance.title)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.status = validated_data.get('status', instance.status)
        instance.content = validated_data.get('content', instance.content)
        instance.updated = validated_data.get('updated', instance.updated)
        instance.publication_date = validated_data.get('publication_date', instance.publication_date)
        instance.save()
        return instance
