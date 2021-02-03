from copyx import copy
		
def main():
    baseDir = r'/home/data'
    targetDir = r'/home/dataCopy'
    dir_list = [r'abc', 
    r'ab/c', 
    r'a/bc']
    file_list = [
        r'a.txt',
        r'b.txt',
        r'c.txt']

    copy(baseDir, targetDir, dir_list, file_list)
    pass

if __name__ == '__main__':
    main()
    
