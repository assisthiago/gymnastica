from django import forms

from app.core.models import Branch, Training, User


class TrainingForm(forms.ModelForm):

    # Filter the personal and clients fields
    def __init__(self, *args, **kwargs):
        super(TrainingForm, self).__init__(*args, **kwargs)
        self.fields["personal"].queryset = User.objects.filter(groups__in=[3]).order_by(
            "first_name", "last_name"
        )
        self.fields["clients"].queryset = User.objects.filter(groups__in=[1]).order_by(
            "first_name", "last_name"
        )

    class Meta:
        model = Training
        fields = "__all__"
