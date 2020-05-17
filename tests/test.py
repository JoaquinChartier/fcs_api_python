from fcs_api_py import Forex

forex = Forex("YnYoWTp2zMKlO0uncML1wRdPVHJ9Ie1RESxNdP0DifgozAIuBh")
obj = forex.technical_indicator("EUR/JPY", "1d")

print(obj.response.oa_summary)
print(obj.response.indicators.ATR14.s)
print(obj.response.indicators.ATR14.v)
print(obj.response.indicators.WilliamsR.s)
print(obj.response.indicators.WilliamsR.v)


print(obj.info.disclaimer)