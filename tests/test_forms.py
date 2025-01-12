from django.test import TestCase

from django_recaptcha.fields import ReCaptchaField
from home.models import TestCaptchaEmailFormField

from wagtailcaptcha.forms import WagtailCaptchaFormBuilder


class WagtailCaptchaFormBuilderTestCase(TestCase):
    fixtures = ["test_data.json"]

    def test_captcha_field_name(self):
        self.assertEqual(WagtailCaptchaFormBuilder.CAPTCHA_FIELD_NAME, "wagtailcaptcha")

    def test_captcha_field_is_present(self):
        user_defined_fields = TestCaptchaEmailFormField.objects.all()
        form = WagtailCaptchaFormBuilder(user_defined_fields)
        generated_fields = form.formfields

        self.assertIn(
            WagtailCaptchaFormBuilder.CAPTCHA_FIELD_NAME,
            generated_fields,
            msg="Captcha field should be present in generated form fields.",
        )
        self.assertIsInstance(
            generated_fields[WagtailCaptchaFormBuilder.CAPTCHA_FIELD_NAME],
            ReCaptchaField,
            msg="Captcha field should be an instance of `django_recaptcha.fields.ReCaptchaField`.",
        )

    def test_user_defined_fields_are_present(self):
        user_defined_fields = TestCaptchaEmailFormField.objects.all()
        user_defined_field_names = [f.clean_name for f in user_defined_fields]

        form = WagtailCaptchaFormBuilder(user_defined_fields)
        generated_fields = form.formfields

        generated_fields.pop(WagtailCaptchaFormBuilder.CAPTCHA_FIELD_NAME)
        generated_field_names = list(
            generated_fields.keys()
        )  # Cast the `KeysView` to list for Python 3.

        # Note: `user_defined_field_names` and `generated_field_names` should already be in the same order
        # since the former is a queryset (it has a specific order)
        # and the latter an OrderedDict build from that same queryset.
        self.assertEqual(
            user_defined_field_names,
            generated_field_names,
            msg="The form builder should not add or remove user defined fields.",
        )
