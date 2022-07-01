# Заметки по топологии

Ячейки расставляли и соединяли проводами вручную. Фиттер так не расставит красиво и роутер не соединит.

![image](https://user-images.githubusercontent.com/5828819/175983109-d13f8b43-3bb9-4e85-842e-b8bf61fdd92b.png)

Это человек делал.

![image](https://user-images.githubusercontent.com/5828819/175983175-84c133a4-d846-4451-81fe-b535a47a4efd.png)

И ячейки уложены модульно (что собсно у @nukeykt на картинках видно - каунтер отдельно, регистры отдельно и проч.)

VDP - CMOS с одним слоем металла.

![image](https://user-images.githubusercontent.com/5828819/175983002-4df8cd5c-90a1-49fe-9fc4-dbe16c287375.png)

https://www.icreversing.com/chips/315-5313a

Ещё одной необычной особенностью является использование n-карманов, вместо привычных p:

![image](https://user-images.githubusercontent.com/5828819/176116906-edc63b0e-4829-4dec-9c4e-634e062aece4.png)

При реверсе не стоит на это обращать внимание. Там где земля - с той стороны N-трансы, там где VDD - с той стороны P-трансы, обычные правила для CMOS.

## Модули

Карта распределения ячеек по модулям, by @nukeykt.

![image](https://user-images.githubusercontent.com/5828819/176502964-95bc5798-02ce-4933-ac8c-da426f77f7a4.png)

## Группа самосовмещений ячеек

В некоторых местах встречается такое (земля снизу):

![image](https://user-images.githubusercontent.com/5828819/176856526-86d02e64-7d99-4f38-9a79-cd850feba478.png)

Казалось бы это две ячейки `or`, но нет.

Группа самосовмещений (ячейка `or`):

|ident (земля снизу)|rot (земля сверху)|flip_h (земля снизу)|rot+flip_h (земля сверху|
|---|---|---|---|
|![image](https://user-images.githubusercontent.com/5828819/176852861-7d7a0f57-d302-4f71-bd27-1cea605fb091.png)|![image](https://user-images.githubusercontent.com/5828819/176852945-8082ee45-692c-42dc-92d7-c90748a3aae1.png)|![image](https://user-images.githubusercontent.com/5828819/176853301-54b26e7c-8166-430b-9e86-bc5045b9614b.png)|![image](https://user-images.githubusercontent.com/5828819/176857460-1020e86c-4dcd-4f58-824e-76e226a66e25.png)|

Т.е. понятно что ячейка не может быть повернута вверх (т.к. они уложены рядами) и не может быть флипнута вертикально (снизу-вверх), т.к. в этом случае мы получаем картину, что была показана вначале.

Ячейка `or` флипнутая по вертикали меняет N и P транзисторы, оставляя землю, поэтому становится ячейкой `and`.

Поэтому у ячейки `and` будет такая группа самосовмещений:

|ident (земля снизу)|rot (земля сверху)|flip_h (земля снизу)|rot+flip_h (земля сверху)|
|---|---|---|---|
|![image](https://user-images.githubusercontent.com/5828819/176853681-b5759600-34d0-4bc9-be78-0f6d9d245eaa.png)|![image](https://user-images.githubusercontent.com/5828819/176853715-74e3c938-3f99-410f-bbf8-6dd91cbcbb9e.png)|![image](https://user-images.githubusercontent.com/5828819/176853767-57d5a1f7-5c1b-4c51-b9e7-fd7c9e5a4074.png)|![image](https://user-images.githubusercontent.com/5828819/176857641-2b40c1dc-3858-439d-addf-e99a83b466ba.png)|

Не все ячейки позволяют такие фокусы, а только комплементарно симметричные, типа nor / nand, or / and.

Группа самосовмещений ячеек является простейшей группой диэдра D2 (`Vierergruppe`).

![image](https://user-images.githubusercontent.com/5828819/176861596-9f27ad7b-82f0-4c9a-888c-5250f60a61ae.png)

## Карта ячеек по рядам

Исходный файл см. cells.json.

![image](https://user-images.githubusercontent.com/5828819/176867463-cb188394-577d-4608-badc-3babf42d162a.png)
