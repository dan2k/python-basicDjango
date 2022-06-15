# python-basicDjango
pip install Django==4.0.5
python -m django --version
django-admin startproject firstdjango .
python manage.py runserver
python manage.py migrate

query string ไม่เอามาคิดใน route ไม่ 404

https://codecollab.io/ แชร์โค้ดให้คนอื่นดู ดูแก้ไขแบบ realtime ได้เลย

python manage.py makemigrations
pip install mysqlclient

python manage.py migrate

python manage.py createsuperuser
python manage.py createsuperuser --username

from django.contrib.auth.decorators import login_required
@login_required(login_url='/login')

 {% csrf_token %} ระบบจะตรวจสอบได้ว่า กรอกจากเว็บเรา

 pip install djangorestframework
