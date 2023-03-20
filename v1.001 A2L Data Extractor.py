with open("SC8O30.a2l", encoding="Latin-1") as f, open("output.txt", "w", encoding="Latin-1") as txtout:
    des_flag = False
    address_flag = False
    for line in f:
        line = line.strip()
        if address_flag:
            if line.startswith("ECU_ADDRESS") or line.startswith("0x"):
                txtout.write(line.strip("ECU_ADDRESS"))
                txtout.write("\n")
                address_flag = False
        elif des_flag:
            txtout.write(line + "|")
            des_flag = False
            address_flag = True
        elif line.startswith("/begin CHARACTERISTIC") or line.startswith("/begin MEASUREMENT") or line.startswith("/begin AXIS_PTS"):
            txtout.write(" " + line.strip("/begin ") + "|")
            des_flag = True
    print("text file created successfully")
