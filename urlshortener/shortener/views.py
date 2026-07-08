from django.shortcuts import render
from .models import ShortURL
from .forms import GetUrl
from .utils import unique_code
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

"""
Views for the URL shortening application.

Provides HTML views for creating, updating,
deleting, and redirecting shortened URLs.

"""


def home_view(request):
    """
    Display the homepage and create a shortened URL.

    If the request method is POST, validate the submitted
    URL, generate a unique short code, and save the
    shortened URL.

    :param request: Incoming HTTP request.
    :type request: HttpRequest
    :return: Rendered homepage.
    :rtype: HttpResponse

    """

    short_url = None
    form = GetUrl()

    if request.method == "POST":
        form = GetUrl(request.POST)

        if form.is_valid():
            original_url = form.cleaned_data["original_url"]
            short_code = unique_code()

            short_url = ShortURL.objects.create(url=original_url, short_code=short_code)

    context = {"form": form, "short_url": short_url}

    return render(request, "shortener/home.html", context)


def redirect_url(request, short_code):
    """
     Redirect a short URL to its original URL.
    Increments the access count before redirecting.
    :param request: Incoming HTTP request.
    :type request: HttpRequest
    :param short_code: Generated short code.
    :type short_code: str
    :return: Redirect response.
    :rtype: HttpResponseRedirect
    """
    url = get_object_or_404(ShortURL, short_code=short_code)
    url.access_count += 1
    url.save(update_fields=["access_count"])
    return redirect(url.url)


def dashboard(request):
    urls = ShortURL.objects.order_by("-created_at")

    context = {"urls": urls}

    return render(request, "shortener/dashboard.html", context)


def delete_url(request, id):
    url = get_object_or_404(ShortURL, id=id)
    url.delete()
    return redirect("dashboard")


def update_url(request, id):
    url = get_object_or_404(ShortURL, id=id)
    if request.method == "POST":
        form = GetUrl(request.POST)

        if form.is_valid():
            url.url = form.cleaned_data["original_url"]
            url.save()

            return redirect("dashboard")

    return redirect("dashboard")


# User visits page
#         │
#         ▼
# Is request POST?
#         │
#    ┌────┴────┐
#    │         │
#  No         Yes
#    │         │
# Create     Validate Form
# empty form      │
#                 ▼
#           Is form valid?
#                 │
#            ┌────┴────┐
#            │         │
#           No        Yes
#            │         │
#      Show errors   Generate code
#                      │
#                      ▼
#                 Save to DB
#                      │
#                      ▼
#              Render template
