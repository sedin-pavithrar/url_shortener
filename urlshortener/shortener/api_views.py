"""API views for the URL shortening service."""

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ShortURL
from .serializers import ShortURLSerializer, ShortURLStatsSerializer
from .utils import unique_code


class ShortURLAPIView(APIView):
    """Handle CRUD operations for shortened URLs."""

    def post(self, request):
        """
        Create a new shortened URL.

        Generates a unique short code and stores the URL in the database.

        :param request: Incoming HTTP request containing the URL.
        :type request: rest_framework.request.Request
        :return: JSON response containing the created shortened URL.
        :rtype: rest_framework.response.Response
        """
        serializer = ShortURLSerializer(data=request.data)

        if serializer.is_valid():
            # CHANGE:
            # Generate a unique short code before saving.
            short = serializer.save(short_code=unique_code())

            # CHANGE:
            # Return the saved object so generated fields are included.
            return Response(
                ShortURLSerializer(short).data,
                status=status.HTTP_201_CREATED,
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )

    def get(self, request, short_code):
        """
        Retrieve a shortened URL.

        :param request: Incoming HTTP request.
        :type request: rest_framework.request.Request
        :param short_code: Unique short code.
        :type short_code: str
        :return: Short URL details.
        :rtype: rest_framework.response.Response
        """
        # CHANGE:
        # Replaced try/except with get_object_or_404().
        short = get_object_or_404(
            ShortURL,
            short_code=short_code,
        )

        serializer = ShortURLSerializer(short)
        return Response(serializer.data)

    def put(self, request, short_code):
        """
        Update an existing shortened URL.

        :param request: Incoming HTTP request.
        :type request: rest_framework.request.Request
        :param short_code: Unique short code.
        :type short_code: str
        :return: Updated URL details.
        :rtype: rest_framework.response.Response
        """
        short = get_object_or_404(
            ShortURL,
            short_code=short_code,
        )

        serializer = ShortURLSerializer(
            short,
            data=request.data,
        )

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_200_OK,
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )

    def delete(self, request, short_code):
        """
        Delete a shortened URL.

        :param request: Incoming HTTP request.
        :type request: rest_framework.request.Request
        :param short_code: Unique short code.
        :type short_code: str
        :return: Empty response with HTTP 204.
        :rtype: rest_framework.response.Response
        """
        short = get_object_or_404(
            ShortURL,
            short_code=short_code,
        )

        short.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class ShortURLStatsAPIView(APIView):
    """Handle statistics for shortened URLs."""

    def get(self, request, short_code):
        """
        Retrieve statistics for a shortened URL.

        :param request: Incoming HTTP request.
        :type request: rest_framework.request.Request
        :param short_code: Unique short code.
        :type short_code: str
        :return: Statistics including access count.
        :rtype: rest_framework.response.Response
        """
        short = get_object_or_404(
            ShortURL,
            short_code=short_code,
        )

        serializer = ShortURLStatsSerializer(short)

        return Response(serializer.data)
