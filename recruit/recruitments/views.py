from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.http import JsonResponse

from recruit.users.models import User as user_model
from . import models, serializers
from .forms import CreateRecruitmentForm, UpdateRecruitmentForm

# Create your views here.
def index(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            recruitments = models.Recruitment.objects.filter(
            ).order_by("-create_at")

            serializer = serializers.RecruitmentSerializer(recruitments, many=True)
            print(serializer.data)

            return render(
                request,
                'recruitments/main.html',
                {"recruitments": serializer.data}
            )

def recruitment_create(request):
    if request.method == 'GET':
        form = CreateRecruitmentForm()
        return render(request, 'recruitments/recruitment_create.html', {"form": form})

    elif request.method == 'POST':
        if request.user.is_authenticated:
            user = get_object_or_404(user_model, pk=request.user.id)

            form = CreateRecruitmentForm(request.POST, request.FILES)
            if form.is_valid():
                recruitment = form.save(commit=False)
                recruitment.rc_author = user 
                recruitment.cp_id = user.cp
                recruitment.save()
            else:
                print(form.errors)

            return redirect(reverse('recruitments:index'))

        else:
            return render(request, 'users/main.html')

def recruitment_update(request, recruitment_id):
    if request.user.is_authenticated:
        # 작성자 체크
        recruitment = get_object_or_404(models.Recruitment, pk=recruitment_id)
        if request.user != recruitment.rc_author:
            return redirect(reverse('recruitments:index'))

        # GET 요청
        if request.method == 'GET':
            form = UpdateRecruitmentForm(instance=recruitment)
            return render(
                request,
                'recruitments/recruitment_update.html',
                {"form": form, "recruitment": recruitment}
            )

        elif request.method == 'POST':
            # 업데이트 버튼 클릭 후 저장을 위한 POST api 요청 로직
            form = UpdateRecruitmentForm(request.POST)
            if form.is_valid():
                recruitment.rc_position = form.cleaned_data['rc_position']
                recruitment.rc_reward = form.cleaned_data['rc_reward']
                recruitment.rc_content = form.cleaned_data['rc_content']
                recruitment.rc_skill = form.cleaned_data['rc_skill']
                recruitment.save()

            return redirect(reverse('recruitments:index'))

    else:
        return render(request, 'users/main.html')


def recruitment_delete(request, recruitment_id):
    if request.user.is_authenticated:
        recruitment = get_object_or_404(models.Recruitment, pk=recruitment_id)
        if request.user == recruitment.rc_author:
            recruitment.delete()

        return redirect(reverse('recruitments:index'))

    else:
        return render(request, 'users/main.html')


def search(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            searchKeyword = request.GET.get("q", "")
            recruitments = models.Recruitment.objects.filter(
                Q(rc_content__contains=searchKeyword)
            ).order_by("-create_at")

            serializer = serializers.RecruitmentSerializer(recruitments, many=True)
            print(serializer.data)

            return render(
                request,
                'recruitments/main.html',
                {"recruitments": serializer.data}
            )

    else:
        return render(request, 'users/main.html')

    