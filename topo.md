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

## Карта ячеек по рядам

TBD: Ещё не все ячейки зареверсили, поэтому будут уточнения.

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
