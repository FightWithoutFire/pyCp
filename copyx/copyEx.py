import os,shutil

def copy(source_path, target_path, dir_list, file_list):
    for dir in dir_list:
        source_join_path = os.path.join(source_path, dir)
        target_join_path = os.path.join(target_path, dir)  
        # shutil.copytree(source_join_path, target_join_path)
        copy_dir(source_join_path, target_join_path)
    for file in file_list:
        source_join_path = os.path.join(source_path, file)
        target_join_path = os.path.join(target_path, file)  
        copy_file(source_join_path, target_join_path)
       

    pass

def copy_dir(source_path, target_path):
    dir_files = os.listdir(source_path)            
    for file in dir_files:
        source_join_path = os.path.join(source_path, file)
        target_join_path = os.path.join(target_path, file)
        if os.path.isfile(source_join_path):  
            # print("{} is file".format(source_join_path))         
            copy_file(source_path, target_path, file)
        if os.path.isdir(source_join_path): 
            # print("{} is dir".format(source_join_path))         
            mkdir(source_join_path)
            copy_dir(source_join_path, target_join_path)
    print("移动文件成功！")
    pass

def copy_file(source_path, target_path, file=''):
    # print(os.path.dirname(target_path))
    mkdir(os.path.dirname(target_path))
    if file != '':
        source_join_path = os.path.join(source_path, file)
        target_join_path = os.path.join(target_path, file)
        shutil.copy(source_join_path, target_join_path)
    else:
        shutil.copy(source_path, target_path)

    pass

def mkdir(path):
 
	folder = os.path.exists(path)
 
	if not folder:                   #判断是否存在文件夹如果不存在则创建为文件夹
		os.makedirs(path)            #makedirs 创建文件时如果路径不存在会创建这个路径
		print("---  new folder...  ---")
		print("---  OK  ---")
 
	else:
		print("---  There is this folder!  ---")
		

def main():
    pass

if __name__ == '__main__':
    main()
