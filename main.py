# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time
import os

from openpyxl import load_workbook

import Handlers.PhoneHandler as PhoneHandler
import Handlers.TinderHandler as TinderHandler
import Util.Thread as ThreadUtil
import shutil

from Handlers.ExcelHandler import merge_excel_files

wrongTimeOut = 0

def GetOtpProcess(wrongTime):
    brandName = "tinder"
    acount = "CanTest_gw"
    phoneNumb="855182551481"
    try:
        dataReturn = PhoneHandler.CallOtpApi\
            (phoneNumb=phoneNumb, brandName=brandName, acount= acount)
        # if (dataReturn == "Message not found or Archived for another partner"):
        #     print("Nall!!")
        if (dataReturn != "Message not found or Archived for another partner"):
            print("OTP come!!!")
    except Exception as e:
        print(f"Error in GetOtpProcess: {e}")
        wrongTime += 1
        return False
    return True

def TinderHandle(wrongTime, i, idx,workbook):
    testTinder = TinderHandler.TestTinder()
    testTinder.setup_method(None)
    try:
        testTinder.test_tinder(str(i),idx,workbook)
    except:
        wrongTime += 1
        print("wrong")

def Loop(loopAmout,num_thread,workbook):
    for i in range(0, loopAmout, 1):
        print(f"time: {i}")
        TinderHandle(wrongTimeOut,str(num_thread), i+1, workbook)
        # GetOtpProcess(wrongTimeOut)
    workbook.save(f'D:\\Workspace\\Get_OTP\\Resource\\Excel\\report_template{num_thread}.xlsx')
        # TinderHandle(wrongTimeOut)
        # GetOtpProcess(wrongTimeOut)

def LoopByTime(startTime):
    while(time.time()-startTime < 60*3):
        GetOtpProcess(wrongTimeOut)

otpGet = 4

# Số lượng luồng bạn muốn tạo
num_threads = 2

start_time = time.time()  # Lấy thời gian bắt đầu
workbook= []
template_file_name = 'D:\\Workspace\\Get_OTP\\Resource\\Excel\\report_template.xlsx'

for i in range(num_threads):
    new_file_name = f'D:\\Workspace\\Get_OTP\\Resource\\Excel\\report_template{i}.xlsx'
    shutil.copy(template_file_name, new_file_name)
    workbook.append(load_workbook(new_file_name))

# Tạo và bắt đầu các luồng
for i in range(num_threads):
    ThreadUtil.CreateThreadForLoopFunc(Loop, otpGet//num_threads,i,workbook[i])
ThreadUtil.StartAllThread()
ThreadUtil.JoinAllThreads()

# for i in range(num_threads):
#     ThreadUtil.CreateThreadForLoopFunc(LoopByTime, start_time)
# ThreadUtil.StartAllThread()
# ThreadUtil.JoinAllThreads()

# TinderHandle(wrongTimeOut)

for num_thread in range(num_threads):
    final = 'D:\\Workspace\\Get_OTP\\Resource\\Excel\\report_total.xlsx'
    each_thread = 'D:\\Workspace\\Get_OTP\\Resource\\Excel\\report_template' + str(num_thread) + '.xlsx'
    merge_excel_files(final,each_thread)
    # os.remove(each_thread)


# print("start !!")
# for i in range(1,10):
#     print(f"loop {i}:")
#     TinderHandle(wrongTime= wrongTimeOut)
end_time = time.time()  # Lấy thời gian kết thúc

execution_time = end_time - start_time  # Tính toán thời gian thực hiện
print(f"Execution time: {execution_time} seconds")
print(f'wrong time: {wrongTimeOut}')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
