from django.shortcuts import render
from .models import Food
from django.http import JsonResponse

# Create your views here.
def food_list(request):
    foods = Food.objects.filter(is_available=True)
    data = []
    for food in foods:
        data.append({
            'id': food.id,
            'name': food.name,
            'description': food.description,
            'price': float(food.price),
            'image_url': food.image.url if food.image else None,
        })
    return JsonResponse({'foods': data})

def food_detail(request, food_id):
    try:
        food = Food.objects.get(id=food_id, is_available=True)
        data = {
            'id': food.id,
            'name': food.name,
            'description': food.description,
            'price': float(food.price),
            'image_url': food.image.url if food.image else None,
            'created_at': food.created_at,
            'updated_at': food.updated_at,
        }
        return JsonResponse({'food': data})
    except Food.DoesNotExist:
        return JsonResponse({'error': 'Food not found'}, status=404)
