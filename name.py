import sys
import os
name = sys.argv[1:]
name = ' '.join(name)

name = name.replace('.', '').lower()
name_list = name.split(' ')

dir_name = '_'.join(name_list)
file_name = '_'.join(name_list[1:])
file_name += '.py'

os.makedirs(dir_name)
f = open(dir_name + '/' + file_name, 'a')
f.write('solution = Solution()\nprint(solution.')
f.close()

print('file: ' + file_name + ' created successfully.')