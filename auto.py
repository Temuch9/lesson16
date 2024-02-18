import random
auto = ['Cherry', 'Toyota', 'Ferrari', 'Lada', 'Gelly', 'Москвич', 'Уаз', 'Ford', 'Haval', 'Tesla']
x = random.choice(auto)
print(x)
a = 'Авто не под санкциями' if (x == 'Lada', 'Gelly', 'Уаз', 'Haval', 'Cherry', 'Москвич') else 'Автомобиль под санкциями'
print(a)

