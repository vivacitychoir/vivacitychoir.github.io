{% set vivacity_user = 'vivacity' %}
{% set vivacity_venv = '/home/{0}/vivacity'.format(vivacity_user) %}
{% set vivacity_proj = '{0}/site'.format(vivacity_venv) %}
{% set vivacity_url = 'vivacitychoir.com' %}
{% set vivacity_root = '{0}/output'.format(vivacity_proj) %}

vivacity:
  user: {{ vivacity_user }}
  venv: {{ vivacity_venv }}
  proj: {{ vivacity_proj }}
  url: {{ vivacity_url }}
  root: {{ vivacity_root }}
