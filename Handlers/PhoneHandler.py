#
from Util import ApiConTact
import time

def CallMsisonApi(brandName, acount): # get phone numb
    apiMode = ApiConTact.data_const.API_GET_MSISDN_MODE;
    apiInputData = ApiConTact.ApiInputData(brandName=brandName, apiMode=apiMode, acount=acount)

    linkMsison = ApiConTact.GetApiLink(apiInputData);

    data = ApiConTact.API(url=linkMsison).GET();
    return data;

def CallOtpApi(phoneNumb = "0", brandName = "msverify",acount = "CanTest_gw"): # need to call during at least 5 minute
    apiMode = ApiConTact.data_const.API_GET_OTP_MODE;
    apiInputData = ApiConTact.ApiInputData(brandName=brandName, apiMode=apiMode, acount=acount, phone=phoneNumb);

    link = ApiConTact.GetApiLink(apiInputData);

    data = ApiConTact.API(url=link).GET();
    return data


def call_api_continuously(phone_number, brand_name, account):
    start_time = time.time()
    end_time = start_time + 60  # 1 minute = 60 seconds
    final_result = None
    status = "failed"

    while time.time() < end_time:
        mess = CallOtpApi(phone_number, brand_name, account)
        print(type(mess))
        if isinstance(mess, str):
            final_result = mess
        else:
            final_result = mess
            status = "success"
            break

        time.sleep(1)  # Wait 1 second before calling the API again

    return {"final_result": final_result, "status": status}