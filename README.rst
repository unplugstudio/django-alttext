
Django Alt Text
===============

Generic alt text model associated to files by their path.

Install
-------

1. Install via pip: ``pip install django-alttext``.
2. Add ``alttext`` to your ``INSTALLED_APPS``.
3. Run migrations.
4. Optionally follow the integration instructions that apply to your case.

Usage
-----

Using one of the supported integrations staff users will be able to add alt text for images in the admin interface. The app stores a list of alt texts by their associated image path.

In your templates, you can now access the alt text for any file using the ``alttext`` filter:

.. code::

  {% load alttext_tags %}
  <img src="{{ mymodel.imagefield }}" alt="{{ mymodel.imagefield|alttext }}" >

Mezzanine integration
---------------------

If you're using Mezzanine and filebrowser-safe, add ``alttext.mezzanine`` to your INSTALLED_APPS before ``mezzanine.boot`` to enable alt-text links in the admin. A link to "Edit alt text" will appear next to each ``FileField`` in Add and Change forms.

Configuration
-------------

- Enable the admin list view to manage all AltText instances: ``settings.ALTTEXT_ADMIN_DISPLAY = True``.

Contributing
------------

Review contribution guidelines at CONTRIBUTING.md_.

.. _CONTRIBUTING.md: CONTRIBUTING.md
