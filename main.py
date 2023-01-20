import fastapi.responses
from fastapi import FastAPI
import uvicorn
import jinja2

app = FastAPI()
templateLoader = jinja2.FileSystemLoader(searchpath="./templates")
templateEnv = jinja2.Environment(loader=templateLoader)
headerTemplate = templateEnv.get_template("components/header.html.jinja2")
navbarTemplate = templateEnv.get_template("components/navbar.html.jinja2")
homeTemplate = templateEnv.get_template("home.html.jinja2")
contactTemplate = templateEnv.get_template("contact.html.jinja2")
projectTemplate = templateEnv.get_template("projects.html.jinja2")
blogTemplate = templateEnv.get_template("blog.html.jinja2")
homePage = homeTemplate.render(header=headerTemplate.render(),
                               navbar=navbarTemplate.render())
contactPage = contactTemplate.render(header=headerTemplate.render(),
                                     navbar=navbarTemplate.render())
projectPage = projectTemplate.render(header=headerTemplate.render(),
                                     navbar=navbarTemplate.render())
blogPage = blogTemplate.render(header=headerTemplate.render(),
                               navbar=navbarTemplate.render())



@app.get("/", response_class=fastapi.responses.HTMLResponse)
def homepage():
    return homePage

@app.get("/contact", response_class=fastapi.responses.HTMLResponse)
def contact():
    return contactPage

@app.get("/projects", response_class=fastapi.responses.HTMLResponse)
def projects():
    return projectPage

@app.get("/blogs", response_class=fastapi.responses.HTMLResponse)
def blogs():
    return blogPage

if __name__ == "__main__":
    '''Uvicorn is the ASGI used to run the server'''
    uvicorn.run(app,
                host="0.0.0.0",
                port=80,
                log_level="debug")