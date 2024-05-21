from django.shortcuts import redirect

def admin_panel(request):
    return redirect('admin:index')