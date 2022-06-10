import os, shutil
#пофиксить path

class Storage:
    def __init__(self, size, computer_name, operation_systems, users,
    path = '/home/siarhei/Programming/IIT/Univer/ППвИС/Computers_data'):
        self.path_to_comp = (path + '/' + computer_name)
        self.storage_size = size
        self.user_storage_size = int(size*0.7)
        self.system_storage_size = int(size*0.3)
        
        if os.path.exists(self.path_to_comp)!=True:
            os.chdir(path=path)
            os.mkdir(self.path_to_comp)
            
            for i in operation_systems:
                os.chdir(self.path_to_comp) #заходим в папку компа

                os.mkdir(i._get_system_type())
                os.chdir(self.path_to_comp+'/'+str(i._get_system_type()))# в папку операционки

                os.mkdir('System_storage')
                os.chdir((self.path_to_comp+'/'+str(i._get_system_type())+'/System_storage'))# /операционка/System_storage

                writing_commands_to_storage = open('Commands_and_descriptions.txt', 'w')
                writing_commands_to_storage.write(str(i._get_system_type())) # записываем команды
                self.system_storage_size -= 1
                
                os.chdir(self.path_to_comp+'/'+str(i._get_system_type()))
                os.mkdir('User_storage') # операционка + User_strorage

                if i._get_system_type() == users[0].get_operation_system_type():
                    os.chdir((self.path_to_comp+'/'+str(i._get_system_type())+'/System_storage'))
                    os.mkdir(users[0].get_login()) # операционка/System_storage + Login
                    os.chdir((self.path_to_comp+'/'+str(i._get_system_type())+'/System_storage/'+users[0].get_login()))#
                    writing_user_info_to_storage = open('User_info.txt','w')
                    writing_user_info_to_storage.write(str(users[0].get_all_user_info()))
                    self.system_storage_size -= 1

                    os.chdir(self.path_to_comp+'/'+str(i._get_system_type())+'/User_storage')
                    os.mkdir(users[0].get_login())


    def get_all_storage_info(self):
        return {self.storage_size:' storage size.',
                self.system_storage_size : ' free system memory.',
                self.user_storage_size :' free user memory'}
    
    def get_storage_size(self):
        return self.storage_size

    def get_free_system_storage_size(self):
        return self.system_storage_size

    def get_free_user_storage_size(self):
        return self.user_storage_size


    def __clear_user_s_storage(self, user):
        folder = self.path_to_comp+'/'+str(user.get_operation_system_type())+'/User_storage/'+str(user.get_login())
        for the_file in os.listdir(folder):
            file_path = os.path.join(folder, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path): shutil.rmtree(file_path)
            except Exception as e:
                print(e)
        os.rmdir(folder)
        self.user_storage_size = self.storage_size*0.7

    def __clear_user_s_system_storage(self, user):
        folder = self.path_to_comp+'/'+str(user.get_operation_system_type())+'/System_storage/'+str(user.get_login())
        for the_file in os.listdir(folder):
            file_path = os.path.join(folder, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path): shutil.rmtree(file_path)
            except Exception as e:
                print(e)
        os.rmdir(folder)
        self.system_storage_size = self.storage_size*0.3


    def _add_new_user_directory(self,user):
        if os.path.exists(self.path_to_comp+'/'+str(user.get_operation_system_type())+'/System_storage/'+str(user.get_login()))!=True:
            path_to_user_syst = self.path_to_comp+'/'+str(user.get_operation_system_type())
            user_login = user.get_login()

            os.chdir(path_to_user_syst+'/System_storage')
            os.mkdir(str(user_login))
            os.chdir(path_to_user_syst+'/System_storage/'+str(user_login)+'/')#
            writing_user_info_to_storage = open('User_info.txt','w')
            writing_user_info_to_storage.write(str(user.get_all_user_info()))

            os.chdir(path_to_user_syst+'/User_storage')
            os.mkdir(str(user_login))


    def _delete_user(self, user):
        self.__clear_user_s_storage(user)
        self.__clear_user_s_system_storage(user)
