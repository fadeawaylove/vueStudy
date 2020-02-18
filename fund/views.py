from django.shortcuts import render
from .spiders import QieManSpider
# Create your views here.


def index(requests):

    return render(requests, "fund/fund.html")


def search(requests):
    """显示基金的基本信息
    base_info: {
        "基金公司"：属于哪个基金公司.
        "晨星评级"：三年、五年.
        "当日涨跌估计图"：,
        "直达链接"： 1到晨星，2到天天基金，3到且慢（点击到对应的网站去看详细信息）
        "当前基金规模"：总共募集了多少钱
        "持仓情况"
        "历史涨跌"：从开始到现在的历史涨跌图（拆分为近 1 2 3 4 5年，今年以来，近1 3 6 月）
    }
    """

    fund_code = requests.GET.get("fund_code")
    fund_data = QieManSpider.search(fund_code)

    return render(requests, "fund/fund.html", context={"fund_data": fund_data})

