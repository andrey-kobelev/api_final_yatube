from rest_framework.exceptions import APIException


class FollowingExistsError(APIException):
    status_code = 400
    default_detail = ('Вы уже подписаны на '
                      'пользователя на которого хотите подписаться!')
    default_code = 'following_exists'


class FollowError(APIException):
    status_code = 400
    default_detail = 'Пользователь не может подписаться сам на себя!'
    default_code = 'follow_error'
