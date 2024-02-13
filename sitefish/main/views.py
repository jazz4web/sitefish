# sitefish/main/views.py

import os

from starlette.exceptions import HTTPException
from starlette.responses import FileResponse, RedirectResponse

from ..dirs import static, templates


async def show_index(request):
    return request.app.jinja.TemplateResponse(
        'main/index.html',
        {'request': request})


async def show_page(request):
    page = request.path_params.get('page')
    if page == 'index.html':
        return RedirectResponse(request.url_for('index'), 301)
    template = f'main/{page}'
    tf = os.path.join(templates, template)
    if not os.path.exists(tf):
        raise HTTPException(
            status_code=404, detail='Такой страницы у нас нет.')
    return request.app.jinja.TemplateResponse(
        template,
        {'request': request})


async def show_favicon(request):
    if request.method == 'GET':
        return FileResponse(
            os.path.join(static, 'images', 'favicon.ico'))
