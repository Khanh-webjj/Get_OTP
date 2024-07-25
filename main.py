# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time;
import Handlers.PhoneHandler as PhoneHandler
import Handlers.TinderHandler as TinderHandler
import Handlers.TiktokHandler as TiktokHandler
import Util.Thread as ThreadUtil


def GetOtpProcess(wrongTime):
    brandName = "tinder";
    acount = "CanTest_gw";
    phoneNumb="855182551481"
    try:
        dataReturn = PhoneHandler.CallOtpApi\
            (phoneNumb=phoneNumb, brandName=brandName, acount= acount);
        # if (dataReturn == "Message not found or Archived for another partner"):
        #     print("Nall!!")
        if (dataReturn != "Message not found or Archived for another partner"):
            print("OTP come!!!");
    except Exception as e:
        print(f"Error in GetOtpProcess: {e}")
        wrongTime += 1;
        return False;
    return True;

wrongTimeOut = 0
def TinderHandle(wrongTime):
    testTinder = TinderHandler.TestTinder();
    testTinder.setup_method(None)
    try:
        testTinder.test_tinder();
    except Exception as e:
        wrongTime += 1
        print("wrong")

    # testTinder.teardown_method(None)

def TiktokHandle(wrongTime):
    testTiktok = TiktokHandler.TestTiktok();
    testTiktok.setup_method(None)
    try:
        testTiktok.test_tiktok();
    except Exception as e:
        wrongTime += 1
        print("wrong")

def Loop(loopAmout):
    for i in range(0, loopAmout, 1):
        print(f"time: {i}");
        TinderHandle(wrongTimeOut);
        # GetOtpProcess(wrongTimeOut);

def LoopByTime(startTime):
    while(time.time()-startTime < 60*3):
        GetOtpProcess(wrongTimeOut);

otpGet = 10000;

# Số lượng luồng bạn muốn tạo
num_threads = 10

start_time = time.time()  # Lấy thời gian bắt đầu

# # Tạo và bắt đầu các luồng
# for i in range(num_threads):
#     ThreadUtil.CreateThreadForLoopFunc(Loop, otpGet//num_threads);
# ThreadUtil.StartAllThread();
# ThreadUtil.JoinAllThreads();

# for i in range(num_threads):
#     ThreadUtil.CreateThreadForLoopFunc(LoopByTime, start_time);
# ThreadUtil.StartAllThread();
# ThreadUtil.JoinAllThreads();

print("start !!")
for i in range(1,10):
    print(f"loop {i}:")
    TinderHandle(wrongTime= wrongTimeOut)
end_time = time.time()  # Lấy thời gian kết thúc

execution_time = end_time - start_time  # Tính toán thời gian thực hiện
print(f"Execution time: {execution_time} seconds")
print(f'wrong time: {wrongTimeOut}')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
