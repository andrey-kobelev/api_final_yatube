from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from posts.models import Comment, Post, Group, Follow, User


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment
        read_only_fields = ('post',)


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        required=False, slug_field='username', read_only=True
    )
    following = serializers.SlugRelatedField(
        required=True, slug_field='username', queryset=User.objects.all()
    )

    class Meta:
        fields = '__all__'
        model = Follow

    def validate(self, data):
        following = data['following']
        user = self.context['request'].user
        user_followings = user.follower.all()
        if user == following:
            raise serializers.ValidationError(
                'Пользователь не может подписаться сам на себя!'
            )
        if user_followings.filter(following=following).exists():
            raise serializers.ValidationError(
                f'Вы уже подписаны на {following}!'
            )
        return data
