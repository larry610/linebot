import requests
import twstock
import pandas as pd
import numpy as np
from linebot.models import FlexSendMessage


def PE():
    query_url = 'https://openapi.twse.com.tw/v1/exchangeReport/BWIBBU_ALL' 
    response = requests.get(query_url) 
    data = response.json() 
    df = pd.DataFrame(data) 
    column_mapping = { 
        'Code': '股票代號', 
        'Name': '公司名稱', 
        'PEratio': '本益比', 
        'DividendYield': '殖利率',
        'PBratio': '股價淨值比'
     }
    df = df.rename(columns=column_mapping) 
    sorted_df = df.sort_values(by='本益比', ascending=True).head(15) 
    # 設定每個欄位的寬度，並使用 str.format() 調整對齊 
    format_string = "{:<10} {:<10} {:>8}" 
    header = format_string.format("股票代號", "公司名稱", "本益比") 
    result_text = [header] 
    for index, row in sorted_df.iterrows():
        formatted_row = format_string.format(row["股票代號"], row["公司名稱"], row["本益比"]) 
         
        result_text.append(formatted_row)

    return "\n".join(result_text)


def DY():
    # 列出殖利率最高前15
    query_url = f'https://openapi.twse.com.tw/v1/exchangeReport/BWIBBU_ALL'
    response = requests.get(query_url)
    data = response.json()
    df = pd.DataFrame(data)
    column_mapping = {
        'Code': '股票代號',
        'Name': '公司名稱',
        'PEratio': '本益比',
        'DividendYield': '殖利率',
        'PBratio': '股價淨值比'
    }
    df = df.rename(columns=column_mapping)
    sorted_df = df.sort_values(by='殖利率', ascending=False).head(15)
    format_string = "{:<10} {:<10} {:>10}" 
    header = format_string.format("股票代號", "公司名稱", "殖利率") 
    result_text = [header] 
    for index, row in sorted_df.iterrows():
        formatted_row = format_string.format(row["股票代號"], row["公司名稱"], row["殖利率"]) 
            
        result_text.append(formatted_row)

    return "\n".join(result_text)

def PB():
    query_url = 'https://openapi.twse.com.tw/v1/exchangeReport/BWIBBU_ALL' 
    response = requests.get(query_url) 
    data = response.json() 
    df = pd.DataFrame(data) 
    column_mapping = { 
        'Code': '股票代號', 
        'Name': '公司名稱', 
        'PEratio': '本益比', 
        'DividendYield': '殖利率',
        'PBratio': '股價淨值比'
     }
    df = df.rename(columns=column_mapping) 
    sorted_df = df.sort_values(by='股價淨值比', ascending=True).head(15) 
    # 設定每個欄位的寬度，並使用 str.format() 調整對齊 
    format_string = "{:<10} {:<10} {:>10}" 
    header = format_string.format("股票代號", "公司名稱", "股價淨值比") 
    result_text = [header] 
    for index, row in sorted_df.iterrows():
        formatted_row = format_string.format(row["股票代號"], row["公司名稱"], row["股價淨值比"]) 
         
        result_text.append(formatted_row)

    return "\n".join(result_text)


def PE2():
    query_url = f'https://www.tpex.org.tw/openapi/v1/tpex_mainboard_peratio_analysis'
    response = requests.get(query_url)
    data = response.json()
    df = pd.DataFrame(data)
    column_mapping = {
        'Date': '資料日期',
        'SecuritiesCompanyCode': '股票代號',
        'CompanyName' :'公司名稱',
        'PriceEarningRatio': '本益比',
        'DividendPerShare': '每股股利',
        'YieldRatio': '殖利率',
        'PriceBookRatio':'股價淨值比'
    }
    df = df.rename(columns=column_mapping)
    sorted_df = df[["股票代號", "公司名稱", "本益比"]].sort_values(by='本益比', ascending=True).head(15)
    format_string = "{:<10} {:<10} {:>10}" 
    header = format_string.format("股票代號", "公司名稱", "本益比") 
    result_text = [header] 
    for index, row in sorted_df.iterrows():
            formatted_row = format_string.format(row["股票代號"], row["公司名稱"], row["本益比"]) 
            
            result_text.append(formatted_row)

    return("\n".join(result_text))

def DY2():
    query_url = f'https://www.tpex.org.tw/openapi/v1/tpex_mainboard_peratio_analysis'
    response = requests.get(query_url)
    data = response.json()
    df = pd.DataFrame(data)
    column_mapping = {
        'Date': '資料日期',
        'SecuritiesCompanyCode': '股票代號',
        'CompanyName' :'公司名稱',
        'PriceEarningRatio': '本益比',
        'DividendPerShare': '每股股利',
        'YieldRatio': '殖利率',
        'PriceBookRatio':'股價淨值比'
    }
    df = df.rename(columns=column_mapping)
    sorted_df = df.sort_values(by='殖利率', ascending=False).head(15)
    format_string = "{:<10} {:<10} {:>10}" 
    header = format_string.format("股票代號", "公司名稱", "殖利率") 
    result_text = [header] 
    for index, row in sorted_df.iterrows():
        formatted_row = format_string.format(row["股票代號"], row["公司名稱"], row["殖利率"]) 
            
        result_text.append(formatted_row)

    return "\n".join(result_text)

def PB2():
    query_url = f'https://www.tpex.org.tw/openapi/v1/tpex_mainboard_peratio_analysis'
    response = requests.get(query_url)
    data = response.json()
    df = pd.DataFrame(data)
    column_mapping = {
        'Date': '資料日期',
        'SecuritiesCompanyCode': '股票代號',
        'CompanyName' :'公司名稱',
        'PriceEarningRatio': '本益比',
        'DividendPerShare': '每股股利',
        'YieldRatio': '殖利率',
        'PriceBookRatio':'股價淨值比'
    }
    df = df.rename(columns=column_mapping)
    sorted_df = df.sort_values(by='股價淨值比', ascending=False).head(15)
    format_string = "{:<10} {:<10} {:>10}" 
    header = format_string.format("股票代號", "公司名稱", "股價淨值比") 
    result_text = [header] 
    for index, row in sorted_df.iterrows():
        formatted_row = format_string.format(row["股票代號"], row["公司名稱"], row["股價淨值比"]) 
            
        result_text.append(formatted_row)

    return "\n".join(result_text)




if __name__ == "__main__":
    flex_message_dy = FlexSendMessage(alt_text="殖利率排行", contents=DY())
    flex_message_pe = FlexSendMessage(alt_text="本益比排行", contents=PE())
    flex_message_pb = FlexSendMessage(alt_text="股價淨值比排行", contents=PB())
    flex_message_dy2 = FlexSendMessage(alt_text="殖利率排行", contents=DY2())
    flex_message_pe2 = FlexSendMessage(alt_text="本益比排行", contents=PE2())
    flex_message_pb2 = FlexSendMessage(alt_text="股價淨值比排行", contents=PB2())
    
    print(flex_message_dy)
    print(flex_message_pe)
    print(flex_message_pb)
    print(flex_message_dy2)
    print(flex_message_pe2)
    print(flex_message_pb2)






