
def pushInService(self):
    self.service.push(self)

# def PushInService(service):
#     def onDecorator(aClass):
#         import configuration.cfg
#         aClass.service = configuration.cfg.App().getObject(service)
#         aClass.pushInService = pushInService
#         return aClass
#     return onDecorator

# def Component(lifestile):
#     def onDecorator(aClass):
#         App().pinsor.addcomponent(
#             aClass, lifestyle = lifestile
#         )
#         return aClass
#     return onDecorator