from django.shortcuts import render

def blog_view(request):
    return render(request, 'blog.html')  # Certifique-se de que 'blog.html' existe e o nome está correto
