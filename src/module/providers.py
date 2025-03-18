from dependency_injector import providers


class ApplicationScoped(providers.Singleton):
    pass


class RequestScoped(providers.ContextLocalSingleton):
    pass


class RouteProvider(providers.Singleton):
    pass


class UseCaseProvider(providers.Singleton):
    pass
