# 這個檔案儲存業務諮詢欄位的同義詞
# 將會對應到資料庫中存取的欄位


brief = ['簡介', '介紹']
time = ['開始', '期限', '截止', '時限', '日期']
details = ['詳細', '更多']
requirements = ['繳交', '文件', '審查', '需求', '需要']
qualification = ['條件', '資格', '限制']
notice = ['留意', '注意', '提醒']
all_conditions = brief + time + details + requirements + qualification + notice


def conditions_in_sentence(sentence):
    return any(cond in sentence for cond in all_conditions)