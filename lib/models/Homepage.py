from lib.models import Page



class Homepage(Page):
    """
    课工场网站首页模型
    """

    url = "http://www.kgc.cn"

    def act_teachers(self):
        """
        进入金牌讲师界面
        """
        more_button = self.driver.find_element_by_css_selector("div.good-teacher span.title-r a")

        more_button.click()