import json
from django.http import JsonResponse
from django.shortcuts import render
from .models import Message, Room
from django.views.generic.detail import DetailView

def home(request):
    rooms = Room.objects.all().order_by('-created_at')
    return render(request, 'chat/home.html', {'rooms': rooms})

class RoomDetailView(DetailView):
    model = Room
    template_name = 'chat/list-messages.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        room = self.get_object()
        context['messages'] = room.messages.all()
        return context


def send_message(request, pk):
    if request.method == 'POST':
        data = json.loads(request.body)
        room = Room.objects.get(id=pk)
        new_message = Message.objects.create(user=request.user, tex=data['message'])
        room.messages.add(new_message)
        return JsonResponse({'message': new_message.tex, 'user': new_message.user.username})
    return JsonResponse({'error': 'Invalid request'}, status=400)

def create_room(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        title = data.get('title')
        room = Room.objects.create(title=title)
        room.users.add(request.user)
        return JsonResponse({'room_id': room.id, 'title': room.title})
    return JsonResponse({'error': 'Invalid request'}, status=400)