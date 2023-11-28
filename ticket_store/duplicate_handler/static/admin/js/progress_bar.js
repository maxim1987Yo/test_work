{
    window.addEventListener('load',
        function () {
            const $ = django.jQuery;
            const handlerId = 'transfer_' + $('#progress-wrapper').attr('object_id');
            const progressUrl = '/admin/duplicate_handler/duplicatehandler/progress/';
            const updateProgress = function (progress) {
                $('#progress-bar').css('width', progress.percent + "%");
                $('#progress-bar-message').html(progress.percent + ' из ' + 100);
                if (progress.finished) {
                    location.reload();
                }
            };
            const getProgress = function () {
                $.ajax({
                    url: progressUrl + handlerId,
                    method: 'get',
                    dataType: 'json',
                    success: function (data) {
                        updateProgress(data);
                    }
                });
            };
            setInterval(getProgress, 1000);
        }
    );
}