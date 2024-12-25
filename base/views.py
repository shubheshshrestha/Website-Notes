from django.shortcuts import render
from .models import Note, NoteType
from .forms import NoteForm, NoteFormType

# Create your views here.

def home(request):
    note_objs = Note.objects.all().order_by('id')
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

def edit_note(request,pk):
    note_obj = Note.objects.get(id=pk)
    if request.method == 'POST':
        form_obj = NoteForm(instance=note_obj, data=request.POST)
        if form_obj.is_valid():
            form_obj.save()
    form_obj = NoteForm(instance=note_obj)
    data = {'form':form_obj}
    return render(request,'edit_note.html', context=data)

def create_type(request):
    type_form_obj = NoteFormType()
    if request.method == "POST":
        type_form_obj = NoteFormType(data=request.POST)
        if type_form_obj.is_valid():
            type_form_obj.save()
    data = {"form_type": type_form_obj}
    return render(request, "create_type.html", context=data)


