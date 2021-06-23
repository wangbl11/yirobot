import requests
import json

url ="https://login.taobao.com/member/login.jhtml"
# url="https://login.taobao.com/newlogin/login.do?appName=taobao&fromSite=0"

ponse = requests.session()

# 在devtools的console中运行document.cookie，把字符串拷贝出来
headers = {
'cookie':'cna=6TYgF0FGzEMCAXOrKfS60kPl; hng=CN%7Czh-CN%7CCNY%7C156; lid=tinawbl74; t=b033c31d86e558792fc5412bfd0a1e54; tracknick=tinawbl74; lgc=tinawbl74; dnk=tinawbl74; _tb_token_=eb0b350b78ff8; _m_h5_tk=63470b9914e96e8bef7f4cf50fe34bd2_1594480490019; _m_h5_tk_enc=6c1dfcf39fa395ca6229b0a8ab49ea1e; tfstk=co25BJ0fUye2jAfeUusqzHHwRvDhZk9S0gg0VS-qo4oWCzZ5iV9Z5hZ7xEpx6m1..; uc1=cookie14=UoTV6OZXGU7Gdw%3D%3D&cookie15=UIHiLt3xD8xYTw%3D%3D&pas=0&cookie21=VFC%2FuZ9ajCbF99I65Qm9gQ%3D%3D&cookie16=WqG3DMC9UpAPBHGz5QBErFxlCA%3D%3D&existShop=false; _l_g_=Ug%3D%3D; unb=272034677; login=true; _nk_=tinawbl74; sg=472; csg=4c993475; pnm_cku822=; l=eBSW_wvrQAwMkiqyBOfZourza77OSIRYnuPzaNbMiOCPOkf65qPGWZlFrDYBC3hNhsTDR3l5AnGaBeYBc7Vonxv9phmLdJMmn; isg=BObmSykhhX-V2VBMafWvLstnN1poxyqBhKOQDNCP0onkU4ZtOFd6kcyhqkdfQSKZ',
'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',

}

data="""loginId=tinawbl74&password2=7d9d11b81a6898ac0290881ef2a15696151a6453af419f580b052eaca2a88348ebe32a1ffd938a6b1dbe8e8eadf44f39c40b3f5c39938f9b3116f7b87c2883131bb0bd4d6fbedb104c8391cb211e496aff34d83a20f6f957163128752a1f708c1545f429c9dad923c835c9ed7a5d9a8d8b83f7e1d43ce9f9390081b889462b62&keepLogin=false&ua=125%23cQgca%2FH0cW2D1bAe%2BaY1xfdSuDf2r14YEXzdh0wkDDIBPnGPY%2B%2FEZTQapR9Np%2FoikMJU1w%2Bs0GlM0MKufPGfn7JRuhBM0Q5p7%2FPwBiLKToLcre2kJll9HUgsYIUHGuxJD63TJWYB3vSGNkOjhcOfp2O8K%2FNe1EDfHO%2BcszqojdxMKcy08CPGJfJ3Kl%2BC6%2BBkiirLyI7tUCo5U9SR171iI7qC9hppvxCz1VQxGyeNkNXPira0Q%2BRyvBlhM7Qa9sX481uaehFTvZDLvQZzBgys4ewToP2XrPC5MzI%2ByVg393pDFk9gshect%2BtD%2BJi4FDiccgapEgsSUXoSWVnZcNVJiaDMpJfhf%2BHOzaSR3NaRbyDVSvHkcNaYU6aOkqhffyeOFhAbEjcSUrifaJwtaKelO%2BriU2bFEZzWiIfO%2BNzHJPAAfQG28XvYGvrtvRF7YDASzlFZkS9O3pA0si7DAR%2BpTIJavuZ3xcdeIHM4Kjh37ACAlOyEp1JbG%2FPB76WIZh2CYYvU7XOx2qIYYOJ2y5rKbXhR%2Bnyl5tfI8eF2tMRoxH25r1MdcQmdMAYHk%2B8KZbEV2HXiYUqKaByqavS38TpK8xfThs%2B%2FHitIlsJjhDur%2Bb5NGzw5xQqCVNWGcbJCrZ2CVDg8bHptsMx6NtCNm6CVFcQcbrprO3VqW1MUifUz6O1h4X7voHWvlrmILOeAKF4azlUr0hVvq1oiW%2FFnOT7crlL76pRFNCNd%2FFlzobZlUW4kzY09oPZTlCz0jfCzeKBelHhDix91IUonojX3saTWND3KDi7VM0GRAHMEV9EYeUWFBUYAPY16TzrBjg9AtvItQpFgHsLYeMmiEMQEo3FdtbZFR3D%2BWB5jJmoljVAADeXO5O03azN9ABwtSTH2GyVkSkkcxs747O9engpp2O6DH5kX0q5Aq8i4xtceMQTTzzN%2BoquRa1ogkIjuaxDt4jo6skLdU%2BcSbNEP%2BLcvKbvjO9qUvsp3VQMltaQwENActr9f17ahoFpmsUVEo%2FG3IEhGTe6JEqs7OY7yH7F0rFO8FE77V5rlGNtiPoWv2bJ8xjyEMHRz7fiBJ2sIvZ6gQL6L3ZG47lvfc3rVBemkkYlZ8jLj3g5xJt6OXhKbQSKhl0eOpDiNaRE4RklIZPydZBqgG6SFKIEmvVtSYC92t56JRa01klPrmHfQVLmRREm%2B0OLopFSa&umidGetStatusVal=255&screenPixel=1440x900&navlanguage=en-US&navUserAgent=Mozilla%2F5.0%20%28Macintosh%3B%20Intel%20Mac%20OS%20X%2010_15_4%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F83.0.4103.116%20Safari%2F537.36&navPlatform=MacIntel&appName=taobao&appEntrance=taobao_pc&_csrf_token=joKxlGi40muMaeA4uQfom8&umidToken=b209223db4291eb9e9c4ffdacd4f87d4454856d1&hsiz=1b0cbc15005ffea3a0a71538b83bb51e&bizParams=&style=default&appkey=00000000&from=tbTop&isMobile=false&lang=zh_CN&returnUrl=https%3A%2F%2Fwww.taobao.com%2F&fromSite=0"""
datum=data.split("&")
_data={}
for one in datum:
    _idx=one.index("=")
    _data[one[0:_idx]]=one[_idx+1:]

url1="https://elandkids.tmall.com/search.htm"

t = ponse.get(url1,headers=headers)
print(t.text)

