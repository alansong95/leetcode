import sys
import os
name = sys.argv[1:]
name = ' '.join(name)

name = name.replace('.', '').lower()
name_list = name.split(' ')

file_name = '_'.join(name_list)
file_name += '.py'

f = open(file_name, 'a')
f.write('solution = Solution()\nprint(solution.')
f.close()

print('file: ' + file_name + ' created successfully.')