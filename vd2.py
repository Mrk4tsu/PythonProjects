##Nhập 1 năm dương lịch, in ra năm âm lịch tương ứng

#VD: 2024  -> Giáp Thìn

can = ['Canh', 'Tân', 'Nhâm', 'Quý', 'Giáp', 'Ất', 'Bính', 'Đinh', 'Mậu', 'Kỷ']
chi = ['Tý', 'Sửu', 'Dần', 'Mão', 'Thìn', 'Tỵ', 'Ngọ', 'Mùi', 'Thân', 'Dậu', 'Tuất', 'Hợi']


#Nhập năm dương lịch
namDl = int(input("Nhập năm dương lịch: "))

can1 = namDl  % 10  # Thực hiện điều chỉnh vị trí Can
chi1 = (namDl + 8) % 12   # Thực hiện điều chỉnh vị trí Chi

namAL = can[can1] + ' ' + chi[chi1]
print(namAL)

