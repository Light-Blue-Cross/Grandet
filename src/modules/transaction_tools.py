#/bin/bash python3

from datetime import datetime

from functools import cmp_to_key
from functions.log4py import print_log
from modules.transaction import Transaction
from modules.transaction_datetime import TransactionDateTime
from functions.read_table import ReadTransactionTable
from functions.write_table import WriteTransactionTable
from gui.ui.globel_varable import set_value
from gui.ui.globel_varable import get_value

def check_dt1_dt2(dt1: TransactionDateTime, dt2: TransactionDateTime) -> bool:
    
    dt1_bigger_than_dt2 = False
    dt_1 = datetime(dt1.year, dt1.month, dt1.day, dt1.hour, dt1.minute, dt1.second)
    dt_2 = datetime(dt2.year, dt2.month, dt2.day, dt2.hour, dt2.minute, dt2.second)

    if dt_1 > dt_2:
        # print_log("dt1 晚于 dt2")
        dt1_bigger_than_dt2 = False
    elif dt_1 < dt_2:
        # print_log("dt1 早于 dt2")
        dt1_bigger_than_dt2 = True
    else:
        # print_log("dt1 等于 dt2")
        dt1_bigger_than_dt2 = True
    
    return dt1_bigger_than_dt2


def cmp_transaction_by_datetime(x: Transaction, y: Transaction) -> int:
    

    if check_dt1_dt2(x.get_datetime(), y.get_datetime()):
        return 1
    else:
        return -1
    

def delete_same_transaction(transactions: list) -> list:
    
    new_transactions = []
    transaction_ids = []
    for item in transactions:
        if isinstance(item, Transaction):
            transaction_id = str(item.transaction_number).replace(" ", "").replace("\t", "")
            
            if transaction_id not in transaction_ids:
                transaction_ids.append(transaction_id)
                new_transactions.append(item)
            else:
                print_log(f"{item.time_.get_v_str()}: {item.transaction_number}, has same transaction number.")
    return new_transactions


def check_number_is_float(number: str) -> bool:
    
    isFloat = False
    try:
        float(number)
    except:
        isFloat = False
    else:
        isFloat = True
    return isFloat


def get_batch_transactions_target_values(transactions: list, func: callable) -> list:
    
    batch_transactions = []
    
    for item in transactions:
        if not isinstance(item, Transaction):
            continue
        else:
            value = func(item)
            if check_number_is_float(str(value)):
                value_num = float(value)
                batch_transactions.append(value_num)
            else:
                print("Error:" + str(type(value)) + ":" + str(value))
    return batch_transactions



def analysis_all_bills(target_csv_files: list, csv_folder_path: str) -> list:
    
    all_transactions = []

    for item in target_csv_files:
        
        info = "Read transaction csv file: " + item
        print_log(info)
        transactions = ReadTransactionTable.open_csv(csv_file_path=item,
                                                    head=False,
                                                    frist_line_word='交易时间')
        all_transactions.extend(transactions)
        
    all_transactions.sort(key=cmp_to_key(cmp_transaction_by_datetime))
    target_transactions = delete_same_transaction(all_transactions)
    print_log("All transactions count: " + str(len(target_transactions)) + ".")
    print_log("All transactions count: " + str(len(all_transactions)) + ".")
    set_value("all_transactions_as_list", target_transactions)
    return target_transactions


def save_transactions_to_file(all_transactions: list, transaction_file_path: str, head: list):
    
    target_transactions_list = []
    for item in all_transactions:
        if isinstance(item, Transaction):
            target_transactions_list.append(item.to_list())
    WriteTransactionTable.write_csv(csv_file_path=transaction_file_path,
                                    fields=head,
                                    rows=target_transactions_list)