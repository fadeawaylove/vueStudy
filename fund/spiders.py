import lxml
import logging


from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

class QieManSpider(object):
    """
    且慢爬虫
    爬取整个页面没必要 可以简单爬取关心的信息，然后详情按钮直接到对应的网站去，所以也需要爬取到网址
    """

    @staticmethod
    def search(fund_code):
        """

        :param fund_code: 基金代码
        :return: data : {
                "晨星评级",

                }
        """
        data = {}

        options = Options()
        options.add_argument('--headless')
        with webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',
                              desired_capabilities=DesiredCapabilities.CHROME,
                              options=options) as driver:
            # 从且慢获取相关信息
            driver.get("https://cn.morningstar.com/quickrank/default.aspx")

            a = driver.find_element_by_id("ctl00_cphMain_txtFund")
            a.click()
            a.send_keys(fund_code)
            b = driver.find_element_by_id("ctl00_cphMain_btnGo")
            b.click()

            try:
                row_elems = driver.find_element_by_class_name("gridItem").find_elements_by_tag_name("td")
            except NoSuchElementException:
                logging.warning("基金代码[{}]不存在！".format(fund_code))
                return {}

            data["starts_years3"] = row_elems[5].find_element_by_tag_name("img").get_attribute("src")
            data["starts_years5"] = row_elems[6].find_element_by_tag_name("img").get_attribute("src")
            data["fund_type"] = row_elems[4].text
            data["detail_url"] = row_elems[3].find_element_by_tag_name("a").get_attribute("href")


        return data


if __name__ == '__main__':

    QieManSpider.search("519674")







