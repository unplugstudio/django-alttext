
Django Alt Text
===============

Generic alt text model associated to files by their path.

Install
-------

1. Install via pip: ``pip install django-alttext``.
2. Add ``alttext`` to your ``INSTALLED_APPS``.
3. Run migrations.
4. Enable the admin interface if you require it: ``settings.ALTTEXT_ADMIN_DISPLAY = True``.
5. Optionally follow the integration instructions that apply to your case.

Mezzanine integration
---------------------

If you're using Mezzanine and filebrowser-safe, add ``alttext.mezzanine`` to your INSTALLED_APPS before ``mezzanine.boot`` to enable alt-text links in the admin. A link to "Edit alt text" will appear next to each ``FileField`` in Add and Change forms.

Contributing
------------

Review contribution guidelines at CONTRIBUTING.md_.

.. _CONTRIBUTING.md: CONTRIBUTING.md
