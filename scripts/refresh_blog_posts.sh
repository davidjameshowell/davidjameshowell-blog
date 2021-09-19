#!/bin/bash

CI_JOB="${CI_JOB:-true}"

if [[ $CI_JOB == *"true"* ]]; then
    export PATH="/opt/hostedtoolcache/pyenv_root/2.0.0/x64/shims:${PATH}"
    eval "$(pyenv init --path)"
    pip install wheel
    POETRY_VIRTUALENVS_CREATE=false && poetry install --no-root
fi

python ./deploy_blog_post.py
