form selenium import webdrive

navegador  = webdrive.Chrome()
navegador.get('https://login.live.com/')
navegador.fild_element_by_xpath('//*[@id="i0116"]').send_keys('rafael@gmail')
navegador.fild_element_by_xpath('//*[@id="i0116"]').click()
navegador.fild_element_by_xpath('//*[@id="i0116"]').send_keys('rafael@gmail')
navegador.fild_element_by_xpath('//*[@id="i0116"]').click()



