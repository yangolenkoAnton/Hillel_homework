import codecs
import re


def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()
    cleaned = re.sub(r'<[^>]*>', '', html)
    lines = cleaned.split('\n')
    non_empty_lines = []
    for line in lines:
        stripped_line = line.strip()
        if stripped_line:
            non_empty_lines.append(stripped_line)
    with codecs.open(result_file, 'w', 'utf-8') as file:
        file.write('\n'.join(non_empty_lines))
delete_html_tags('/mnt/user-data/uploads/draft.html', 'cleaned_result.txt')
with open('cleaned_result.txt', 'r', encoding='utf-8') as f:
    print(f.read())