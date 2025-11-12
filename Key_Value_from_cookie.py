cookie_string = ("cf_clearance=3kvl4m4S9QPo59_H4Sy0E75EF3C8kYo9utsq23EJdpk-1734674864-1.2.1.1-Kfq.SVVWeqZIzrz0Kky"
                 "TD1At.r79MeqsSgbQ_TYZHPq6RaINIZF5LbqSxuA388oAj5ct9IsoPla8OH7Qze2rkvX7bqPamVARp8u556IdbZBoFiJK204"
                 "T9MLHCrTlSMzhf2K3sQLAyPI149QEaQ5BfgIt3uaoUiWKdEDFWrYPBNuQuWo5omsfpB3SO4vU5gDqrywuOXzBa9.hCe3G8VH"
                 "D5SxuNALVvKTYG_RkYrOCVAmioOUIoSvwYg37N7qYQop3gmYhsMkv8RyConLdE_pRrYlbY02fRdFwesx.In2A8DN.uvty2ND5"
                 "ThqEQBM2_InPiKgqxc7y0qgobfxQXwWJyph_95avIbLgMgBHT1A.fWMGJcWONym83CGp6y.6YVVZRykaJb7VL"
                 "zjCKyDGkm4KPhH0B9Js_Ppp9JnJDPQ_XERI7SNcJW1flL8ELmTyUOoc; PHPSESSID=f82df1281cf06a0c4ed8c0c80c0f61c2")

cookies = {}
for pair in cookie_string.split(';'):
    key, value = pair.strip().split('=', 1)
    cookies[key] = value

[print(f"{key} : {value}") for key,value in cookies.items()]
