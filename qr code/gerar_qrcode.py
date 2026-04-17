import qrcode

# Conteúdo do QR Code (pode ser link, texto, etc.)
conteudo = "https://lean16w.github.io/"

# Criar QR Code
qr = qrcode.make(conteudo)

# Salvar imagem
qr.save("qrcode.png")

print("QR Code gerado com sucesso: qrcode.png")
