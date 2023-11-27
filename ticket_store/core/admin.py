from django.contrib import admin

from core.models import Bus, RouteStop, Route, Company, Schedule, Stop, Ticket


admin.site.register(Bus)
admin.site.register(RouteStop)
admin.site.register(Route)
admin.site.register(Company)
admin.site.register(Schedule)
admin.site.register(Stop)
admin.site.register(Ticket)

