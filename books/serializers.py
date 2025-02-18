from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):

    title = serializers.CharField(
        max_length=255,
        required=True
        )
    
    author = serializers.CharField(
        max_length=255,
        required=True
        # error_messages={
        #     "blank": "Author name cannot be empty.",
        #     "max_length": "Author cannot exceed 255 characters.",
        #     "required": "Author is required."
        # }
    )

    isbn = serializers.CharField(
        max_length=13,
        required=True
    )

    class Meta:
        model = Book
        fields = ['id','title', 'author', 'description', 'published_date', 'isbn', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

    def create(self, validated_data):
        """
        Create and return a new 'Book' instance, given the validated data.
        """
        return Book.objects.create(**validated_data)
    
    def update(self, instance, validate_data):
        """
        Update and return and existing 'Book' instance, given the validated data.
        """

        instance.title = validate_data.get('title', instance.title)
        instance.author = validate_data.get('author', instance.author)
        instance.description = validate_data.get('description', instance.description)
        instance.published_date = validate_data.get('published_date', instance.published_date)
        instance.isbn = validate_data.get('isbn', instance.isbn)

        instance.save()
        return instance

    
