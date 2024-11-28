import sys

def createReport(reportName):
    if(reportName == "relatorioDeCampanhas"):
        print("Relatório Criado")
        return [
            {"data": "2024-01-01" , "campanha": "celulares", "custo": 5000},
            {"data": "2024-01-02" , "campanha": "celulares", "custo": 250},
            {"data": "2024-01-03" , "campanha": "celulares", "custo": 10000}
        ]
    else:
        return None

def saveFile(parquetFileName):
    print("arquivo salvo")
    pass

def extractGoogleAdsReportAPI(reportName, parquetFileName):
    dados = createReport(reportName)
    if(dados == None):
        print("######## ERRO AO GERAR O relatório: nome esperado relatorioDeCampanhas")
    else:
        print(dados)
                    saveFile()
    
    return dados

def main():
    extractGoogleAdsReportAPI("relatorioDecampanhas", "dados-de-janeiro.parquet")

if __name__ == '__main__':
    sys.exit(main())