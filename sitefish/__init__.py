# sitefish/__init__.py
import os

import jinja2
import typing

from starlette.applications import Starlette
from starlette.routing import Mount, Route
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from webassets import Environment as AssetsEnvironment
from webassets.ext.jinja2 import assets

from .dirs import base, static, templates, settings
from .errors import show_error
from .main.views import show_index, show_favicon, show_page

DI = '''typing.Union[str, os.PathLike[typing.AnyStr],
typing.Sequence[typing.Union[str,
os.PathLike[typing.AnyStr]]]]'''.replace('\n', ' ')


class J2Templates(Jinja2Templates):
    def _create_env(
            self,
            directory: DI, **env_options: typing.Any) -> "jinja2.Environment":
        loader = jinja2.FileSystemLoader(directory)
        assets_env = AssetsEnvironment(static, '/static')
        assets_env.debug = settings.get('ASSETS_DEBUG', bool)
        env_options.setdefault("loader", loader)
        env_options.setdefault("autoescape", True)
        env_options.setdefault("extensions", [assets])
        env = jinja2.Environment(**env_options)
        env.assets_environment = assets_env
        return env


errs = {404:show_error}

app = Starlette(
    debug=settings.get('DEBUG', cast=bool),
    routes=[
        Route('/', show_index, name='index'),
        Route('/favicon.ico', show_favicon, name='favicon'),
        Route('/{page}', show_page, name='page'),
        Mount('/static', app=StaticFiles(directory=static), name='static')],
    exception_handlers=errs)
app.config = settings
app.jinja = J2Templates(directory=templates)
