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

|ident (земля снизу)|rot (земля сверху)|flip_h (земля снизу)|
|---|---|---|
|![image](https://user-images.githubusercontent.com/5828819/176853681-b5759600-34d0-4bc9-be78-0f6d9d245eaa.png)|![image](https://user-images.githubusercontent.com/5828819/176853715-74e3c938-3f99-410f-bbf8-6dd91cbcbb9e.png)|![image](https://user-images.githubusercontent.com/5828819/176853767-57d5a1f7-5c1b-4c51-b9e7-fd7c9e5a4074.png)|

Не все ячейки позволяют такие фокусы, а только комплементарно симметричные, типа nor / nand, or / and.

## Карта ячеек по рядам

Исходный файл см. cells.json.

```json
"rows":
[
	[
		"not", "nand", "nand", "comp_weak", "comp_weak", "comp_weak",
		"nand3", "nand3", "nand3", "nand3", "nand3", "nand3", "nand3", "nand3", 
		"not", "nand", "nand", "comp_weak", "comp_weak", "comp_weak", 
		"nand3", "nand3", "nand3", "nand3", "nand3", "nand3", "nand3", "nand3", 
		"not", "nand", "nand", "comp_weak", "comp_weak", "comp_weak", 
		"nand3", "nand3", "nand3", "nand3", "nand3", "nand3", "nand3", "nand3", 
		"not", "nand", "nand", "comp_weak", "comp_weak", "comp_weak", 
		"nand3", "nand3", "nand3", "nand3", "nand3", "nand3", "nand3", "nand3"
	],

	[
		"notif0", "or", "dlatch", "notif0", "or", "dlatch", "notif0", "or", "dlatch", "notif0", "or", "dlatch", "comp_strong",
		"notif0", "or", "dlatch", "notif0", "or", "dlatch", "notif0", "or", "dlatch", "notif0", "or", "dlatch", "comp_strong",
		"notif0", "or", "dlatch", "notif0", "or", "dlatch", "notif0", "or", "dlatch", "notif0", "or", "dlatch", "comp_strong",
		"notif0", "or", "dlatch", "notif0", "or", "dlatch", "notif0", "or", "dlatch", "notif0", "or", "dlatch", "comp_strong", "not_strong"
	],

	[
		"dlatch", "or", "or", "comp_strong", "dlatch", "or", "dlatch", "dlatch", "or", "dlatch", "dlatch", "or", "dlatch", "dlatch", "or", "or", "not",
		"dlatch", "or", "or", "dlatch", "or", "or", "dlatch", "or", "or", "comp_strong",
		"not", "aoi21", "and3", "not", "aoi21", "and3", "or", "not", "or", "or", "not", "aoi21", "and3", "or", "or",
		"not", "aoi21", "and3", "not", "aoi21", "and3", "or", "or", "not", "aoi21", "and3",
		"and3", "aoi21", "not", "and3", "aoi21", "not", "not", "not", "not", "not", "not", "nand", "nand", "nand", "nand"
	],

	[
		"dlatch", "dlatch", "dlatch", "dlatch", "dlatch", "dlatch", "dlatch", "dlatch", "dlatch", "dlatch", "dlatch", "dlatch", "dlatch", "dlatch", "dlatch", "dlatch", "dlatch", "dlatch",
		"comp_strong", "comp_strong", "comp_strong",
		"dlatch", "dlatch", "dlatch", "dlatch", "dlatch", "dlatch", "dlatch", "dlatch", "dlatch", "dlatch", "dlatch", "dlatch",
		"comp_strong", "comp_strong", "comp_strong",
		"or", "or", "or", "or", "dlatch", "dlatch", "dlatch", "comp_strong"
	],

	[
		"aon2222", "cgi2a", "aon2222", "cgi2a", "aon2222", "cgi2a", "aon2222", "cgi2a", "aon2222", "cgi2a", "aon2222", "cgi2a", "aon2222", "cgi2a", "aon2222", "cgi2a", "aon2222", "cgi2a", "aon2222", "cgi2a",
		"not", "nand", "sr_bit", "not", "nand", "sr_bit", "not", "nand", "sr_bit", "not", "nand", "sr_bit", "nand3", "not", "sr_bit", "sr_bit", "sr_bit", "sr_bit", "sr_bit"
	],

	[
		"sr_bit", "sr_bit", "sr_bit", "sr_bit", "sr_bit", "sr_bit", "sr_bit", "sr_bit", "sr_bit", "sr_bit",
		"sr_bit", "sr_bit", "sr_bit", "sr_bit", "sr_bit", "sr_bit", "sr_bit", "sr_bit", "sr_bit", "sr_bit",
		"sr_bit", "sr_bit", "sr_bit", "sr_bit", "sr_bit", "sr_bit", "sr_bit", "sr_bit", "sr_bit", "sr_bit",
		"sr_bit", "sr_bit", "sr_bit", "sr_bit", "sr_bit", "sr_bit", "sr_bit", "sr_bit", "sr_bit", "sr_bit",
		"nand", "or", "Cell18", "or", "Cell18", "or", "Cell18", "or", "Cell18", "nand3", "nand3", "not"
	],

	[
		"or", "ha", "or", "ha", "or", "ha", "or", "ha", "or", "ha", "or", "ha", "or", "ha", "or", "ha", "or", "ha", "or", "ha",
		"xor",
		"lfsr_bit", "lfsr_bit", "lfsr_bit", "lfsr_bit", "lfsr_bit", "lfsr_bit", "lfsr_bit", "lfsr_bit", "lfsr_bit", "lfsr_bit", "lfsr_bit", "lfsr_bit", "lfsr_bit", "lfsr_bit", "lfsr_bit", "lfsr_bit",
		"nand", "nand", "nand3"
	],

	[
		"not", "clkgen", "dff",
		"sr_bit", "not", "or", "nand", "sr_bit", "Cell18", "slatch_inv", "not", "nand",
		"buf", "not", "buf", "nand", "not", "buf", "buf", 
		"rs", "nand", "dff", "sr_bit", "dff", "not", "not_strong", "nand3",
		"rs", "dff", "nand", "not", "nand", "not_strong", "not_strong", "nand", "nand3", "or", "not", "sr_bit", "aon22",
		"not", "nand", "or", "not", "nand", "or", "not", "nand", "or", "nand", "or"
	]
]
```
