from collections import Counter

s = input().strip()

genetic_code = {
    'UUU': 'F', 'UUC': 'F',          # Фенилаланин
    'UUA': 'L', 'UUG': 'L',          # Лейцин
    'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',  # Лейцин
    
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I',  # Изолейцин
    'AUG': 'M',                          # Метионин (старт)
    
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',  # Валин
    
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',  # Серин
    'AGU': 'S', 'AGC': 'S',                          # Серин
    
    'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',  # Пролин
    
    'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',  # Треонин
    
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',  # Аланин
    
    'UAU': 'Y', 'UAC': 'Y',          # Тирозин
    'UAA': '*', 'UAG': '*', 'UGA': '*',  # Стоп-кодоны
    
    'CAU': 'H', 'CAC': 'H',          # Гистидин
    'CAA': 'Q', 'CAG': 'Q',          # Глутамин
    
    'AAU': 'N', 'AAC': 'N',          # Аспарагин
    'AAA': 'K', 'AAG': 'K',          # Лизин
    
    'GAU': 'D', 'GAC': 'D',          # Аспарагиновая кислота
    'GAA': 'E', 'GAG': 'E',          # Глутаминовая кислота
    
    'UGU': 'C', 'UGC': 'C',          # Цистеин
    'UGG': 'W',                      # Триптофан
    
    'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',  # Аргинин
    'AGA': 'R', 'AGG': 'R',                          # Аргинин
    
    'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',  # Глицин
}

counts = Counter(genetic_code.values())

res = 1

for i in s:
    res = (res * counts[i]) % 1000000

res = (res * counts['*']) % 1000000

print(res)