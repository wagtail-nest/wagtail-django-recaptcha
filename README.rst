.. image:: https://github.com/wagtail-nest/wagtail-django-recaptcha/actions/workflows/test.yml/badge.svg
   :target: https://github.com/wagtail-nest/wagtail-django-recaptcha/actions/workflows/test.yml
.. image:: https://img.shields.io/pypi/v/wagtail-django-recaptcha.svg
   :target: https://pypi.python.org/pypi/wagtail-django-recaptcha
.. image:: https://codeclimate.com/github/wagtail-nest/wagtail-django-recaptcha/badges/gpa.svg
   :target: https://codeclimate.com/github/wagtail-nest/wagtail-django-recaptcha
.. image:: https://coveralls.io/repos/github/wagtail-nest/wagtail-django-recaptcha/badge.svg?branch=main
   :target: https://coveralls.io/github/wagtail-nest/wagtail-django-recaptcha?branch=main

Wagtail ReCaptcha
=================

    Wagtail forms with a ReCaptcha form field/widget integration app. Wagtail ReCaptcha provides an easy way to integrate the `django-recaptcha <https://github.com/django-recaptcha/django-recaptcha>`_ field when using the Wagtail formbuilder.

Check out `Awesome Wagtail <https://github.com/springload/awesome-wagtail>`_ for more awesome packages and resources from the Wagtail community.

Installation
------------

#. Install wagtailcaptcha via pip ``pip install wagtail-django-recaptcha`` or add ``wagtailcaptcha`` to your Python path.

#. Add ``wagtailcaptcha`` to your ``INSTALLED_APPS`` setting.

#. Config django-recaptcha as explained in `here <https://github.com/django-recaptcha/django-recaptcha>`_.


Usage
-----

Field
~~~~~

The quickest way to add a captcha field to a Wagtail Form Page is to inherit from the two options provided, ``WagtailCaptchaForm`` or ``WagtailCaptchaEmailForm``. The first options inherits from ``AbstractForm`` while the seconds does it from ``AbstractEmailForm``. Either way your page is going to display a captcha field at the end of the form.

Example

.. code-block:: python

    from wagtail.contrib.forms.models import AbstractFormField
    from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
    from wagtail.fields import RichTextField

    from modelcluster.fields import ParentalKey

    from wagtailcaptcha.models import WagtailCaptchaEmailForm


    class SubmitFormField(AbstractFormField):
        page = ParentalKey('SubmitFormPage', related_name='form_fields')


    class SubmitFormPage(WagtailCaptchaEmailForm):
        body = RichTextField(blank=True, help_text='Edit the content you want to see before the form.')
        thank_you_text = RichTextField(blank=True, help_text='Set the message users will see after submitting the form.')

        class Meta:
            verbose_name = "Form submission page"


    SubmitFormPage.content_panels = [
        FieldPanel('title', classname="full title"),
        FieldPanel('body', classname="full"),
        FieldPanel('thank_you_text', classname="full"),
        InlinePanel('form_fields', label="Form fields"),
        MultiFieldPanel([
            FieldPanel('to_address'),
            FieldPanel('from_address'),
            FieldPanel('subject'),
        ], "Email notification")
    ]


The captcha field can't be added from the admin UI but will appear in your frontend as the last of the form fields.

If you need to customise the behaviour of the form builder, make sure to inherit from ``wagtailcaptcha.forms.WagtailCaptchaFormBuilder`` instead of Wagtail's default form builder, then declare it as usual on the page model.

.. code-block:: python

    from wagtailcaptcha.forms import WagtailCaptchaFormBuilder
    from wagtailcaptcha.models import WagtailCaptchaForm


    class CustomFormBuilder(WagtailCaptchaFormBuilder):
        # Some custom behaviour...


    class FormPage(WagtailCaptchaForm):
        form_builder = CustomFormBuilder
        # The rest of the page definition as usual...

For a more thorough example, `Made with Wagtail <http://madewithwagtail.org/>`_ (`github.com/springload/madewithwagtail <https://github.com/springload/madewithwagtail>`_) is an example of an open-source site using this module.

Development
-----------

Installation
~~~~~~~~~~~~

    Requirements: ``virtualenv``, ``pyenv``, ``twine``

.. code:: sh

    git clone git@github.com:wagtail-nest/wagtail-django-recaptcha.git
    cd wagtail-django-recaptcha/
    virtualenv .venv
    source ./.venv/bin/activate
    make init

Commands
~~~~~~~~

Use `make help` to get a list of commands.

Releases
~~~~~~~~

*  Make a new branch for the release of the new version.
*  Update the `CHANGELOG`_.
*  Update the version number in ``wagtailcaptcha/__init__.py``, following semver.
*  Make a PR and squash merge it.
*  Back on ``master`` with the PR merged, use ``make publish`` (confirm, and enter your password).
*  Finally, go to GitHub and create a release and a tag for the new version.
*  Done!

.. _Semantic Versioning: http://semver.org/spec/v2.0.0.html
.. _changelog: https://github.com/wagtail-nest/wagtail-django-recaptcha/blob/main/CHANGELOG.rst

Acknowledgements
----------------

Wagtail ReCaptcha was originally created by `Springload <https://springload.co.nz/>`_. They kindly transferred the project to the Wagtail Nest community in December 2024.
