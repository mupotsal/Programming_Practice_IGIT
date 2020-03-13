def write_to_file():
    my_new_file = open("myfile.txt","w")
    for i in range(10):
        statement = input("What do you want to say? \n")
        my_new_file.write(statement)
    my_new_file.close()

def read_from_file():
    my_new_handle = open("/Users/mupotsal/Desktop/ACADEMICS/Sophomore_second_semester/Computer Science Resources/Resumes_2019/dropbox_resume.txt","wb")
    while True:
        the_liine = my_new_handle.readline()
        print(the_liine)
        if len(the_liine)==0:
            break

    my_new_handle.close()
write_to_file()