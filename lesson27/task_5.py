# Zadanie 5 – Czyszczenie cache
# Znajdź w dokumentacji Django komendę manage.py, która pozwala na wyczyszczenie
# całego cache. Użyj jej w terminalu, aby usunąć wszystkie zbuforowane dane.



python manage.py shell -c "from django.core.cache import cache; cache.clear()"





# venv) PS E:\PythonPro-Course\homework\lesson27> python manage.py shell -c "from django.core.cache import cache; cache.clear()"
# 13 objects imported automatically (use -v 2 for details).

# (venv) PS E:\PythonPro-Course\homework\lesson27> 