'''
1.批量执行脚本，批量执行部分用例，或者批量执行所有用例。
2.生成测试报告。
3.把生成的测试报告通过邮件发送给相关人。
4.脚本执行过程中，相关的日志打印。
'''
import unittest
import time
import HTMLTestRunner
import yagmail
import logging


# 配置日志的输出文件，以及文件的打开方式   该方式是记录selenium日志  用于自己自动化脚本排错
# 在自动化脚本中加入print（）可以自定义日志   用于将自动化脚本注释打印到日志中排错
logging.basicConfig(level=logging.DEBUG,  #critical error warning info debug 日志事件级别  严重信息>>>详细信息
          filename=r'E:\pychon-code\app_auto_scirpt\log\yijiaminsu.txt', #输出日志的保存路径
          filemode='a',  # a表示追加的模式打开文件
          format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')  #保存的格式

# 选取要执行的脚本文件
def discover_all_cases():
    discover=unittest.defaultTestLoader.discover(r"E:\pychon-code\app_auto_scirpt\po\test_cases\\",pattern="login*.py")
    print(discover)
    return discover
    pass



if __name__ == '__main__':
    # unittest.TextTestRunner().run(discover_all_cases())
    # 批量执行脚本


    # 生成测试报告
    now = time.strftime("%Y-%m-%d %H_%M_%S")    # 获取当前系统的时间
    report_path = r"E:\pychon-code\app_auto_scirpt\report\\" +now + "_RC_103.html"
    # 生成报告的存储路径   并定义报告的名称

    fp = open(report_path, "wb") # 打开报告存储路径   wb表示 二进制写入

    # 使用HTMLTestRunner模块展示测试报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="this is a auto_testreport", description="测试用例执行情况如下显示")
    #                                        stream是数据的流向          title是页面标题                description页面内容
    runner.run(discover_all_cases())   #批量执行脚本
    fp.close()



    # 发送邮件
    # 连接邮箱服务器
    yag = yagmail.SMTP(user='fxd604083914@163.com', password='PFSIEANXFQZZLSVM', host='smtp.163.com')#user 是发送者的邮箱   password是邮箱的授权码   host是服务器的域名
    # 邮箱正文
    contents = ['hello,测试报告在附件中，请查收！']
    # 给单用户发送邮件并添加多个附件
    yag.send('fengxiaodng777@163.com','一家民宿app测试报告',contents,attachments=report_path)
    #  被发送的邮箱地址    attachments是发送的附件  本地的路径
    #  发送多个附件时：attachments=[报告1，报告2，报告3]


