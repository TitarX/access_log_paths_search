import sys
import re
from pathlib import Path

root_path = ''
if len(sys.argv) > 1:
    root_path = sys.argv[1]
else:
    sys.exit()

if not Path(root_path).exists():
    sys.exit()

path_regex = re.compile(r'\d]\s"[A-Z]{3,7}\s(/[^\s]+?)\s')

result_file_path = Path(__file__).parent
result_file_path = '%s/result.txt' % result_file_path
result_file_path = Path(result_file_path)
result_file = open(result_file_path, 'w')
result_file.write('')
result_file.close()

result_list = []

log_file_path = Path(__file__).parent
log_file_path = '%s/access.log' % log_file_path
log_file_path = Path(log_file_path)
if log_file_path.exists():
    log_file = open(log_file_path, 'r')
    for line in log_file:
        path_search_result = path_regex.search(line)
        if path_search_result is not None:
            path = Path(root_path + path_search_result.group(1))
            if path.exists() and not path_search_result.group(1) in result_list:
                result_list.append(path_search_result.group(1))
    log_file.close()

    result_list.sort()
    # print(*result_list, sep='\n')

    result_file = open(result_file_path, 'a')
    for path_string in result_list:
        result_file.write(path_string)
        result_file.write('\n')
    result_file.close()
