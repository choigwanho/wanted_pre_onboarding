from rest_framework import serializers

from recruit.users.models import User as user_model
from recruit.users.models import Company as company_model
from . import models


class AuthorCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = company_model
        fields = (
            "cp_name",
            "cp_nation",
            "cp_city"
        )


class RecruitmentAuthorSerializer(serializers.ModelSerializer):
    cp = AuthorCompanySerializer()
    class Meta:
        model = user_model
        fields = (
            "id",
            "username",
            "cp"
        )

class RecruitmentSerializer(serializers.ModelSerializer):
    rc_author = RecruitmentAuthorSerializer()

    class Meta:
        model = models.Recruitment
        fields = (
            "id",
            "rc_author",
            "rc_content",
            "rc_position",
            "rc_reward",
            "rc_skill",
        )