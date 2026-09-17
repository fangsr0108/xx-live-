import pandas as pd

# 导入表
df_ab_test_exposure = pd.read_csv('data/ab_test_exposure.csv', encoding='utf-8')
df_anchor_base_info = pd.read_csv('data/anchor_base_info.csv', encoding='utf-8')
df_gift_transaction_log = pd.read_csv('data/gift_transaction_log.csv', encoding='utf-8')
df_guild_info = pd.read_csv('data/guild_info.csv', encoding='utf-8')
df_live_room_daily = pd.read_csv('data/live_room_daily.csv', encoding='utf-8')
df_user_base_info = pd.read_csv('data/user_base_info.csv', encoding='utf-8')
df_user_behavior_daily = pd.read_csv('data/user_behavior_daily.csv', encoding='utf-8')

#检查空值
df = (df_guild_info, df_live_room_daily, df_user_base_info, df_user_behavior_daily,
      df_ab_test_exposure, df_anchor_base_info, df_gift_transaction_log)
# for table in df:
#     print(table.isnull().sum())

#填充空值
fill_values = {
    'gender': 0,
    'age': 0,
    'network_type': 0,
    'pk_participate_count': -1,
    'active_hour': -1,
    'content_category_main': 0,
    'behavior_tier': 0,
    'stage': 0
}

df_user_behavior_daily.fillna(fill_values, inplace=True)
df_user_base_info.fillna(fill_values, inplace=True)

# 检查异常值

# for table in df:
#     print('------------')
#     print("------------")
#     print("------------")
#     with pd.option_context(
#             'display.max_rows', None,
#             'display.max_columns', None ):
#         print(table.describe())

# 用户日常行为表中总观看时长异常值剔除
outlier_index = df_user_behavior_daily[
    (df_user_behavior_daily['total_duration'] >= 86400) |
    (df_user_behavior_daily['total_duration'] < 0) ].index
df_user_behavior_daily.drop(outlier_index, inplace=True)

for table in df:
    print('------------')
    print("------------")
    print("------------")
    with pd.option_context(
            'display.max_rows', None,
            'display.max_columns', None ):
        print(table.describe())