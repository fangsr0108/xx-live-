import pandas as pd
from sqlalchemy import create_engine

from data_cleaning import (
    df_user_base_info,
    df_anchor_base_info,
    df_user_behavior_daily,
    df_live_room_daily,
    df_gift_transaction_log,
    df_ab_test_exposure,
    df_guild_info,
)

# 1. 创建数据库连接（请替换为你的真实密码和数据库名）
engine = create_engine("mysql+pymysql://root:88888888@localhost:3306/user_behavior_db")

# 2. 严格按照业务依赖顺序排列你的 DataFrame 变量
# 假设你清洗后的 DataFrame 分别叫 df_user、df_anchor 等
data_packages = [
    {"name": "user_base_info", "df": df_user_base_info},
    {"name": "anchor_base_info", "df": df_anchor_base_info},
    {"name": "user_behavior_daily", "df": df_user_behavior_daily},
    {"name": "live_room_daily", "df": df_live_room_daily},
    {"name": "gift_transaction_log", "df": df_gift_transaction_log},
    {"name": "ab_test_exposure", "df": df_ab_test_exposure},
    {'name': 'guild_info', 'df': df_guild_info}  # 在此补充第7张表
]

print("开始批量导入数据库...")

for package in data_packages:
    table_name = package["name"]
    df_to_import = package["df"]

    print(f"正在写入表: {table_name}，总计 {len(df_to_import)} 条数据...")

    try:
        # 3. 执行写入
        # if_exists='append' 表示追加数据（如果之前建立了空表）
        # chunksize=50000 表示每5万条抓取一次写入，防止大文件卡死
        df_to_import.to_sql(
            name=table_name,
            con=engine,
            if_exists="append",
            index=False,
            chunksize=50000,
        )
        print(f"表 {table_name} 导入成功！")

    except Exception as e:
        print(f"表 {table_name} 导入失败，错误原因: {e}")

print("所有数据处理并导入完毕！")
