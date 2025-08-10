import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
import flet as ft
import solve_depedencia
import render_plane


def main(page: ft.Page):
    page.title = "Vetores com Matplotlib"
    page.scroll = ft.ScrollMode.AUTO
    page.window.maximized = True

    idx = [1]
    minha_div = ft.Column(height=400, spacing=10, scroll=ft.ScrollMode.AUTO)

    def add_vector(e):
        i = idx[0]
        linha = ft.Row(
            controls=[
                ft.TextField(label=f"VetX {i}", width=100),
                ft.TextField(label=f"VetY {i}", width=100),
                ft.TextField(label=f"Color {i}", width=100),
            ],
            spacing=10
        )
        minha_div.controls.append(linha)
        idx[0] += 1
        page.update()

    def remove_vector(e):
        if minha_div.controls:
            minha_div.controls.pop()
            idx[0] = max(1, idx[0] - 1)
            page.update()

    def send(e):
        for row in minha_div.controls:
            if any(field.value is None or field.value.strip() == "" for field in row.controls):
                _open_dialog("⚠️ Erro", "Preencha todos os campos antes de enviar.")
                return

        resultados = [
            [int(row.controls[0].value), int(row.controls[1].value), row.controls[2].value]
            for row in minha_div.controls
        ]

        # Chamada ao seu módulo
        try:
            render_plane.plt.close()
        except:
            pass
        
        resultado_texto = solve_depedencia.dependencia_linear(resultados)
        page.client_storage.set("resultado_texto", resultado_texto)
        page.go("/resultado")

        render_plane.model_geometric(resultados)

    def _open_dialog(titulo, mensagem):
        dlg = ft.AlertDialog(
            title=ft.Text(titulo),
            content=ft.Text(mensagem),
            actions=[ft.TextButton("OK", on_click=lambda e: _close_dialog())]
        )
        page.dialog = dlg
        dlg.open = True
        page.update()

    def _close_dialog():
        page.dialog.open = False
        page.update()

    def route_change(e):
        page.views.clear()
        if page.route == "/resultado":
            resultado = page.client_storage.get("resultado_texto") or "Nenhum resultado disponível"
            page.views.append(
                ft.View(
                    "/resultado",
                    controls=[
                        ft.Text("Resultado:", size=30),
                        ft.Text(resultado, selectable=True),
                        ft.ElevatedButton("Voltar", on_click=lambda _: page.go("/"))
                    ]
                )
            )
        else:
            # Página principal com entrada de vetores
            page.views.append(
                ft.View(
                    "/",
                    controls=[
                        ft.Text("Representação de Vetores", size=30),
                        minha_div,
                        ft.Row([
                            ft.ElevatedButton("Adicionar Vetor", on_click=add_vector),
                            ft.ElevatedButton("Remover Vetor", on_click=remove_vector),
                            ft.ElevatedButton("Enviar", on_click=send, bgcolor=ft.Colors.GREEN)
                        ], spacing=10)
                    ]
                )
            )
        page.update()

    page.on_route_change = route_change
    page.go(page.route)

ft.app(target=main, view=ft.AppView.FLET_APP)
