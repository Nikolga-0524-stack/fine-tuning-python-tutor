import json
import random

# Загрузка датасета
with open('dataset.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Перемешиваем данные для случайного разделения
random.seed(42)  # Фиксируем seed для воспроизводимости
random.shuffle(data)

# Разделение: 80% train, 20% test
split_idx = int(len(data) * 0.8)
train_data = data[:split_idx]
test_data = data[split_idx:]

print(f"Всего примеров: {len(data)}")
print(f"Train: {len(train_data)} примеров")
print(f"Test: {len(test_data)} примеров")

# Сохранение train датасета
with open('train_dataset.json', 'w', encoding='utf-8') as f:
    json.dump(train_data, f, ensure_ascii=False, indent=2)

print(f"\n✅ Train датасет сохранён: train_dataset.json")

# Сохранение test датасета
with open('test_dataset.json', 'w', encoding='utf-8') as f:
    json.dump(test_data, f, ensure_ascii=False, indent=2)

print(f"✅ Test датасет сохранён: test_dataset.json")

# Показываем первые 3 примера из test (чтобы убедиться, что они не попали в train)
print(f"\n--- Примеры из TEST датасета (модель их НЕ увидит при обучении) ---")
for i, example in enumerate(test_data[:3]):
    print(f"\nTest пример {i+1}:")
    print(f"  Вопрос: {example['instruction']}")
    print(f"  Ответ: {example['output'][:100]}...")