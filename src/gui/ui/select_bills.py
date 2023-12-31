#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk  # 使用Tkinter前需要先导入
import tkinter.filedialog
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from functions.log4py import print_log
from functions.read_table import ReadTransactionTable
from gui.ui.globel_varable import set_value
from gui.ui.globel_varable import get_value
from gui.ui.frist_page import create_grandet_bills_window
from tools.analysis_transactions import AnalysisTransactions
from modules.transaction_tools import analysis_all_bills


def select_folder_path(bills_folder_bable: tk.Label):

    folder_name = tkinter.filedialog.askdirectory()
    print_log(f"Select bills folder: {folder_name}")
    if folder_name != '':
        bills_folder_bable.config(text = "您选择的文件是：" + folder_name)
        set_value("bills_folder", folder_name)
    else:
        bills_folder_bable.config(text = "您没有选择任何文件夹")
    return folder_name


def select_bills_file_path(bills_file_list: tk.Listbox):
    
    folder_path = get_value("bills_folder")
    print_log(f"Select bills file in folder {folder_path}.")
    
    csv_files = ReadTransactionTable.extract_csv_file_path(folder_path)
    target_csv_files = ReadTransactionTable.flitter_csv_file(csv_files)
    
    set_value("bills_files", target_csv_files)
    
    count = bills_file_list.size() + 1
    for index, item in enumerate(target_csv_files):
        now_index = index + count 
        bills_file_list.insert(now_index, f"{str(now_index)}. {item}")
        print(f"{str(now_index)}. {item}")
    return
    

def clear_bills_file_path(bills_file_list: tk.Listbox):
    
    print_log(f"Clear bills file list.")
    
    bills_file_list.delete(0, tk.END)
    return

 
def analysis_bills():
    
    bills_files = get_value("bills_files")
    if len(bills_files) == 0:
        print("No bills files.")
    else:
        print("Bills files: " + str(bills_files))
    
    bills_folder_path = get_value("bills_folder")
        
    taregt_transactions = analysis_all_bills(target_csv_files=bills_files, csv_folder_path=bills_folder_path)
    
    analysis = AnalysisTransactions(transactions=taregt_transactions)
        
    print_log(f"Target transactions: {str(analysis.get_size())}")
    print_log(f"Source transactions years: {str(analysis.get_years())}")
    print_log(f"Source transactions months: {str(analysis.get_months(target_year=2022))}")
    print_log(f"Source transactions days: {str(analysis.get_days(target_year=2022, target_month=11))}")
    every_years_transactions = analysis.get_every_years_transactions()
    print_log("Set every years transactions.")
    set_value("every_years_transactions", every_years_transactions)
    create_grandet_bills_window()


def chooes_bills_folder():
    
    folder_path = ''
    # 第1步，实例化object，建立窗口window
    select_folder_window = tk.Tk()
    # 第2步，给窗口的可视化起名字
    select_folder_window.title('导入账单')
    # 第3步，设定窗口的大小(长 * 宽)
    select_folder_window.geometry('800x500')  # 这里的乘是小x
    
    bills_folder_bable = tk.Label(select_folder_window, text = '')
    bills_folder_bable.pack()
    
    # 左侧账单文件列表
    btn_frame = tk.Frame(select_folder_window)
    btn_frame.pack(side="left", fill="both", expand=True)
    
    # 右侧每年花销简介
    bills_file_summary = tk.Frame(select_folder_window)
    bills_file_summary.pack(side="right", fill="both", expand=True)
    
     # 提取账单文件
    bills_file_list = tk.Listbox(bills_file_summary, width=60, height=20)
    bills_file_list.pack()
    
    # bt=ttk.Button(lf1, text="处理", bootstyle=SUCCESS,command=fun)
    btn = tk.Button(btn_frame, text="导入账单", command=lambda : select_folder_path(bills_folder_bable=bills_folder_bable))
    select_bills_file_btn = tk.Button(btn_frame, text="提取账单文件", command=lambda : select_bills_file_path(bills_file_list=bills_file_list))
    clear_bills_file_btn = tk.Button(btn_frame, text="重置账单文件", command=lambda : clear_bills_file_path(bills_file_list=bills_file_list)) 
    analysis_btn = tk.Button(btn_frame, text="分析账单", command=lambda : analysis_bills())
    
    btn.pack(side=tk.TOP, fill=tk.X)
    select_bills_file_btn.pack(side=tk.TOP, fill=tk.X)
    analysis_btn.pack(side=tk.TOP, fill=tk.BOTH)
    clear_bills_file_btn.pack(side=tk.TOP, fill=tk.BOTH)
    
    select_folder_window.mainloop()