#/bin/bash python3

import tkinter as tk
from tkinter import ttk

from modules.transaction import Transaction


def genaertion_table(tree: ttk.Treeview, transactions: list, index_flitter: list=[3, 8, 9, 10]) -> ttk.Treeview:
     
    all_heading = ["交易时间", "交易分类", "交易对方", "对方账号", "商品说明", "收/支", "金额", "收/付款方式", "交易状态", "交易订单号", "商家订单号", "备注", "来源"]
    all_heading_width = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
    heading_text = []
    for index, item in enumerate(all_heading):
        if index not in index_flitter:
            heading_text.append(item)
            
    tree["columns"] = heading_text
    for index, item in enumerate(heading_text):
        tree.column(item, width=all_heading_width[index])
        tree.heading(item, text=item)
    # 插入数据
    l = len(transactions)
    for index, item in enumerate(transactions):
        if isinstance(item, Transaction):
            temp_transaction_infos = item.to_list()
            target_transaction_infos = []
            for temp_index, item in enumerate(temp_transaction_infos):
                if temp_index not in index_flitter:
                    target_transaction_infos.append(item)
            tree.insert("", 0, text=f"{str(l - index)}", values=target_transaction_infos)
    return tree
        
    

def show_transactions(transactions: list, index_flitter: list=[3, 8, 9, 10]):
    
    # 创建窗口
    window = tk.Tk()
    window.title("表格数据")
    # all_heading = ["交易时间", "交易分类", "交易对方", "对方账号", "商品说明", "收/支", "金额", "收/付款方式", "交易状态", "交易订单号", "商家订单号", "备注", "来源"]
    # all_heading_width = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
    # heading_text = []
    # for index, item in enumerate(all_heading):
    #     if index not in index_flitter:
    #         heading_text.append(item)
    
    # 创建表格
    tree = ttk.Treeview(window)
    
    yscrollbar = ttk.Scrollbar(window)
    yscrollbar.pack(side=tk.RIGHT,fill=tk.Y)
    yscrollbar.config(command=tree.yview)
    tree.configure(yscrollcommand=yscrollbar.set) # 经过试验，以上两行代码交换顺序后无影响
    tree = genaertion_table(transactions=transactions, index_flitter=index_flitter, tree=tree)
    # tree["columns"] = heading_text
    # for index, item in enumerate(heading_text):
    #     tree.column(item, width=all_heading_width[index])
    #     tree.heading(item, text=item)
    # # 插入数据
    # l = len(transactions)
    # for index, item in enumerate(transactions):
    #     if isinstance(item, Transaction):
    #         temp_transaction_infos = item.to_list()
    #         target_transaction_infos = []
    #         for temp_index, item in enumerate(temp_transaction_infos):
    #             if temp_index not in index_flitter:
    #                 target_transaction_infos.append(item)
    #         tree.insert("", 0, text=f"{str(l - index)}", values=target_transaction_infos)
    tree.pack()
    # 运行窗口
    window.mainloop()

