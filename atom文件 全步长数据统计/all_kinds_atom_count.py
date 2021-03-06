import linecache
import datetime
from copy import deepcopy
import csv
def all_kinds_atom_count():
	path = 'species.out'
	content = ''
	cache_data = linecache.getlines(path)
	for line in range(len(cache_data)):
	    content += cache_data[line].replace('# ','')
	f = open('middle_cache.out','w')
	f.write(content)
	f.close

	with open('middle_cache.out') as f:
		data_reader = csv.reader(f)
		data = list(data_reader)
	# data = linecache.getlines('middle_cache.out')
	odd_row_raw = data[::2]
	even_row_raw = data[1::2]
	# print(odd_row_raw)
	odd_row = []
	even_row = []
	for i,j in zip(even_row_raw,odd_row_raw):
	    even_row.append(i[0].strip().split())
	    odd_row.append(j[0].strip().split())
	# print(odd_row)
	formula = set()
	for i in odd_row:
	    for j in i[2:]:
	        formula.add(j)
	li = list(formula)
	li.sort()
	header = ['Timestep','No_Moles','No_Specs']
	new_column = header + li
	templet_dict = dict.fromkeys(new_column,'0') # 生成一个固定格式的字典以供写入，默认值为空
	a = ''
	for i in new_column:
	    a += ''.join('{%s} ' % i)
	templet_row = ','.join(a.rstrip().split())  # 生成一个固定的模板以供被写入行数据，逗号分隔

	b = ''
	for j in new_column:
	    b += j+','
	first_row = b.rstrip(',')  # 准备columns,用逗号分隔
	# 数据写入部分
	f = open('out.csv','w')
	f.write(first_row+'\n')
	for i,j in zip(odd_row,even_row):
	    tem_dict = dict(zip(i, j))
	#     print(tem_dict)
	    middle = deepcopy(templet_dict)                
	    for key,value in tem_dict.items():
	        middle[key] = value
	    w = templet_row.format(**middle)
	    f.write(w+'\n')
	f.close()

if __name__ == '__main__':
	start  = datetime.datetime.now()
	print('''Tips:Please Ensure that your "species.out" in the 
		   same floder with this script!This script will output a 
		   csv recorded all kinds of atom with thier account!''')
	all_kinds_atom_count()
	end = datetime.datetime.now()
	print('Converted Success!Time consumed：{}'.format((end - start)))