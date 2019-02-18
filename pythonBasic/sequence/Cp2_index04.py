# 检查用户名和PIN码
database = [
    ['albert', '1234'],
    ['dilbert', '4242'],
    ['smith', '7542'],
    ['jones', '9814']
]
username = input("user name: ")
pin = input("PIN code: ")
if [username, pin] in database:
    print("Access granted")
else:
    print("Access rejected")