# passo a passo do projeto:
# passo 0: baixar o framework
# passo 1: título;
# passo 2: botão inicial: Iniciar no chat
# passo 3: popup/alerta
    #titulo: Bem-vindo
    # campo de texto: Digite seu nome
    # Botão: Entrar no chat
        #sumir título e botão inicial
        #fechar popup
        #criar o chat
            #campo de texto: Digite sua mensagem
            #Botão: Enviar
                #Mensagem no chat com o nome do usuário


import flet as ft

def main(pagina):
    titulo_pag_inicial = ft.Text("Central de Comunicação")
    titulo_janela = ft.Text("Bem-vindo a Central de Comunicação!")
    campo_usuario= ft.TextField(label='Digite seu nome')

    def enviar_mensagem(evento):
        mensagem_enviada = f"{campo_usuario.value}: {campo_mensagem.value}"
        pagina.pubsub.send_all(mensagem_enviada)
        campo_mensagem.value = ''
        pagina.update()

    campo_mensagem = ft.TextField(label="Digite sua mensagem", on_submit=enviar_mensagem) 

    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    linha_mensagem = ft.Row([campo_mensagem, botao_enviar])
    chat = ft.Column()
    def criar_chat(evento):
        pagina.remove(titulo_pag_inicial)
        pagina.remove(botao_inicial)
        janela_popup.open = False
        pagina.add(linha_mensagem)
        pagina.add(chat)
        mensagem_login = f'{campo_usuario.value} entrou no chat'
        chat.controls.append(ft.Text(mensagem_login))
        pagina.update()

    botao_chat = ft.ElevatedButton("Entrar", on_click=criar_chat)

    janela_popup = ft.AlertDialog(
        title= titulo_janela,
        content= campo_usuario,
        actions= [botao_chat]
    )
    
    def abrir_popup(evento):
        pagina.dialog = janela_popup
        janela_popup.open = True
        pagina.update()


    botao_inicial = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)

    def tunel_mensagem(mensagem):
        chat.controls.append(ft.Text(mensagem))
        pagina.update()
    pagina.pubsub.subscribe(tunel_mensagem)

    pagina.add(titulo_pag_inicial)
    pagina.add(botao_inicial)

ft.app(target=main, view=ft.WEB_BROWSER)