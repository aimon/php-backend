from rest_framework_nested import routers


class OptionalSlashRouter(routers.SimpleRouter):
    def __init__(self):
        self.trailing_slash = "/?"
        super(routers.SimpleRouter, self).__init__()


class OptionalSlashNestedRouter(routers.NestedSimpleRouter):
    def __init__(self):
        self.trailing_slash = "/?"
        super(routers.NestedSimpleRouter, self).__init__()
