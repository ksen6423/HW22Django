import os
import django


from django.core.management import call_command
from io import StringIO

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()


out = StringIO()
call_command('dumpdata', stdout=out, indent=4)
data = out.getvalue()

with open('groups.json', 'w', encoding='utf-8') as f:
    f.write(data)
