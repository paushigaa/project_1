import csv
def write_csv(stu_info):
    with open('student_info.csv','a',newline='') as csv_file:
        writer=csv.writer(csv_file)
        if csv_file.tell()==0:
            writer.writerow(["Name","Age","Contact_no","Email Id"])
        writer.writerow(stu_info)
if __name__=='__main__':
    condition=True
    stu_no=1
    while(condition):
        student_info=input("enter (name, age, contact number, email id) for student #{}: ".format(stu_no))
        student_info_list=student_info.split(' ')
        print("\nName: {}\nAge: {}\nContact number: {}\nEmail ID: {}".format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
        check=input("Is the given information is correct (yes/no)? : ")
        if check=='yes':
            write_csv(student_info_list)
            condition_check=input("do you want to enter info of another student (yes/no)? : ")
        
            if condition_check=='yes':
                condition=True
                stu_no=stu_no+1
            elif condition_check=='no':
                condition=False
                print("Thankyou!")
        elif check=='no':
            print("\nPlease re-enter the student information")
