import qrcode
from fpdf import FPDF

def obter_valor_compra():
    while True:
        try:
            valor = float(input("Digite o valor da compra: R$ "))
            print(f"Valor recebido: R$ {valor}")
            return valor
        except ValueError:
            print("Erro: valor inválido! Insira um número.")

def gerar_qr_code(valor):
    dados_pagamento = f"https://meupagamento.com/pagar?valor={valor}"
    qr = qrcode.make(dados_pagamento)
    qr.save("qrcode_pagamento.png")
    print("QR Code gerado e salvo como 'qrcode_pagamento.png'.")

def gerar_recibo(valor):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Recibo de Pagamento", ln=True, align='C')
    pdf.cell(200, 10, txt="---------------------------", ln=True, align='C')
    pdf.cell(200, 10, txt=f"Valor da compra: R$ {valor:.2f}", ln=True, align='L')
    pdf.image("qrcode_pagamento.png", x=80, y=60, w=50, h=50)
    pdf.output("recibo_pagamento.pdf")
    print("Recibo gerado e salvo como 'recibo_pagamento.pdf'.")

def main():
    valor = obter_valor_compra()
    gerar_qr_code(valor)
    gerar_recibo(valor)

if __name__ == "__main__":
    main()
