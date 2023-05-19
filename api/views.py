from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from api.models import Point

# import utils
from api.utils import find_all_distance, calculate_distance

@csrf_exempt
def find_two_points_closest(request):
    #if we get data via post
    if request.method == 'POST':
        points = request.POST.get('points')
        point_list = points.split(';')
        print(f"Passed points are  {point_list}")
        try:
            closest_points = find_all_distance(point_list)
        except Exception as e:
            return JsonResponse({'error': f'Invalid Data Passed. Should be a semicolon separated coordinates.  {e}'})
        point = Point(coordinates=points, closest_points=closest_points)
        point.save()
        return JsonResponse({
            'message': 'Points and closest points saved successfully.',
            "inputs":points,
            "solution":closest_points
            })
    #if get method is issued...
    points = Point.objects.all().values('coordinates', 'closest_points')
    return JsonResponse({'points': list(points)})
