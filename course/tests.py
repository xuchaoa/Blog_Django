from django.test import TestCase

# Create your tests here.

a = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
a.sort(key=lambda x:x[0],reverse=False)
print(a)
a.sort(key=lambda x:x[0],reverse=True)
print(a)