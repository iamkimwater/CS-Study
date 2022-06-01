# 파일을 쓰고 읽기
# 예외 처리

# 텍스트파일
# writer = open("users.txt", "a", encoding="utf8")
# writer.write("하하하\n")
# writer.write("하하하\n")
# writer.close()

# reader = open("users.txt", "r", encoding="utf8")
# print(reader.read())
# print(reader.readlines())
# print(reader.readline())
# print(reader.readline())
# print(reader.readline())
# print(reader.readline())
# reader.close()

# csv파일
# import csv
# writer = open("users.csv", "a", encoding="utf8", newline="")
# csv_writer = csv.writer(writer)
# csv_writer.writerow(["하하하", "호호호", "후후후"])
# writer.close()
#
# reader = open("users.csv", "r", encoding="utf8", newline="")
# csv_reader = csv.reader(reader)
# for row in csv_reader:
#     print(row[2])


# while True:
#     try:
#         print(x)
#     except Exception as e:
#         print(e)