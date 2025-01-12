from wagtail.contrib.forms.forms import FormBuilder

from django_recaptcha.fields import ReCaptchaField


class WagtailCaptchaFormBuilder(FormBuilder):
    CAPTCHA_FIELD_NAME = "wagtailcaptcha"

    @property
    def formfields(self):
        # Add wagtailcaptcha to formfields property
        fields = super().formfields
        fields[self.CAPTCHA_FIELD_NAME] = ReCaptchaField(label="")

        return fields


def remove_captcha_field(form):
    if form.is_valid():
        form.fields.pop(WagtailCaptchaFormBuilder.CAPTCHA_FIELD_NAME, None)
        form.cleaned_data.pop(WagtailCaptchaFormBuilder.CAPTCHA_FIELD_NAME, None)
