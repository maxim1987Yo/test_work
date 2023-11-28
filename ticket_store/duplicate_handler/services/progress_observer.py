from django.core.cache import cache


class ProgresObserver:
    def __init__(self, itm_count: int, cache_id: str):
        self.progress = 0
        self.itm_count = itm_count
        self.cache_id = cache_id
        self.finished = False

    def _calculate_progress(self, current_value: int) -> int:
        progress = (current_value * 100) / self.itm_count
        return int(progress)

    def _get_progress(self, itm: int):
        progress = self._calculate_progress(itm)
        if progress >= 100:
            self.finished = True
        return {'finished': self.finished, 'percent': progress}

    def set_progress(self, itm: int):
        cache.set(self.cache_id, self._get_progress(itm), 50)
