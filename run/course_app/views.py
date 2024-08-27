from django.shortcuts import render, get_object_or_404
from .models import Course

def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'course_app/single_course.html', {'course': course})
