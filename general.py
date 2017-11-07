import os

#1.to create a directory
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating Project...')
        os.mkdir(directory)

#2.to create files of queue and crawled(if not created)
def create_data_files(project_name , base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):               #does this file exist already???
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')

#3.create a new file
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()

#4.add data onto an existing file
def append_to_file(path, data):
    file = open(path, 'a')
    file.write(data + '\n')
    file.close()

#5.deleting the content of a file
def delete_file_contents(path):
    f = open(path, 'w')
    f.close()

#6.read a file and converts the links to a set
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results

#7.iterate thru the set, each item in the set will be a new line in the file
def set_to_file(links, file):
    delete_file_contents(file)
    for link in sorted(links):
        append_to_file(file, link)
