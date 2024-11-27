from folio.models import Category


def object(request):
    categories = Category.objects.all().order_by('name')
    
    return {
        "categories": categories,
    }
