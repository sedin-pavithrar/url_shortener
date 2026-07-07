from django.shortcuts import render
from .models import ShortURL
from .forms import GetUrl
from .utils import unique_code

def home_view (request):
    short_url = None 
    form = GetUrl()

    if request.method == "POST":
        form = GetUrl(request.POST)

        if form.is_valid():
            original_url = form.cleaned_data["original_url"]
            short_code = unique_code()

            short_url = ShortURL.objects.create(
                original_url = original_url,
                short_code = short_code
        )
            
    context = {
        "form":form,
        "short_url":short_url
    }

    return render(request,"shortener/home.html",context)

    





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