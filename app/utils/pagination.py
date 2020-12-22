from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from django.conf import settings


class CustomPagination(PageNumberPagination):
    page_size = settings.REST_FRAMEWORK["PAGE_SIZE"]
    page_size_query_param = "per_page"
    max_page_size = 2500

    def get_paginated_response(self, data):
        return Response(
            {
                "links": {
                    "next": self.get_next_link(),
                    "previous": self.get_previous_link(),
                },
                "count": self.page.paginator.count,
                "per_page": self.page.paginator.per_page,
                "total_pages": self.page.paginator.num_pages,
                "results": data,
            }
        )


class CustomLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 10


class CustomPageNumberPagination(PageNumberPagination):
    page_size = 2
