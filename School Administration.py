import csv


def writer_into_csv(splited_detail):
    with open('detail.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        if csv_file.tell() == 0:
            writer.writerow(["Name", "Age", "Contact_no", "E-mail"])

        writer.writerow(splited_detail)


if __name__ == '__main__':
    condition = True
    student_no = 1
    while condition:
        details = input("Enter the #{} students details in the following format(Name Age Number E-mail) : ".format(student_no))
        split_detail = details.split(' ')
        print("The entered student detail is:\nName :{}\nAge :{}\nContact_no :{}\nE-mail :{}"
              .format(split_detail[0], split_detail[1], split_detail[2], split_detail[3]))
        information_check = input("Is the entered information correct (yes/no) : ")
        info_check = information_check.upper()
        if info_check == "YES":
            writer_into_csv(split_detail)
            check = input("Enter (yes/no) if you want to enter information of other student : ")
            s_check = check.upper()
            if s_check == "YES":
                condition = True
                student_no += 1
            elif s_check == "NO":
                condition = False
        elif info_check == "NO":
            print("please re-enter the correct information!!!")
