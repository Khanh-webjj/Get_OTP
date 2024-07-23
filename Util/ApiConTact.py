import requests
import Util.config as data_const
import json

# api form: API_URL_MAIN_TEMPLATE + API_MODE +"/"+ brandName +"/"+ acount +"/"+ API_KEY

class ApiInputData:
    def __init__(self, apiMode,  brandName , acount, phone = "0"):
        if apiMode != None:
            self.__apiMode = apiMode
        else:
            self.__apiMode = data_const.API_GET_MSISDN_MODE;
        self.__brandName = brandName;
        self.__acount = acount;
        self.__phone = phone;

    def __repr__(self):
        return f"ApiInputData(mode='{self.__apiMode}' ,brand='{self.__brandName}', acount='{self.__acount}', phone = '{self.__phone}')";

    # SET
    def SetBrandName(self, brandName):
        self.__brandName = brandName;

    def SetAcount(self, acount):
        self.__acount = acount;

    def SetMode(self, apiMode):
        self.__apiMode = apiMode;

    def SetPhone(self, phone):
        self.__phone = phone;

    # GET
    def GetMode(self):
        return self.__apiMode;

    def GetBrandName(self):
        return self.__brandName;

    def GetAcount(self):
        return self.__acount;

    def GetPhone(self):
        return  self.__phone;


class PhoneNumberInfo:
    # init method
    def __init__(self, msisdn, code, message):
        self.Msisdn = msisdn;
        self.code = code;
        self.message = message;

    def __init__(self, jsonData):
        self.Msisdn = jsonData['Msisdn'];
        self.code = jsonData['code'];
        self.message = jsonData['message'];

    # to string method
    def __repr__(self):
        return f"PhoneNumberInfo(msisdn='{self.Msisdn}', code={self.code}, message='{self.message}')";

    # def ConVertJSonToObj(cls, data):
    #     return cls(
    #         msisdn=data['Msisdn'],
    #         code=data['code'],
    #         message=data['message']
    #     )

class API:
    def __init__(self, url):
        self.__url = url

    def GetUrl(self):
        return self.__url

    def GET(self):
        try:
            response = requests.get(url= self.__url)
            response.raise_for_status()  # Kiểm tra mã trạng thái HTTP
            try:
                data = response.json()
            except json.decoder.JSONDecodeError:
                data = response.text
        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")
            data = None

        return data

# api form: API_URL_MAIN_TEMPLATE + API_MODE +"/"+ brandName +"/"+ acount +"/"+ API_KEY
def  GetApiLinkByElement(apiMod ,brandName, acount, phone = "0"):
    link = f"";
    if (apiMod == data_const.API_GET_MSISDN_MODE):
        link = f"{data_const.API_URL_MAIN_TEMPLATE}/{apiMod}/{brandName}/{acount}/{data_const.API_KEY}"
    elif (apiMod == data_const.API_GET_OTP_MODE):
        link = f"{data_const.API_URL_MAIN_TEMPLATE}/{apiMod}/{brandName}/{acount}/{data_const.API_KEY}/{phone}"

    return link;


def GetApiLink(apiInputData):
    return GetApiLinkByElement(
        apiMod = apiInputData.GetMode(),
        brandName= apiInputData.GetBrandName(),
        acount= apiInputData.GetAcount(),
        phone= apiInputData.GetPhone()
        );
