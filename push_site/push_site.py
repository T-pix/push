from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl

driver = webdriver.Edge()
driver.get('https://www.kabum.com.br/hardware/ssd-2-5/ssd-pcie-nvme')

nome_prod = driver.find_elements(By.XPATH,"//span[@class='sc-d79c9c3f-0 nlmfp sc-cdc9b13f-16 eHyEuD nameCard']")
preco_prod = driver.find_elements(By.XPATH,"//span[@class='sc-620f2d27-2 bMHwXA priceCard']")

workbook = openpyxl.Workbook()
workbook.create_sheet('produtos')

sheet_produtos = workbook['produtos']
sheet_produtos['A1'].value = 'Produto'
sheet_produtos['B1'].value = 'Preço'

for nome, preco in zip(nome_prod, preco_prod):
    sheet_produtos.append([nome.text,preco.text])



workbook.save('produtos.xlsx')
#//span[@class='sc-620f2d27-2 bMHwXA priceCard']
#//span[@class='sc-d79c9c3f-0 nlmfp sc-cdc9b13f-16 eHyEuD nameCard']