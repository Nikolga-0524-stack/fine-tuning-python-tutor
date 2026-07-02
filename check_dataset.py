import json

# Загрузка датасета
with open('dataset.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Проверка структуры
print(f"Всего примеров: {len(data)}")
print(f"\nПервые 3 примера:")
for i, example in enumerate(data[:3]):
    print(f"\n--- Пример {i+1} ---")
    print(f"Instruction: {example.get('instruction', 'НЕТ ПОЛЯ')[:100]}...")
    print(f"Output: {example.get('output', 'НЕТ ПОЛЯ')[:100]}...")

# Проверка, что все примеры имеют нужные поля
valid_count = sum(1 for ex in data if 'instruction' in ex and 'output' in ex)
print(f"\n\nВалидных примеров (с instruction и output): {valid_count}/{len(data)}")

# Статистика по длине текстов
instruction_lengths = [len(ex['instruction']) for ex in data]
output_lengths = [len(ex['output']) for ex in data]

print(f"\nДлина instruction: средняя {sum(instruction_lengths)/len(instruction_lengths):.0f} символов")
print(f"Длина output: средняя {sum(output_lengths)/len(output_lengths):.0f} символов")