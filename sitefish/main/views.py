# sitefish/main/views.py
import os

from starlette.responses import FileResponse, RedirectResponse


async def show_index(request):
    return request.app.jinja.TemplateResponse(
        'main/index.html',
        {'request': request})


async def show_page(request):
    page = request.path_params.get('page')
    if page == 'index.html':
        return RedirectResponse(request.url_for('index'), 301)
    template = f'main/{page}'
    return request.app.jinja.TemplateResponse(
        template,
        {'request': request})


async def show_favicon(request):
    if request.method == 'GET':
        base = os.path.dirname(os.path.dirname(__file__))
        return FileResponse(
            os.path.join(base, 'static', 'images', 'favicon.ico'))
