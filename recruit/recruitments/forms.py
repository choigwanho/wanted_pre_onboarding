from django import forms
from .models import Recruitment

class CreateRecruitmentForm(forms.ModelForm):
    class Meta:
        model = Recruitment
        fields = ["rc_position", "rc_reward", "rc_content", "rc_skill"]
        
        labels = {
            "rc_position" : "채용포지션",
            "rc_reward" : "채용보상금", 
            "rc_content" : "채용내용", 
            "rc_skill" : "사용기술",
        }

class UpdateRecruitmentForm(forms.ModelForm):
    class Meta:
        model = Recruitment
        fields = ["rc_position", "rc_reward", "rc_content", "rc_skill"]

        labels = {
            "rc_position" : "채용포지션", 
            "rc_reward" : "채용보상금", 
            "rc_content" : "채용내용", 
            "rc_skill" : "사용기술",
            }