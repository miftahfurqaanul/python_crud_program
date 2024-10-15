# ===================================
# [Your Program Title]
# ===================================
# Developed by. [Enter your name]
# JCDS - [Class Batch]


# /************************************/

# /===== Data Model =====/
# Create your data model here
# data = [] # Example data model
score_student_list={
    "NIS": [101,102,103,104,105],
    "name": ["Andi", "Andika","Anjani","andin","Anisa"],
    "gender": ["male", "male", "female","female","female"],
    "kelas": [10,11,12,10,11],
    "score": [90,80,70,80,85],
    "kejuruan":["IPA","IPS","BAHASA","IPA","IPA"],
    "mata pelajaran":["Matematika","Bahasa Indonesia","Bahasa Inggris","Biologi","Kimia"]
}

# /===== Feature Program =====/
# Create your feature program here
def show_score():
    while  True:
        print("\n\t\t===Show Score Student Menu ===")
        print("""
            1. Show All Score Students
            2. Search Student By NIS
            3. Back to Main Menu
            4. Detail Student
            """
        )
        user_input = input("Enter Your Choice: ")
        # 1. SHOW  ALL SCORE STUDENTS
        if  user_input == "1":
            print("Show Score Student")
            print("NIS   | nama siswa |  gender    |kejuruan    |  kelas |  mata pelajaran    |  score ")
            for i in range(len(score_student_list["name"])):
                print(f' {score_student_list["NIS"][i]:<4} | {score_student_list["name"][i]:<10} | {score_student_list["gender"][i]:<10} | {score_student_list["kejuruan"][i]:<10} | {score_student_list["kelas"][i]:<5}  | {score_student_list["mata pelajaran"][i]:<18} | {score_student_list["score"][i]:<10}  ')

        # 2. Search Student By NIS
        elif user_input ==  "2":
            search_nis = input("Enter NIS: ")
            for j in range(len(score_student_list["NIS"])):
                if score_student_list["NIS"][j] == int(search_nis):
                    print("NIS   | nama siswa |  gender    |kejuruan    |  kelas |  mata pelajaran    |  score ")
                    print(f' {score_student_list["NIS"][j]:<4} | {score_student_list["name"][j]:<10} | {score_student_list["gender"][j]:<10} | {score_student_list["kejuruan"][j]:<10} | {score_student_list["kelas"][j]:<5}  | {score_student_list["mata pelajaran"][j]:<18} | {score_student_list["score"][j]:<10}  ')
                    break
            else:
                print("Student Not Found")
                
        # 3 back to main menu
        elif user_input == "3":
            main()
        else:
            print("Invalid Input")
        # elif user_input == "2":
            return

def create_score():
    while  True:
        print("\n\t\t=== ADD STUDENT MENU ===")
        print("""
            1. Add Score Student
            2. Back to Main Menu
            """
        )
        user_input = input("Enter Your Choice: ")
        if user_input == "1" :
            new_nis =  int(input("Enter NIS: "))
            if  new_nis in score_student_list["NIS"]:
                print("NIS Already Exist")
            else:
                new_name = input("name : ")
                new_gender = input("gender : ")
                new_kejuruan = input("kejuruan : ")
                new_kelas = int(input("kelas  : "))
                new_mata_pelajaran = input("mata pelajaran : ")
                new_score = int(input("score : "))
                for j in range(len(score_student_list["NIS"])):
                    if score_student_list["NIS"][j] == int(new_nis):
                        print("NIS   | nama siswa |  gender    |kejuruan    |  kelas |  mata pelajaran    |  score ")
                        print(f' {score_student_list["NIS"][j]:<4} | {score_student_list["name"][j]:<10} | {score_student_list["gender"][j]:<10} | {score_student_list["kejuruan"][j]:<10} | {score_student_list["kelas"][j]:<5}  | {score_student_list["mata pelajaran"][j]:<18} | {score_student_list["score"][j]:<10}  ')
                saved = input("Apakah Anda Yakin Menyimpan Data Siswa ini ?  y/n ? ")
                if saved == "y":
                    score_student_list["NIS"].append(new_nis)
                    score_student_list["name"].append(new_name)
                    score_student_list["gender"].append(new_gender)
                    score_student_list["kelas"].append(new_kelas)
                    score_student_list["kejuruan"].append(new_kejuruan)
                    score_student_list["mata pelajaran"].append(new_mata_pelajaran)
                    score_student_list["score"].append(new_score)
                    print("Data Siswa Berhasil Disimpan")
                else:
                    print("Data  Siswa Tidak Disimpan")
        elif user_input == "2":
            main()
        else:
            print("Invalid Input")
    """Function for create the data
    """
    return

def update_score():
    while  True:
        print("\n\t\t=== Update STUDENT MENU ===")
        print("""
            1. Edit Score Student
            2. Back to Main Menu
            """
        )
        user_input = input("Enter Your Choice: ")
        if user_input == "1":
            new_nis = int(input("Enter NIS: "))
            if new_nis in score_student_list["NIS"]:
                for j in range(len(score_student_list["NIS"])):
                    if score_student_list["NIS"][j] == int(new_nis):
                        print("NIS   | nama siswa |  gender    |kejuruan    |  kelas |  mata pelajaran    |  score ")
                        print(f' {score_student_list["NIS"][j]:<4} | {score_student_list["name"][j]:<10} | {score_student_list["gender"][j]:<10} | {score_student_list["kejuruan"][j]:<10} | {score_student_list["kelas"][j]:<5}  | {score_student_list["mata pelajaran"][j]:<18} | {score_student_list["score"][j]:<10}  ')
                saved = input("Apakah Anda Yakin Menyimpan Data Siswa ini ?  y/n ")
                if saved == "y":
                    colom_change =  input("Colom Yang Mau diUbah : ")
                    if colom_change == "NIS" :
                        new_nis = int(input("Enter New NIS : "))
                        saved_change = input("Apakah Anda Serius Ingin Mengubahnya  ?  y/n ")
                        if saved_change == "y":
                            score_student_list["NIS"][score_student_list["NIS"].index(new_nis)] = new_nis
                    if colom_change == "gender" :
                        new_gender = input("Enter New gender : ")
                        saved_change = input("Apakah Anda Serius Ingin Mengubahnya  ?  y/n ")
                        if saved_change == "y":
                            score_student_list["gender"][score_student_list["NIS"].index(new_nis)] = new_gender
                    if colom_change == "kejuruan" :
                        new_kejuruan = input("Enter New kejuruan : ")
                        saved_change = input("Apakah Anda Serius Ingin Mengubahnya  ?  y/n ")
                        if saved_change == "y":
                            score_student_list["kejuruan"][score_student_list["NIS"].index(new_nis)] = new_kejuruan
                    if colom_change == "kelas" :
                        new_kelas = int(input("Enter New kelas : "))
                        saved_change = input("Apakah Anda Serius Ingin Mengubahnya  ?  y/n ")
                        if saved_change == "y":
                            score_student_list["kelas"][score_student_list["NIS"].index(new_nis)] = new_kelas
                    if colom_change == "mata pelajaran" :
                        new_mata_pelajaran = int(input("Enter New mata pelajaran : "))
                        saved_change = input("Apakah Anda Serius Ingin Mengubahnya  ?  y/n ")
                        if saved_change == "y":
                            score_student_list["mata pelajaran"][score_student_list["NIS"].index(new_nis)] = new_mata_pelajaran
                    if colom_change == "score" :
                        new_score = int(input("Enter New Score: "))
                        saved_change = input("Apakah Anda Serius Ingin Mengubahnya  ?  y/n ")
                        if saved_change == "y":
                            score_student_list["score"][score_student_list["NIS"].index(new_nis)] = new_score
                    print("Data Siswa Berhasil Disimpan")
                else:
                    print("Data Tidak Berhasil Di simpan")
            else:
                print("NIS Tidak Ditemukan")
        elif user_input == "2":
            main()
        else:
            print("Pilihan Tidak Tersedia")
    """Function for update the data
    """
    return

def delete_score():
    while  True:
        print("\n\t\t=== Delete STUDENT MENU ===")
        print("""
            1. Remove Score Student
            2. Back to Main Menu
            """
        )
        user_input = input("Enter Your Choice: ")
        if user_input == "1":
            new_nis = int(input("Enter NIS: "))
            if new_nis in score_student_list["NIS"]:
                print("\n\t\t=== Data Student ===")
                for j in range(len(score_student_list["NIS"])):
                    if score_student_list["NIS"][j] == int(new_nis):
                        print("NIS   | nama siswa |  gender    |kejuruan    |  kelas |  mata pelajaran    |  score ")
                        print(f' {score_student_list["NIS"][j]:<4} | {score_student_list["name"][j]:<10} | {score_student_list["gender"][j]:<10} | {score_student_list["kejuruan"][j]:<10} | {score_student_list["kelas"][j]:<5}  | {score_student_list["mata pelajaran"][j]:<18} | {score_student_list["score"][j]:<10}  ')
                delete_score = input("Apakah ingin  menghapus data ini ? y/n ")
                if delete_score == "y":
                    score_student_list["name"].remove(score_student_list["name"][score_student_list["NIS"].index(new_nis)])
                    score_student_list["gender"].remove(score_student_list["gender"][score_student_list["NIS"].index(new_nis)])
                    score_student_list["kejuruan"].remove(score_student_list["kejuruan"][score_student_list["NIS"].index(new_nis)])
                    score_student_list["kelas"].remove(score_student_list["kelas"][score_student_list["NIS"].index(new_nis)])
                    score_student_list["mata pelajaran"].remove(score_student_list["mata pelajaran"][score_student_list["NIS"].index(new_nis)])
                    score_student_list["score"].remove(score_student_list["score"][score_student_list["NIS"].index(new_nis)])
                    score_student_list["NIS"].remove(new_nis)
                    print("Data Siswa Berhasil Dihapus")
                else:
                    print("Data Tidak jadi dihapus")
            else:
                print("Data NIS tidak dapat ditemukan")
        elif user_input == "2":
            main()
        else:
            print("Pilihan Tidak Tersedia")


    """Function for delete the data
    """
    return

# /===== Main Program =====/
# Create your main program here
def main():
    while True:
        print("\n\t========= Data Nilai Siswa ==========")
        print(
            """List Menu:
            1. Show Name Student
            2. Create Score Name Student
            3. Update Score Name Student
            4. Delete Score Name Student
            5. Others...
            6. exit 
            """
            )
        input_user = input("Insert your option: ")
        if input_user == "1":
            show_score()
        elif input_user == "2":
            create_score()
        elif input_user == "3":
            update_score()
        elif input_user == "4":
            delete_score()
#         elif input_user == "5":
#             others()
#         elif input_user == "6":
#             break
#         else:
#             print("Input is not valid !")

            
if __name__ == "__main__":
    main()