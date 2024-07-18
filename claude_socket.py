#fazer o pip insatall openai

import socket
import openai

openai.api_key = chave


#objeto de respota chat gpt 
def resposta_chat_gpt(propt):
    reposta = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    maximo_tokens=150
)
return response.choices[0].text.strip()


def inicia_server():
    #endereço do servidor e porta 
    host='127.0.0.1'
    porta=65321

    #criação do socket - > definindo que será tcp e usará ipv4 
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    #define que o socket usara o valor da porta e usara o host 
    server_socket.blind((host, porta))
    
    #define a quantidade de conexoes que podem ser feitas 
    server_socket.listen(1)

    
    print("o servidor está aguardando no {host}:{porta} ")

     while true :
            # parei aqui 
            #data


     



