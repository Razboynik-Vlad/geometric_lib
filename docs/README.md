# Math formulas
## Area
- Circle: S = πR² (см. [Формула Площади круга](https://yandex.by/video/preview/7246615200798915892?text=%D0%B4%D0%BE%D0%BA%D0%B0%D0%B7%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D1%81%D1%82%D0%B2%D0%BE%20%D1%84%D0%BE%D1%80%D0%BC%D1%83%D0%BB%D1%8B%20%D0%BF%D0%BB%D0%BE%D1%89%D0%B0%D0%B4%D0%B8%20%D0%BA%D1%80%D1%83%D0%B3%D0%B0&path=yandex_search&parent-reqid=1728572958918907-17059737248404353548-balancer-l7leveler-kubr-yp-klg-54-BAL&from_type=vast))
- Rectangle: S = ab (см. [Формула Площади прямоугольника](https://yandex.by/video/preview/3369844751185063943?text=%D0%B4%D0%BE%D0%BA%D0%B0%D0%B7%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D1%81%D1%82%D0%B2%D0%BE%20%D1%84%D0%BE%D1%80%D0%BC%D1%83%D0%BB%D1%8B%20%D0%BF%D0%BB%D0%BE%D1%89%D0%B0%D0%B4%D0%B8%20%D0%BF%D1%80%D1%8F%D0%BC%D0%BE%D1%83%D0%B3%D0%BE%D0%BB%D1%8C%D0%BD%D0%B8%D0%BA%D0%B0&path=yandex_search&parent-reqid=1728573629021687-11507726721831934841-balancer-l7leveler-kubr-yp-klg-54-BAL&from_type=vast))
- Square: S = a² (см. [Формула Площади квадрата](https://yandex.by/video/preview/13869370009101690800?text=%D0%B4%D0%BE%D0%BA%D0%B0%D0%B7%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D1%81%D1%82%D0%B2%D0%BE%20%D1%84%D0%BE%D1%80%D0%BC%D1%83%D0%BB%D1%8B%20%D0%BF%D0%BB%D0%BE%D1%89%D0%B0%D0%B4%D0%B8%20%D0%BA%D0%B2%D0%B0%D0%B4%D1%80%D0%B0%D1%82%D0%B0&path=yandex_search&parent-reqid=1728573742179731-10995364852978495184-balancer-l7leveler-kubr-yp-klg-54-BAL&from_type=vast))

## Perimeter
- Circle: P = 2πR (см. [Формула длины окружности](https://yandex.by/video/preview/13710253640718718517?text=%D0%B4%D0%BE%D0%BA%D0%B0%D0%B7%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D1%81%D1%82%D0%B2%D0%BE%20%D1%84%D0%BE%D1%80%D0%BC%D1%83%D0%BB%D1%8B%20%D0%BF%D0%B5%D1%80%D0%B8%D0%BC%D0%B5%D1%82%D1%80%D0%B0%20%D0%BA%D1%80%D1%83%D0%B3%D0%B0&path=yandex_search&parent-reqid=1728574530764429-10222003799735677270-balancer-l7leveler-kubr-yp-klg-54-BAL&from_type=vast))
- Rectangle: P = 2a + 2b (см. [Формула периметра прямоугольника](https://yandex.by/video/preview/10046918671315005715?text=%D0%B4%D0%BE%D0%BA%D0%B0%D0%B7%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D1%81%D1%82%D0%B2%D0%BE%20%D1%84%D0%BE%D1%80%D0%BC%D1%83%D0%BB%D1%8B%20%D0%BF%D0%B5%D1%80%D0%B8%D0%BC%D0%B5%D1%82%D1%80%D0%B0%20%D0%BF%D1%80%D1%8F%D0%BC%D0%BE%D1%83%D0%B3%D0%BE%D0%BB%D1%8C%D0%BD%D0%B8%D0%BA%D0%B0&path=yandex_search&parent-reqid=1728574617604010-4921237565256832813-balancer-l7leveler-kubr-yp-klg-54-BAL&from_type=vast))
- Square: P = 4a (см. [Формула периметра квадрата](https://yandex.by/video/preview/10665490490445280431?text=%D0%B4%D0%BE%D0%BA%D0%B0%D0%B7%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D1%81%D1%82%D0%B2%D0%BE%20%D1%84%D0%BE%D1%80%D0%BC%D1%83%D0%BB%D1%8B%20%D0%BF%D0%B5%D1%80%D0%B8%D0%BC%D0%B5%D1%82%D1%80%D0%B0%20%D0%BA%D0%B2%D0%B0%D0%B4%D1%80%D0%B0%D1%82%D0%B0&path=yandex_search&parent-reqid=1728574676975580-11879877817701308951-balancer-l7leveler-kubr-yp-klg-54-BAL&from_type=vast))
## Функции
### 1.Нахождение площади круга
```
def area(r):
    return math.pi * r * r
   ```
Используя формулу площади круга (см. выше) находим площадь круга
##### Пример:
area(5) = 78.53981633974483
### 2.Нахождение длины окружности
```
def perimeter(r):
    return 2 * math.pi * r
   ```
Используя формулу длины окружности (см. выше) находим длину окружности
##### Пример:
perimeter(3346457) = 6692914.999999999
### 3.Нахождение площади квадрата
```
def area(a):
    return a * a
   ```
Используя формулу площади квадрата (см. выше) находим площадь квадрата
##### Пример:
area(5) = 25
### 4.Нахождение периметра квадрата
```
def perimeter(a):
    return 4 * a
```    
Используя формулу периметра квадрата (см. выше) находим периметр квадрата
##### Пример:
perimeter(500000000000) = 2000000000000

## История коммитов
- 8ba9aeb
