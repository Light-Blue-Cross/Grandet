#/bin/bash python3

rules = {
    "住宿费用": {
        "酒店住宿": {
            "0": {"name": "交易分类", "operation": "包含", "value": "住宿费用"},
        },
        "房租": {
            "0": {"name": "收款人", "operation": "包含", "value": "房东"},
            "1": {"name": "收款人", "operation": "包含", "value": ""},
            "2": {"name": "收款人", "operation": "包含", "value": ""},
        },
        "中介担保": {
            
        },
        "水费": {
            
        },
        "电费": {
            
        },
        "网费": {
            
        },
        "燃气费": {
            
        },
        "取暖费": {
            
        },
        "其他": {
            
        }
    },
    "餐饮美食": {
        "朋友聚餐": {
            "0": {"name": "交易分类", "operation": "包含", "value": "餐饮美食"},
            "1": {"name": "金额", "operation": "大于", "value": "200"},
        },
        "日常外卖": {
            "0": {"name": "交易分类", "operation": "包含", "value": "餐饮美食"},
            "1": {"name": "交易对方", "operation": "包含", "value": "饿了吗"},
        },
        "优惠团购": {
            "0": {"name": "交易分类", "operation": "包含", "value": "餐饮美食"},
        },
        "到店吃饭": {
            "0": {"name": "交易分类", "operation": "包含", "value": "餐饮美食"},
            "1": {"name": "金额", "operation": "大于", "value": "200"},
        },
        "其他": {
            "0": {"name": "交易分类", "operation": "包含", "value": "餐饮美食"}
        }
    },
    "交通出行": {
        "上班通勤": {
            "0": {"name": "交易分类", "operation": "包含", "value": "交通出行"},
            "1": {"name": "交易对方", "operation": "不包含", "value": "轨道交通"},
        },
        "市内出行": {
            "0": {"name": "交易分类", "operation": "包含", "value": "交通出行"},
            "1": {"name": "交易对方", "operation": "包含", "value": "轨道交通"},
        },
        "跨市出行": {
            "0": {"name": "交易分类", "operation": "包含", "value": "交通出行"},
            "1": {"name": "交易对方", "operation": "包含", "value": "铁路12306"},
            "2": {"name": "交易对方", "operation": "包含", "value": "票务"},
        }

    },
    "日用百货": {
        "体检": {
            "0": {"name": "交易分类", "operation": "包含", "value": "扫二维码付款"},
        }

    },
    "医疗保健": {
        "体检": {
            "0": {"name": "交易分类", "operation": "包含", "value": "FAFULI"},
        },
        "买药": {},
        "挂号": {}
    },
    "生活服务": {
        "寄送快递": {
            "0": {"name": "交易分类", "operation": "包含", "value": "生活服务"},
            "1": {"name": "交易对方", "operation": "包含", "value": "顺丰"},
        },
        "美容美发": {
            "0": {"name": "交易分类", "operation": "包含", "value": "美容美发"},
        },
        "洗化用品": {
            "0": {"name": "交易分类", "operation": "包含", "value": "美容美发"},
            "1": {"name": "交易对方", "operation": "包含", "value": "天猫"},
        },
        "服饰装扮": {
            
        },
        
    },
    "信息订阅": {
        "充值缴费": {
            "0": {"name": "交易分类", "operation": "包含", "value": "充值缴费"},
            "1": {"name": "交易对方", "operation": "包含", "value": "中国移动"},
        },
    },
    "公共服务": {
        "证件办理": {
            "0": {"name": "交易分类", "operation": "包含", "value": "公共服务"},
            "1": {"name": "交易对方", "operation": "包含", "value": "证件费"},
        }
    },
    "娱乐休闲": {

    },
    "投资理财": {

    },
    "信用借还": {
        "朋友转账": {},
    },
    "个人转账": {
        "账户存取": {},
        "微信红包": {}
    },
    "教育培训": {
        
    },
    "职业收入": {
        "": {},
    },
    "数码电器": {
        "": {}
    }
}

key_word = ['餐饮美食', '投资理财', '生活服务', '日用百货', '交通出行', '信用借还', '酒店旅游', '收入', '账户存取',
    '退款', '商业服务', '文化休闲', '充值缴费', '爱车养车', '转账红包', '教育培训', '美容美发', '服饰装扮',
    '医疗健康', '数码电器', '其他', '家居家装', '母婴亲子', '运动户外', '保险', '交易类型', '商户消费',
    '转账', '微信红包（单发）', '扫二维码付款', '转账-退款', '微信红包', '零钱提现', '零钱充值',
    '微信红包-退款', '群收款', '小芒特权-退款', '微信红包（群红包）', '二维码收款', 'FAFULI-退款']