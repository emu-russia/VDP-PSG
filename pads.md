# Контакты

На изучаемом ошмётке VDP кроме аналоговых выходов PSG просматриваются идентичные схемы следующих контактов:
- Контакт с 1 портом (двух видов, различаются от Input / Output)
- Контакт с 2 портами (Inout)
- Контакт с 3 портами (Inout + TriState)

Понятно что у всех контактов группа симметрии S4 (вращение на произвольный угол в 90° и флип).

TBD: Пока без схематики, просто коллекция картинок.

## Порты рядом с PSG

![PSG_Pads](/imgstore/PSG_Pads.png)

## Терминал Input

![image](https://user-images.githubusercontent.com/5828819/175827693-8ca7febe-4233-4f3e-8266-8d5e6087e2ec.png)

## Терминал Output

![image](https://user-images.githubusercontent.com/5828819/177574039-d237de48-ed87-4b40-8b99-d4b56eced7de.png)

## Терминал Inout

Для обычных двунаправленных I/O портов.

![image](https://user-images.githubusercontent.com/5828819/175827798-973f8c91-4d2e-4cb9-9d5c-150d283a7a7b.png)

## Терминал Inout+TriState

Используется для шин, которые могут находится в третьем состоянии (`z`).

![image](https://user-images.githubusercontent.com/5828819/175827664-34e516d7-6bf2-417b-9c40-caddacd6148e.png)
