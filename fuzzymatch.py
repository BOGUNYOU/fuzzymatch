#_*_ coding:utf-8 _*_
import re
import sys
collection = ['django_migrations.py',
              'django_admin_log',
              'django_generator.py',
              'migrations.py',
              'api_user.py',
              'user_group.py',
              'accounts.py']
suggestion = []
user_input = sys.argv[1]
pattern = '.*?'.join(user_input)
regex = re.compile(pattern)
for item in collection:
    match = regex.search(item)
    if match:
        suggestion.append((len(match.group()),match.start(),item))
print [x for _,_,x in sorted(suggestion)]
