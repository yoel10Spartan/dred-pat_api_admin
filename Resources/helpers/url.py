class URL:
    @staticmethod
    def prepare(url: str):
        list_parts = url.split('/')
        return '/'.join([' '.join(i.split('__')) for i in list_parts])