from django import forms
from .models import Memo, Tag

class MemoForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    new_tags = forms.CharField(
        required=False, 
        help_text="カンマ区切りでタグを複数追加できます"
    )

    class Meta:
        model = Memo
        fields = ['title', 'content', 'tags']

    def clean_new_tags(self):
        """新しいタグをカンマ区切りで処理"""
        new_tags = self.cleaned_data.get('new_tags', '').strip()
        return [tag.strip() for tag in new_tags.split(',') if tag.strip()]

    def save(self, commit=True):
        """新しいタグを保存してメモにタグ付けする"""
        memo = super().save(commit=False)
        new_tags = self.cleaned_data.get('new_tags', [])

        if commit:
            memo.save()
            self.save_m2m()  # 既存のタグを保存

            for tag_name in new_tags:
                tag, created = Tag.objects.get_or_create(name=tag_name)
                memo.tags.add(tag)  # メモに新規タグを追加

        return memo
