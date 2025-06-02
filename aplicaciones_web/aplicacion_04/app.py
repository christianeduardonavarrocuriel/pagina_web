import web

urls = (
    '/', 'Index',
    '/bienvenida','Bienvenida'
)

render = web.template.render('templates')
app = web.application(urls, globals())

class Index:

    def __init__(self):
        self.mensaje = "Este es un el index"

    def GET(self):
        return render.index(self.mensaje)
    
class Bienvenida:
    def __init__(self):
        pass

        mensaje = "Esta es la Bienvenida"
        return render.bienvenida(self.mensaje)
    



if __name__ == "__main__":
    app.run()
