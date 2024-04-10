from drf_spectacular.utils import extend_schema
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView

from blogapp.api.mixins import ApiAuthMixin
from blogapp.api.pagination import (LimitOffsetPagination,
                                    get_paginated_response_context)
from blogapp.blog.models import Comment
from blogapp.blog.selectors.comment import post_comment_list
from blogapp.blog.services.comment import comment_create


class CommentListApi(APIView):
    class Pagination(LimitOffsetPagination):
        default_limit = 10

    class OutPutSerializer(serializers.ModelSerializer):
        replies = serializers.StringRelatedField(many=True)

        class Meta:
            model = Comment
            fields = ["pk", "text", "email", "replies"]

    @extend_schema(
        responses=OutPutSerializer,
    )
    def get(self, request, post_id):
        try:
            query = post_comment_list(post_id=post_id)
        except Exception as ex:
            return Response(
                {"detail": "" + str(ex)},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return get_paginated_response_context(
            pagination_class=self.Pagination,
            serializer_class=self.OutPutSerializer,
            queryset=query,
            request=request,
            view=self,
        )


class CommentCreateApi(ApiAuthMixin, APIView):
    class InputSerializer(serializers.Serializer):
        text = serializers.CharField(max_length=1000)
        email = serializers.EmailField(max_length=200)
        post = serializers.IntegerField(min_value=1)
        parent = serializers.IntegerField(min_value=1, required=False, default=None)

    class OutPutSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = [
                "id",
                "post",
                "parent",
                "text",
                "email",
            ]

    @extend_schema(
        responses=OutPutSerializer,
        request=InputSerializer,
    )
    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            query = comment_create(
                email=serializer.validated_data.get("email"),
                text=serializer.validated_data.get("text"),
                post=serializer.validated_data.get("post"),
                parent=serializer.validated_data.get("parent"),
            )
        except Exception as ex:
            return Response(
                {"detail": "Database Error - " + str(ex)},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(
            self.OutPutSerializer(query).data, status=status.HTTP_201_CREATED
        )
