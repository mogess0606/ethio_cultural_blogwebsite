from .models import Category

def get_all_category(request):
    categories = Category.objects.all()
    context = {
        "Categories": categories
    }
    return context