# Стандартные ячейки

Библиотека стандартных ячеек, применяемых в PSG.

Стандартные ячейки используют группу симметрии S2 (налево-направо + флип).

Пока не понятно что за ячейки, просто собираем зоопарк. Только кодовые имена. Как будет содрана "шкура" с чипа, можно будет делать схемы ячеек.

## Ячейка 1 - not

|![image](https://user-images.githubusercontent.com/5828819/175828155-b9515f2e-2b66-4da4-86f1-a14564c949ac.png)|![image](https://user-images.githubusercontent.com/5828819/175999883-90b013b2-fc58-4027-9236-9763d79340f4.png)|
|---|---|

## Ячейка 2 - nand

|![image](https://user-images.githubusercontent.com/5828819/175828162-69dcf454-e27e-4bb9-aa23-9b45bb4da4f8.png)|![image](https://user-images.githubusercontent.com/5828819/175999920-ba876784-3b6e-4314-ab34-8da8cb6cd6b2.png)|
|---|---|

## Ячейка 3 - "99% not"

![image](https://user-images.githubusercontent.com/5828819/175828185-c3d8d309-6e06-4d31-9407-ce7882585c71.png)

## Ячейка 4 - 3-nand

|![image](https://user-images.githubusercontent.com/5828819/175828193-f8cd0cd6-c3d2-421a-b0d5-5c432deee133.png)|![image](https://user-images.githubusercontent.com/5828819/176125415-f76623ef-382e-403c-807a-b7bc2bb4f5f4.png)|![image](https://user-images.githubusercontent.com/5828819/176121734-2aa7369c-96d0-4490-bcc4-e194179e0b00.png)|
|---|---|---|

## Ячейка 5 - "99% DFF"

![image](https://user-images.githubusercontent.com/5828819/175957768-2fb18bf3-0f28-4936-ae84-23d2bfefcf88.png)

## Ячейка 6 - "писюн + ворота"

![image](https://user-images.githubusercontent.com/5828819/175828255-fcc3b21d-1581-41ae-8568-4f52225abaf9.png)

## Ячейка 7 - or

|![image](https://user-images.githubusercontent.com/5828819/175828343-ca770b7b-c711-4926-9c7d-ecec5fb66e1b.png)|![image](https://user-images.githubusercontent.com/5828819/176018358-e445fd72-a8ca-4356-9f05-3e22aa7e1689.png)|
|---|---|

## Ячейка 8 - notif0

Управляемый инвертор с инверсным управлением.

|![image](https://user-images.githubusercontent.com/5828819/175957964-541661c6-e339-40c5-a8da-9e1b2a712aab.png)|![image](https://user-images.githubusercontent.com/5828819/176018237-bffd9aed-79f7-4be7-835f-edf27a565b64.png)|![image](https://user-images.githubusercontent.com/5828819/176018267-0b7643de-d56e-43f9-88f1-686f33d86382.png)|![image](https://user-images.githubusercontent.com/5828819/176018287-d56c1a19-cee0-4df7-8e19-1636e6f89323.png)|
|---|---|---|---|

## Ячейка 9 - "большая 2"

![image](https://user-images.githubusercontent.com/5828819/175958669-7aa6f479-e25a-481c-abe2-32311ec462e9.png)

## Ячейка 10 - SRBit

Разряд регистра сдвига. Дикая магия CMOS. Если убрать P-MOS часть, то ячейка принимает знакомый вид N-MOS разряда сдвигателя:

![image](https://user-images.githubusercontent.com/5828819/176033538-51ae5998-eaa3-4a6f-afd0-77f932a2fa79.png)

|![image](https://user-images.githubusercontent.com/5828819/175828434-def8dd3c-53b6-4d24-a516-ee5cc95f0329.png)|![image](https://user-images.githubusercontent.com/5828819/176033676-29be2ee5-71db-433f-bd14-1f58dde82434.png)|![image](https://user-images.githubusercontent.com/5828819/176033844-dfea478a-1031-477b-9ae1-519eba22c462.png)|
|---|---|---|

Анализ работы:

![image](https://user-images.githubusercontent.com/5828819/176033609-a2666229-4ae3-45be-bd83-4faa5e3da96f.png)

Ещё поли:

![image](https://user-images.githubusercontent.com/5828819/176114115-4355ba98-e814-454e-9c3f-baf2cafca8f8.png)

После получения поли стало понятно что верхняя часть не соединяется с VDD (как видно там обрубок), в остальном угадали. Есть предположение, что в неокрепших умах инженеров YAMAHA всё ещё витали мечты о N-MOS защёлках на затворных емкостях. Сейчас использовать емкость на затворах в CMOS считается моветоном и используют обычные FF на двух инверторах или норах.

## Ячейка 11 - "ещё такая"

![image](https://user-images.githubusercontent.com/5828819/175959809-c1862af9-696c-46fe-9019-12709208eeb8.png)

## Ячейка 12 - "среднее месиво"

![image](https://user-images.githubusercontent.com/5828819/175828469-cc7eb04a-b432-42e6-9993-2a5ab3a4f7a3.png)

## Ячейка 13 - "телега"

![image](https://user-images.githubusercontent.com/5828819/175828496-8fb2ec44-639f-4f8a-8e6e-b1a8025b9a3d.png)

## Ячейка 14

![image](https://user-images.githubusercontent.com/5828819/175828573-7624076a-974f-4a9d-925d-074ff6fd7563.png)

Пока в единственном экземпляре (нижний левый угол).

## Ячейка 15

![image](https://user-images.githubusercontent.com/5828819/175828586-a9f2d510-197e-467b-a42a-39891fc2ff49.png)

Пока в единственном экземпляре (нижний левый угол). Немного отличается от Ячейки 14.

## Ячейка 16 - "C"

![image](https://user-images.githubusercontent.com/5828819/175958334-d19d87ae-733f-43b7-aa7c-a20700d82527.png)

## Ячейка 17 - "длинный чел"

![image](https://user-images.githubusercontent.com/5828819/175958473-c3b2788c-d1af-4d75-8925-04c54ab030c2.png)

## Ячейка 18 - "большая 3"

![image](https://user-images.githubusercontent.com/5828819/175959078-5cf9f231-baaa-4a33-add7-f35cdb7e9b32.png)

## Ячейка 19

![image](https://user-images.githubusercontent.com/5828819/175959384-6d79e735-510f-4cd9-a2bb-2bce819033a5.png)

В единственном экземпляре в правом нижнем углу.

## Ячейка 20 - "мощный писюн"

![image](https://user-images.githubusercontent.com/5828819/175965602-246a1d11-7b25-4778-815f-2e8ef21c58b4.png)

В единственном экземпляре в правом верхнем углу.

## Ячейка 21 - "дошик"

![image](https://user-images.githubusercontent.com/5828819/176142680-64b77b8c-6504-4125-8328-b580dd110bef.png)

Встречается в ряду `G`.

## Ячейка 22 - "xor?"

![image](https://user-images.githubusercontent.com/5828819/176143304-03e4979f-e4ea-472a-bd6b-024e2db7229c.png)

В единственном экземпляре, по сердеине ряда `G`.
