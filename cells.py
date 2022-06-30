"""
	Скрипт для автоматических операций с ячейками.

	Нетлист предполагает горизонтальное размещение ячеек.

	TBD: Добавить вариант вертикального размещения (PSXCPU).
	
"""

import os
import sys
import argparse
import json
import xml.etree.ElementTree as ET


"""
	Процессинг десериализованного XML по рядам ячеек.
"""
def ProcessCells (op, cells, netlist):
	# Для всех ячеек:

	TopMin = 0
	row_num = 0
	total_cells = 0

	found = True
	while found:
		row = []
		count = 0
		found = False

		# Найти все ячейки в нетлисте выше TopMin и:
		#	- Получить самую верхнюю ячейку - это будет начало ряда
		#   - Получить её высоту
		# 	- Если что-то нашлось - это будет следующий ряд, обработать его в соответствии с массовой операцией. Если не нашлось - выйти.		

		TopY = float("inf")
		TopCell = None

		for entity in netlist:
			entityType = entity.find('Type').text
			y = float(entity.find('LambdaY').text)
			if entityType.startswith('Cell'):
				if y < TopY and y > TopMin:
					TopY = y
					TopCell = entity
					found = True

		if not found:
			break

		height = float(TopCell.find('LambdaHeight').text)
		Gap = height / 2

		# Выбрать ячейки y >= TopMin && y <= (TopY+height+Gap)

		for entity in netlist:
			entityType = entity.find('Type').text
			y = float(entity.find('LambdaY').text)
			if entityType.startswith('Cell'):
				if y >= TopMin and y < (TopY+height+Gap):
					row.append(entity)
					count = count + 1

		# Сортировать по X по возрастанию

		row = sorted(row, key=lambda child: float(child.find('LambdaX').text) )

		if count:
			if op == 'add_names':
				AddNames (cells, row, row_num)
			elif op == 'rem_names':
				RemNames (cells, row, row_num)
			elif op == 'classify':
				Classify (cells, row, row_num)
			elif op == 'unclassify':
				Unclassify (cells, row, row_num)
			elif op == 'add_ports':
				AddPorts (cells, row, row_num)
			elif op == 'rem_ports':
				RemPorts (cells, row, row_num)
			elif op == 'count':
				total_cells = total_cells + CountByRow (cells, row, row_num)

		TopMin = TopY + height
		row_num = row_num + 1

	if op == 'count':
		print ("Total cells: " + str(total_cells))
"""
	ProcessCells end.
"""


def AddNames(cells, row, row_num):
	row_name = cells['map']['row_names'][row_num]
	cell_num = 0
	for entity in row:
		cell_name = cells['map']['rows'][row_num][cell_num]
		entity.find('Label').text = row_name + str(cell_num) + "-" + cell_name
		cell_num = cell_num + 1


def RemNames(cells, row, row_num):
	for entity in row:
		entity.find('Label').text = None


def Classify(cells, row, row_num):
	return


def Unclassify(cells, row, row_num):
	for entity in row:
		entity.find('Type').text = 'CellOther'


def AddPorts(cells, row, row_num):
	return


def RemPorts(cells, row, row_num):
	return


def CountByRow(cells, row, row_num):
	count = len(row)
	print ("row " + str(row_num) + ", cells: " + str(count))
	return count


"""
	Десериализовать JSON и XML. Сделать процессинг выбранной операции. Сериализовать XML в новый файл (выходной результат)
"""
def Main(args):
	with open(args.json_file, mode='r', encoding='UTF8') as f:
		text = f.read()
		cells = json.loads(text)
	netlist = ET.parse(args.xml_file)
	ProcessCells (args.operation, cells, netlist.getroot())
	out_xml = open("out.xml", "wb")
	xml_text = ET.tostring(netlist.getroot(), method='xml')
	out_xml.write(xml_text)
	out_xml.close()


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Для продолжения укажите одну из операций: count (посчитать по рядам), add_names (добавить имена), rem_names (удалить имена), classify (задать типы), unclassify (удалить типы), add_ports (добавить порты), rem_ports (удалить порты)')
	parser.add_argument('--op', dest='operation', help='Операция над ячейками.')
	parser.add_argument('--json', dest='json_file', help='JSON с определениями ячеек')
	parser.add_argument('--xml', dest='xml_file', help='XML файл из Deroute с нетлистом')
	Main(parser.parse_args())
