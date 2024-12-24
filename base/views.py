from django.shortcuts import render
from .models import Note, NoteType
from .forms import NoteForm

# Create your views here.

def home(request):
    note_objs = Note.objects.all()
    data = {'notes': note_objs}
    return render(request,'index.html', context= data)

def note_type(request):
    note_objs = Note.objects.all()
    data = {'notes': note_objs}
    return render(request,'note_type.html', context= data)

# def create_note(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         description = request.POST.get("description")
#         type_id = request.POST.get("type")

#         n_t_obj = NoteType.objects.get(id=type_id)
        
#         Note.objects.create(name=name,description=description,type=n_t_obj)
#     note_type_objs = NoteType.objects.all()
#     data = {'notes_types': note_type_objs}
#     return render(request, 'create_note.html', context= data)


def create_note(request):
    note_form_obj = NoteForm()
    if request.method == "POST":
        note_form_obj = NoteForm(data=request.POST)
        if note_form_obj.is_valid(): #Validation
            note_form_obj.save()
    data = {'form':note_form_obj}
    return render(request, "create_note.html", context=data)

