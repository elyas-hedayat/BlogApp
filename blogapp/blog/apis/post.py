from drf_spectacular.utils import extend_schema
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView

from blogapp.api.mixins import ApiAuthMixin
from blogapp.api.pagination import LimitOffsetPagination, get_paginated_response_context
from blogapp.blog.models import Post
from blogapp.blog.selectors.post import post_detail, post_list
from blogapp.blog.services.post import post_create, post_update


class PostListApi(APIView):
    class Pagination(LimitOffsetPagination):
        default_limit = 10

    class FilterSerializer(serializers.Serializer):
        title = serializers.CharField(required=False, max_length=100)

    class OutPutSerializer(serializers.ModelSerializer):
        thumbnail_url = serializers.SerializerMethodField()

        class Meta:
            model = Post
            fields = (
                "pk",
                "title",
                "content",
                "thumbnail",
                "thumbnail_url",
                "created_at",
                "updated_at",
            )

        def get_thumbnail_url(self, obj):
            return obj.thumbnail.url if obj.thumbnail else ""

    @extend_schema(
        parameters=[FilterSerializer],
        responses=OutPutSerializer,
    )
    def get(self, request):
        filters_serializer = self.FilterSerializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)

        try:
            query = post_list(filters=filters_serializer.validated_data)
        except Exception as ex:
            return Response(
                {"detail": "Filter Error - " + str(ex)},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return get_paginated_response_context(
            pagination_class=self.Pagination,
            serializer_class=self.OutPutSerializer,
            queryset=query,
            request=request,
            view=self,
        )


class PostDetailApi(ApiAuthMixin, APIView):
    class OutPutDetailSerializer(serializers.ModelSerializer):
        class Meta:
            model = Post
            fields = ("pk", "title", "content", "created_at", "updated_at")

    @extend_schema(
        responses=OutPutDetailSerializer,
    )
    def get(self, request, pk):
        try:
            query = post_detail(pk=pk)
        except Exception as ex:
            return Response(
                {"detail": "Filter Error - " + str(ex)},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = self.OutPutDetailSerializer(query)
        return Response(serializer.data)


class PostCreateApi(ApiAuthMixin, APIView):
    class InputSerializer(serializers.Serializer):
        content = serializers.CharField(max_length=1000)
        title = serializers.CharField(max_length=200)

    class OutPutSerializer(serializers.ModelSerializer):
        class Meta:
            model = Post
            fields = ("pk", "title", "content", "created_at", "updated_at")

    @extend_schema(
        responses=OutPutSerializer,
        request=InputSerializer,
    )
    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            query = post_create(
                title=serializer.validated_data.get("title"),
                content=serializer.validated_data.get("content"),
            )
        except Exception as ex:
            return Response(
                {"detail": "Database Error - " + str(ex)},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(
            self.OutPutSerializer(query).data, status=status.HTTP_201_CREATED
        )


class PostUpdateApi(ApiAuthMixin, APIView):
    class InputSerializer(serializers.Serializer):
        content = serializers.CharField(max_length=1000)
        title = serializers.CharField(max_length=200)

    @extend_schema(
        request=InputSerializer,
    )
    def patch(self, request, post_id):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            post_update(
                pk=post_id,
                data=serializer.data,
            )
        except Exception as ex:
            return Response(
                {"detail": "Database Error - " + str(ex)},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(status=status.HTTP_200_OK)
