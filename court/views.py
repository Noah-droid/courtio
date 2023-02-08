from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import Case, Judge, Witness

def index(request):
    return HttpResponse('<h1>WTF</h1>')
    

def case_list(request):
    cases = Case.objects.all()
    return render(request, 'court_session/case_list.html', {'cases': cases})

def case_detail(request, case_id):
    case = get_object_or_404(Case, id=case_id)
    return render(request, 'court_session/case_detail.html', {'case': case})

def add_case(request):
    if request.method == 'POST':
        case_number = request.POST.get('case_number')
        case_title = request.POST.get('case_title')
        case_description = request.POST.get('case_description')
        date_filed = request.POST.get('date_filed')
        new_case = Case.objects.create(case_number=case_number, case_title=case_title, case_description=case_description, date_filed=date_filed)
        return redirect('case_detail', case_id=new_case.id)
    return render(request, 'court_session/add_case.html')

