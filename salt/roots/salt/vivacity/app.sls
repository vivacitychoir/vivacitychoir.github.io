{% set vivacity_venv = salt['pillar.get']('vivacity:venv') %}
{% set vivacity_proj = salt['pillar.get']('vivacity:proj') %}
{% set vivacity_user = salt['pillar.get']('vivacity:user') %}

include:
  - git
  - nginx
  - python.pip
  - python.virtualenv

{{ vivacity_user }}:
  user:
    - present
    - shell: /bin/bash
    - home: /home/{{ vivacity_user }}

vivacity_venv:
  virtualenv:
    - managed
    - name: {{ vivacity_venv }}
    - runas: {{ vivacity_user }}
    - require:
      - pkg: python-virtualenv
      - user: {{ vivacity_user }}

vivacitysite:
  git:
    - latest
    - name: https://github.com/drgjm/vivacitysite.git
    - target: {{ vivacity_proj }}
    - runas: {{ vivacity_user }}
    - force: True
    - require:
      - pkg: git
      - virtualenv: vivacity_venv
    - watch_in:
      - service: nginx

vivacity_pkgs:
  pip:
    - installed
    - bin_env: {{ vivacity_venv }}
    - requirements: {{ vivacity_proj }}/requirements.txt
    - require:
      - git: vivacitysite
      - pkg: python-pip
      - virtualenv: vivacity_venv

/etc/nginx/conf.d/vivacity.conf:
  file:
    - managed
    - source: salt://vivacity/files/vivacity.conf
    - template: jinja
    - user: root
    - group: root
    - mode: 644
    - require:
      - git: vivacitysite
      - pkg: nginx
    - watch_in:
      - service: nginx

/etc/nginx/sites-enabled/default:
  file:
    - absent

