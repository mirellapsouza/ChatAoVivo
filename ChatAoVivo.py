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

        mensagem_texto = ft.Text(f"{usuario} entrou no chat")
        chat.controls.append(mensagem_texto)
        
        pagina.update()


    def enviar_mensagem(evento):
        nome_usuario = usuario_modal.value
        mensagem_usuario = mensagem_chat.value
        mensagem_chat.value = ""  # limpa o campo

        mensagem_texto = ft.Text(f"{nome_usuario}: {mensagem_usuario}")
        chat.controls.append(mensagem_texto)

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


ft.app(main)