act_list = [
    {
     'act_name': '赚积分', 'aid': 1418,
     'if_task': True,  # 是否有任务
     'referer': 'https://hd.oppo.com/act/m/2021/jifenzhuanpan/index.html?us=gerenzhongxin&um=hudongleyuan&uc=yingjifen',
     'if_draw': False,  # 是否有抽奖活动，已修复抽奖，如不需要抽奖请自行修改为False
     'extra_draw_cookie': 'app_innerutm={"uc":"yingjifen","um":"hudongleyuan","ut":"direct","us":"gerenzhongxin"};',
     # 抽奖必要的额外cookie信息，请勿随意修改，否则可能导致不中奖
     'lid': 1307,  # 抽奖参数
     'draw_times': 3, # 控制抽奖次数3
     'end_time': '2033-8-18 23:59:59',  # 长期任务
     'text':'每次扣取0积分，任务获取次数'
     },
    {
     'act_name': 'realme积分大乱斗-8月', 'aid': 1582,
     'if_task': True,
     'referer': 'https://hd.oppo.com/act/m/2021/2021/realmejifendalu/index.html',
     'if_draw': False,  # 已修复抽奖，如不需要抽奖请自行修改为False
     'extra_draw_cookie': 'app_innerutm={"uc":"renwuzhongxin","um":"hudongleyuan","ut":"direct","us":"gerenzhongxin"};',
     'lid': 1466,
     'draw_times': 3,
     'end_time': '2022-8-31 23:59:59',
     'text':'每次扣取5积分，测试仍然可以中奖'
     },
    {
     'act_name': 'realme积分大乱斗-9月', 'aid': 1582,
     'if_task': True,
     'referer': 'https://hd.oppo.com/act/m/2021/2021/realmejifendalu/index.html?&us=realmenewshouye&um=yaofen&ut=right&uc=realmedaluandou',
     'if_draw': False,  # 已修复抽奖，如不需要抽奖请自行修改为False
     'extra_draw_cookie': 'app_innerutm={"uc":"renwuzhongxin","um":"hudongleyuan","ut":"direct","us":"gerenzhongxin"};',
     'lid': 1554, #抽奖接口与8月不一样，测试可以独立抽奖
     'draw_times': 3,
     'end_time': '2022-8-31 23:59:59',
     'text':'每次扣取5积分'
     },
    {
     'act_name': 'realme积分大乱斗-9月(2)', 'aid': 1598,
     'if_task': True,
     'referer': 'https://hd.oppo.com/act/m/2021/huantaishangchengjif/index.html?&us=realmeshouye&um=icon&ut=3&uc=realmejifendaluandou',
     'if_draw': False,  # 已修复抽奖，如不需要抽奖请自行修改为False
     'extra_draw_cookie': 'app_innerutm={"uc":"realmejifendaluandou","um":"icon","ut":"3","us":"realmeshouye"};',
     'lid': 1535,
     'draw_times': 3,
     'end_time': '2022-8-31 23:59:59',
     'text':'每次扣取10积分'
     },
    {
     'act_name': '天天积分翻倍', 'aid': 675,
     'if_task': False,  # 该活动没有任务
     'referer': 'https://hd.oppo.com/act/m/2019/jifenfanbei/index.html?us=qiandao&um=task',
     'if_draw': False,  # 已修复抽奖，如不需要抽奖请自行修改为False
     'extra_draw_cookie': 'app_innerutm={"uc":"direct","um":"zuoshangjiao","ut":"direct","us":"shouye"};',
     'lid': 1289,
     'draw_times': 1,
     'end_time': '2033-8-18 23:59:59',  # 长期任务
     'text':'每次扣取10积分'
     },
    {
     'act_name': '智能硬件0元抽奖', 'aid': 1588,
     'if_task': False,  # 该活动没有任务
     'referer': 'https://hd.oppo.com/act/m/2021/3719/index.html?us=iotchannel&um=icon',
     'if_draw': False,  # 已修复抽奖，如不需要抽奖请自行修改为False
     'extra_draw_cookie': 'app_innerutm={"uc":"direct","um":"icon","ut":"direct","us":"iotchannel"};',
     'lid': 1514,
     'draw_times': 3,
     'end_time': '2022-8-18 23:59:59',  # 活动8-5结束，实际还能玩
     'text':'每次扣取0积分'
     },
     {
     'act_name': '双十一活动', 'aid': 1768,
     'if_task': True,  
     'referer': 'https://hd.oppo.com/act/m/2021/choumiandan/index.html?us=shouye&um=youshangjiao&uc=2021oppowin',
     'if_draw': False,  # 已修复抽奖，如不需要抽奖请自行修改为False
     'extra_draw_cookie': 'app_innerutm={"uc":"direct","um":"direct","ut":"direct","us":"direct"};',
     'lid': 1586,
     'draw_times': 1,
     'end_time': '2021-11-13 23:59:59',  # 长期任务
     'text':'每次扣取5积分'
     }

]
