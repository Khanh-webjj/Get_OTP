#
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
    return data;