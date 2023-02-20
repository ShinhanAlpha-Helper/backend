from rest_framework import pagination

class NewsPagination(pagination.PageNumberPagination):
    # pass라고 두면 pagination 기본값으로 설정됨
    page_size = 50
