'use strict';
{
    window.addEventListener('load',
        function () {
            const $ = django.jQuery; // add jQuery
            const asyncReplacementObjectIdContainer = 'field-async_replacement_object_id'; // Контейнер селекта замены
            const asyncOriginalObjectIdContainer = 'field-async_original_object_id'; // Контейнер селекта оригинала
            const contentTypeSelectorId = 'id_content_type';  // Селектор ContentType
            const contentTypeSelectorContainer = 'field-content_type';  // Селектор ContentType
            const suggestUrl = '/admin/duplicate_handler/duplicatehandler/content_type/suggest/';
            const asyncOriginalObjectIdSelect = 'id_async_original_object_id'; // Селект оригинала
            const asyncReplacementObjectIdSelect= 'id_async_replacement_object_id'; // Селект замены
            const emptyChoice = '------';
            const originalHiddenSelectId = 'id_original_object_id';
            const replacementHiddenSelectId = 'id_replacement_object_id';
            const defaultErrorMessage = 'Обязательно к заполнению';
            const validatedInputContainers = [
                asyncReplacementObjectIdContainer,
                asyncOriginalObjectIdContainer,
                contentTypeSelectorContainer,
            ];
            const selectForAsyncUpdate = [asyncOriginalObjectIdSelect, asyncReplacementObjectIdSelect];
            const selectOptionsContainers = [asyncReplacementObjectIdContainer, asyncOriginalObjectIdContainer];

            const disabledInput = function () {
                $('input[type=submit]').prop('disabled', true);
            };
            const enabledInput = function () {
                $('input[type=submit]').prop('disabled', false);
            };

            const deleteErrorMessage = function (containerId) {
                $(`.${containerId} .errorlist`).remove();
            }

            const pushErrorMessage = function (containerId, errorMessage=defaultErrorMessage) {
                let errorHtml = `<ul class="errorlist"><li>${errorMessage}</li></ul>`;
                $(`.${containerId}`).prepend(errorHtml);
            };

            const checkEmptyValue = function (containerId) {
                if (!Boolean($(`.${containerId} select`).val())) return true;
                return false;
            };

            const validateInput = function () {
                let validationResult = true;
                disabledInput();
                $.each(validatedInputContainers, function (index, value) {
                    deleteErrorMessage(value);
                    if (checkEmptyValue(value)) {
                        pushErrorMessage(value);
                        validationResult = false;
                    }
                });
                if (validationResult) {
                        enabledInput();
                    }
            };

            const setValueInHiddenSelect = function (hiddenSelectId, value) {
                $(`#${hiddenSelectId}`).attr('value', value);
            };

            const showContainer = function (containerClass) {
                $(`.${containerClass}`).show();
            };
            const hideContainer = function (containerClass) {
                $(`.${containerClass}`).hide();
            };

            const createSelectOptions = function (data) {
                let selectOptions = [];
                selectOptions.push(`<option value selected>${emptyChoice}</option>`);
                $.each(data, function (index, value) {
                    selectOptions.push(`<option value="${value.value}" >${value.label}</option>`);
                });
                return selectOptions;
            };

            const deleteOptions = function (selectId) {
                $(`#${selectId}`).empty();
            };
            const pushOption = function (selectId, options) {
                $(`#${selectId}`).append(options);
            };
            const eachContainers = function (array, func) {
                $.each(array, function (index, value) {
                    func(value);
                });
            };

            const setOptions = function (data) {
                let selectOptions = createSelectOptions(data);
                eachContainers(selectOptionsContainers, hideContainer);
                eachContainers(selectForAsyncUpdate, deleteOptions);
                eachContainers(
                    selectForAsyncUpdate,
                    function (selectId) {
                        pushOption(selectId, selectOptions);
                    }
                );
                eachContainers(selectOptionsContainers, showContainer);
            };

            const getSuggestData = function (contentTypeId) {
                $.ajax({
                    url: suggestUrl + contentTypeId,
                    method: 'get',
                    dataType: 'json',
                    success: function (data) {
                        setOptions(data);
                    }
                });
            };
            eachContainers(selectOptionsContainers, hideContainer);
            $(`#${contentTypeSelectorId}`).on(
                'change',
                function() {
                    getSuggestData($(this).val());
                    validateInput();
                }
                );
            $(`#${asyncOriginalObjectIdSelect}`).on(
                'change',
                function() {
                    setValueInHiddenSelect(originalHiddenSelectId, $(this).val());
                    validateInput();
                }
                );
            $(`#${asyncReplacementObjectIdSelect}`).on(
                'change',
                function() {
                    setValueInHiddenSelect(replacementHiddenSelectId, $(this).val());
                    validateInput();
                }
                );
        });
}