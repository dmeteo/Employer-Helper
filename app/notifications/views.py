from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from .models import Notification

from django.http import JsonResponse
from .models import Notification
from django.contrib.auth.decorators import login_required

@login_required
def get_notifications(request):
    notifications = Notification.objects.filter(user=request.user, is_read=False)
    data = [
        {
            "id": notification.id,
            "message": notification.message,
            "created_at": notification.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        }
        for notification in notifications
    ]
    return JsonResponse({"notifications": data})


@csrf_exempt
@login_required
def mark_as_read(request, notification_id):
    try:
        notification = Notification.objects.get(id=notification_id, user=request.user)
        notification.is_read = True
        notification.save()
        return JsonResponse({"status": "success"})
    except Notification.DoesNotExist:
        return JsonResponse({"status": "error", "message": "Notification not found"}, status=404)



# class NotificationListView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         user = request.user
#         notifications = Notification.objects.filter(recipient=user).order_by('-created_at')
#         data = [
#             {
#                 "id": n.id,
#                 "message": n.message,
#                 "type": n.type,
#                 "is_read": n.is_read,
#                 "created_at": n.created_at
#             } for n in notifications
#         ]
#         return Response(data)