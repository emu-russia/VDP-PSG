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

![image](https://user-images.githubusercontent.com/5828819/176447287-aeaba731-4815-466c-9ff1-083305dc2a16.png)

## Карта ячеек по рядам

TBD: Ещё не все ячейки зареверсили, поэтому будут уточнения.

Исходный файл см. cells.json.

```json
"rows":
[
	[
		"not", "nand", "nand", "Cell3", "Cell3", "Cell3",
		"nand3", "nand3", "nand3", "nand3", "nand3", "nand3", "nand3", "nand3", 
		"not", "nand", "nand", "Cell3", "Cell3", "Cell3", 
		"nand3", "nand3", "nand3", "nand3", "nand3", "nand3", "nand3", "nand3", 
		"not", "nand", "nand", "Cell3", "Cell3", "Cell3", 
		"nand3", "nand3", "nand3", "nand3", "nand3", "nand3", "nand3", "nand3", 
		"not", "nand", "nand", "Cell3", "Cell3", "Cell3", 
		"nand3", "nand3", "nand3", "nand3", "nand3", "nand3", "nand3", "nand3"
	],

	[
		"notif0", "or", "dlatch", "notif0", "or", "dlatch", "notif0", "or", "dlatch", "notif0", "or", "dlatch", "comp",
		"notif0", "or", "dlatch", "notif0", "or", "dlatch", "notif0", "or", "dlatch", "notif0", "or", "dlatch", "comp",
		"notif0", "or", "dlatch", "notif0", "or", "dlatch", "notif0", "or", "dlatch", "notif0", "or", "dlatch", "comp",
		"notif0", "or", "dlatch", "notif0", "or", "dlatch", "notif0", "or", "dlatch", "notif0", "or", "dlatch", "comp", "Cell20"
	],

	[
		"dlatch", "or", "or", "comp", "dlatch", "or", "dlatch", "dlatch", "or", "dlatch", "dlatch", "or", "dlatch", "dlatch", "or", "or", "not",
		"dlatch", "or", "or", "dlatch", "or", "or", "dlatch", "or", "or", "comp",
		"not", "aoi21", "and3", "not", "aoi21", "and3", "or", "not", "or", "or", "not", "aoi21", "and3", "or", "or",
		"not", "aoi21", "and3", "not", "aoi21", "and3", "or", "or", "not", "aoi21", "and3",
		"and3", "aoi21", "not", "and3", "aoi21", "not", "not", "not", "not", "not", "nand", "nand", "nand", "nand"
	],

	[
		"dlatch", "dlatch", "dlatch", "dlatch", "dlatch", "dlatch", "dlatch", "dlatch", "dlatch", "dlatch", "dlatch", "dlatch", "dlatch", "dlatch", "dlatch", "dlatch", "dlatch", "dlatch",
		"comp", "comp", "comp",
		"dlatch", "dlatch", "dlatch", "dlatch", "dlatch", "dlatch", "dlatch", "dlatch", "dlatch", "dlatch", "dlatch", "dlatch",
		"comp", "comp", "comp",
		"or", "or", "or", "or", "dlatch", "dlatch", "dlatch", "comp"
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
		"or", "Cell21", "or", "Cell21", "or", "Cell21", "or", "Cell21", "or", "Cell21", "or", "Cell21", "or", "Cell21", "or", "Cell21", "or", "Cell21", "or", "Cell21",
		"xor",
		"lfsr_bit", "lfsr_bit", "lfsr_bit", "lfsr_bit", "lfsr_bit", "lfsr_bit", "lfsr_bit", "lfsr_bit", "lfsr_bit", "lfsr_bit", "lfsr_bit", "lfsr_bit", "lfsr_bit", "lfsr_bit", "lfsr_bit", "lfsr_bit",
		"nand", "nand", "nand3"
	],

	[
		"not", "Cell14_15", "Cell11",
		"sr_bit", "not", "or", "nand", "sr_bit", "Cell18", "Cell23", "not", "nand",
		"buf", "not", "buf", "nand", "not", "buf", "buf", 
		"rs", "nand", "Cell11", "sr_bit", "Cell11", "not", "Cell20", "nand3",
		"rs", "Cell11", "nand", "not", "nand", "Cell20", "Cell20", "nand", "nand3", "or", "not", "sr_bit", "Cell19",
		"not", "nand", "or", "not", "nand", "or", "not", "nand", "or", "nand", "or"
	]
]
```
