liczba_str = "5.8"

liczba_float = float(liczba_str)
print(liczba_float) 

liczba_int = int(liczba_float)
print(liczba_int) 

# Podczas konwersji z float na int część po przecinku zostaje obcięta,
# a nie zaokrąglona. Dlatego 5.8 zamienia się na 5.