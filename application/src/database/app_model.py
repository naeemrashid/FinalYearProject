class App:
    def __init__(self,title,subtitle,desc,icon,download_url,service,app_url):
        self._title=title
        self._subtitle=subtitle
        self._desc=desc
        self._icon=icon
        self._download_url=download_url
        self._service=service
        self._app_url=app_url
    def get_app(self):
        return {'title':self._title,
                'subtitle':self._subtitle,
                'description':self._desc,
                'icon':self._icon,
                'download_url':self._download_url,
                'service':self._service,
                'app_url':self._app_url}
    def get_service_name(self):
        return self._service
    def get_title(self):
        return self._title