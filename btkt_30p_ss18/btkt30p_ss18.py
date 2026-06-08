list_ct = [
    {
        "id": "CT007",
        "name": "Nguyen Quang Hai",
        "tran_dau": 10,
        "goal": 5,
        "kien_tao": 4,
        "hieu_suat": 33,
        "phong_do": "Trụ cột đội bóng"
    }
]
# case 1
def read_list(list_emp):
    if len(list_emp) == 0:
        print("danh sách cầu thủ không tồn tại")
    else:
        print("--------- DANH SÁCH CẦU THỦ ---------")
        for index, value in enumerate(list_emp, start=1):
            print(f"{index}. MÃ CT: {value["id"]} | Họ Tên: {value["name"]} | Số Trận: {value["tran_dau"]} | Bàn thắng: {value["goal"]} | Kiến tạo: {value["kien_tao"]} | Điểm hiệu suất: {value["hieu_suat"]} | Phân loại phong độ: {value["phong_do"]}")
# case 2
# hàm tính điểm hiệu suất và trạng thái phong độ
def total_hieu_suat_and_phong_do(tran_dau, goal, kien_tao):
    tran_dau = int(tran_dau)
    goal = int(goal)
    kien_tao = int(kien_tao)
    hieu_suat = (tran_dau * 1) + (goal * 3) + (kien_tao * 2)
    if hieu_suat >= 50:
        return hieu_suat, "Ngôi sao đẳng cấp"
    elif hieu_suat >= 30:
        return hieu_suat, "Trụ cột đội bóng"
    elif hieu_suat >= 15:
        return hieu_suat, "Dự bị chiến lược"
    else:
        return hieu_suat, "Cần thanh lý / Cho mượn"
# hàm check mã cầu thủ
def check_id(list_emp, id):
    flag = False
    for index, value in enumerate(list_emp):
        if value["id"] == id:
            flag = True
            return True
    if not flag:
        return False
# check số trận
def check_so(emp):
    if (not emp.isdigit()) and (int(emp) < 0 or int(emp) > 50):
        return True
    else:
        return False
# check số bàn thắng và kiến tạo
def check_so_bt_kt(emp):
    if (not emp.isdigit()) and (int(emp) < 0):
        return True
    else:
        return False
# check rỗng 
def check_rong(emp):
    if emp == "":
        return True
    else:
        return False
def creat_list(list_emp):
    id = input("Nhập mã cầu thủ mới: ").strip().upper()
    if check_id(list_emp, id) == True:
        print("ID đã tồn tại trong danh sách cầu thủ")
        return
    if check_rong(id) == True:
        print("id không được để trống") 
        return
    name = input("Nhập tên cầu thủ mới: ").strip().title()
    if check_rong(name) == True:
        print("tên không được để trống")
        return
    tran_dau = input("Nhập số trận đấu mới: ").strip()
    if check_so(tran_dau) == True:
        print("Số trận thi đấu phải là số nguyên nằm trong khoảng từ 0 đến 50")
        return
    goal = input("Nhập số bàn thắng mới: ").strip()
    if check_so_bt_kt(goal) == True:
        print("Số kiến tạo phải là số nguyên lớn hơn hoặc bằng 0")
        return
    kien_tao = input("Nhập số lần kiến tạo mới: ").strip()
    if check_so_bt_kt(kien_tao) == True:
        print("Số bàn thắng phải là số nguyên lớn hơn hoặc bằng 0")
        return
    hieu_suat, phong_do  = total_hieu_suat_and_phong_do(tran_dau, goal, kien_tao)
    list_emp.append({
        "id": id,
        "name": name,
        "tran_dau": tran_dau,
        "goal": int(goal),
        "kien_tao": int(kien_tao),
        "hieu_suat": int(hieu_suat),
        "phong_do": phong_do
    })
# case 3
# hàm trả index 
def check_id_index(list_emp, id):
    flag = False
    for index, value in enumerate(list_emp):
        if value["id"] == id:
            flag = True
            index_id = index
            return index_id
    if not flag:
        return False
def update_list(list_emp):
    id_new = input("Nhập mã cầu thủ cần cập nhật: ").strip().upper()
    if check_id(list_emp, id_new):
        index_id = check_id_index(list_emp, id_new)
        tran_dau = input("Nhập số trận đấu mới: ").strip()
        if check_so(tran_dau) == True:
            print("Số trận thi đấu phải là số nguyên nằm trong khoảng từ 0 đến 50")
            return
        goal = input("Nhập số bàn thắng mới: ").strip()
        if check_so_bt_kt(goal) == True:
            print("Số kiến tạo phải là số nguyên lớn hơn hoặc bằng 0")
            return
        kien_tao = input("Nhập số lần kiến tạo mới: ").strip()
        if check_so_bt_kt(kien_tao) == True:
            print("Số bàn thắng phải là số nguyên lớn hơn hoặc bằng 0")
            return
        hieu_suat, phong_do  = total_hieu_suat_and_phong_do(tran_dau, goal, kien_tao)
        # cập nhật lại
        list_emp[index_id]["tran_dau"] = int(tran_dau)
        list_emp[index_id]["goal"] = int(goal)
        list_emp[index_id]["kien_tao"] = int(kien_tao)
        list_emp[index_id]["hieu_suat"] = int(hieu_suat)
        list_emp[index_id]["phong_do"] = phong_do
        print(f"Cập nhật {id_new} thành công")
    else:
        print("Id không tồn tại trong danh sách")
        return
# case 4
def delete_list(list_emp):
    id_new = input("Nhập mã cầu thủ cần xóa(thanh lý hợp đồng): ").strip().upper()
    if check_id(list_emp, id_new):
        index_id = check_id_index(list_emp, id_new)
        list_emp.pop(index_id)
        print(f"Thanh lý thành công cầu thủ {id_new}")
    else:
        print("Id không tồn tại trong danh sách")
        return
# case 5
# hàm tìm tên
def filter_list(list_emp):
    check_key = input("Mời bạn nhập id cần tìm hoặc theo tên: ").strip().upper()
    if check_rong(check_key) == True:
        print("Không được để trống")
        return
    flag = False
    for index, value in enumerate(list_emp):
        print("--- cầu thủ cần tìm --- ")
        name = value["name"]
        name = name.lower()
        if check_key == value["id"] or check_key.strip().lower() in name:
            flag = True
            print(f"{index}. MÃ CT: {value["id"]} | Họ Tên: {value["name"]} | Số Trận: {value["tran_dau"]} | Bàn thắng: {value["goal"]} | Kiến tạo: {value["kien_tao"]} | Điểm hiệu suất: {value["hieu_suat"]} | Phân loại phong độ: {value["phong_do"]}")
            break
    if not flag:
        print("Không tìm thấy key bạn cần tìm")
# case 6
def total_all(list_emp):
    total_phong_do_01 = 0
    total_phong_do_02 = 0
    total_phong_do_03 = 0
    total_phong_do_04 = 0
    for index, value in enumerate(list_emp):
        if value["phong_do"] == "Cần thanh lý / Cho mượn":
            total_phong_do_01 += 1
        elif value["phong_do"] == "Dự bị chiến lược":
            total_phong_do_02 += 1
        elif value["phong_do"] == "Trụ cột đội bóng":
            total_phong_do_03 += 1
        elif value["phong_do"] == "Ngôi sao đẳng cấp":
            total_phong_do_04 += 1
    print(f"""
    ---- Số lượng các phong độ ----
    Cần thanh lý / Cho mượn: {total_phong_do_01}
    Dự bị chiến lược : {total_phong_do_02}
    Trụ cột đội bóng: {total_phong_do_03}
    Ngôi sao đẳng cấp: {total_phong_do_04}
    """)
def main():
    while True:
        print("--- MENU ---")
        print("""
            1. Hiển thị danh sách cầu thủ
            2. Tiếp nhận cầu thủ mới 
            3. Cập nhật thông tin và chỉ số
            4. xóa cầu thủ (Thanh lý hợp đồng)
            5. Tìm kiếm cầu thủ
            6. Thống kê phân loại phong độ
            8. Thoát chương trình
            """)
        choice = input("Mời bạn nhập chức năng (1-8): ")
        match choice:
            case "1":
                read_list(list_ct)
            case "2":
                creat_list(list_ct)
            case "3":
                update_list(list_ct)
            case "4":
                delete_list(list_ct)
            case "5":
                filter_list(list_ct)
            case "6":
                total_all(list_ct)
            case "8":
                print("Chào tạm biệt")
                break
            case _:
                print("Mời bạn nhập lại lựa chọn từ 1-8")
main()
