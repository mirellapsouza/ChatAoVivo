import flet as ft

# funcao principal
def main(pagina):

    def abrir_modal(evento):
        pagina.dialog = modal
        modal.open = True
        pagina.update()
    

    def abrir_chat(evento):
        modal.open = False
        pagina.remove(titulo, botao_iniciar)
        pagina.add(chat, linha_enviar_chat)
        usuario = usuario_modal.value

        texto_chat = f"{usuario} entrou no chat"
        pagina.pubsub.send_all(texto_chat)
        
        pagina.update()


    def enviar_mensagem(evento):
        nome_usuario = usuario_modal.value
        mensagem_usuario = mensagem_chat.value
        mensagem_chat.value = ""  # limpa o campo

        texto_chat = f"{nome_usuario}: {mensagem_usuario}"
        pagina.pubsub.send_all(texto_chat)

        pagina.update()


    def enviar_mensagem_tunel(texto_chat):
        mensagem = ft.Text(texto_chat)
        chat.controls.append(mensagem)
        pagina.update()


    # elementos pagina inicial
    titulo = ft.Text("Chat Ao Vivo")
    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=abrir_modal)
    pagina.add(titulo, botao_iniciar)

    # elementos modal (pop-up alert)
    titulo_modal = ft.Text("Entre no chat")
    usuario_modal = ft.TextField(label="Digite o seu nome")
    botao_modal = ft.ElevatedButton("Entrar", on_click=abrir_chat)
    modal = ft.AlertDialog(title=titulo_modal, content=usuario_modal, actions=[botao_modal])

    # elementos pagina chat
    mensagem_chat = ft.TextField(label="Escreva...", on_submit=enviar_mensagem)
    botao_chat = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    linha_enviar_chat = ft.Row([mensagem_chat, botao_chat])
    chat = ft.Column()

    # tunel de comunicação
    pagina.pubsub.subscribe(enviar_mensagem_tunel)

ft.app(main, view=ft.WEB_BROWSER)