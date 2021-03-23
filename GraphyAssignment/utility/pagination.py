from rest_framework.pagination import LimitOffsetPagination


class BaseLimitOffsetPagination(LimitOffsetPagination):
    max_limit = 50
