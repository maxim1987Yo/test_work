from celery import shared_task

from duplicate_handler.models import DuplicateHandler, DuplicateHandlerStatus
from duplicate_handler.services import DuplicateHandlerService


@shared_task
def duplicate_handler_task(handler_id):
    try:
        service = DuplicateHandlerService(handler_id)
        service.transfer()
    except Exception as e:
        handler = DuplicateHandler.objects.filter(pk=handler_id).first()
        handler.status = DuplicateHandlerStatus.FAILED
        handler.errors = str(e)
        handler.save()
