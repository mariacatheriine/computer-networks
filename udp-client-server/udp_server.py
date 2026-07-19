import socket
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(("", 9000))
print("Server is running...")
data, addr = server.recvfrom(1024)
sentence = data.decode()
print("Message received:", sentence)
words = sentence.split()
translated = []
translations = {"tbh":"to be honest", "ig":"i guess", "atm":"at the moment", "irl":"in real life", "brb":"be right back","omg":"oh my god", "nvm":"never mind", "idk":"i don't know", "ttly":"talk to you later", "btw":"by the way"}
for word in words:
    clean = word.strip(".,!?").lower()
    if clean in translations:
        punctuation = ""
        if word[-1] in ".,!?":
            punctutation = word[-1]
        translated_word = translations[clean] + punctuation
        translated.append(translated_word)
    else:
        translated.append(word)
result = " ".join(translated)
print("Translated sentence:", result)
server.sendto(result.encode(), addr)
server.close()