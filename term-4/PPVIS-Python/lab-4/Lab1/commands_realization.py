import os


class Commands_realization:

    def clear_file(self, file_name, path):
        os.chdir(path=path)
        open(file_name, 'w').close()

    def delete_file(self, file_name, path):
        os.chdir(path=path)
        os.remove(str(file_name))

    def create_file(self, file_name, path):
        os.chdir(path=path)
        file = open(str(file_name), "w")
        file.close()

    def overwrite_file(self, file_name, path):
        os.chdir(path=path)
        file = open(str(file_name), "w")
        file.write(str(input()))
        file.close()

    def add_data_to_end(self, file_name, path):
        os.chdir(path=path)
        file = open(str(file_name), "a")
        file.write(str(input()))
        file.close()

    def view_file_data(self, file_name, path):
        os.chdir(path=path)
        file = open(str(file_name), "r")
        print(file.read())
        file.close()
