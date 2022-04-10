from django.contrib import admin


class InputFilter(admin.SimpleListFilter):
    template = 'admin/input_filter.html'

    def lookups(self, request, model_admin):
        # Dummy, required to show the filter.
        return ((),)

    def choices(self, changelist):
        # Grab only the "all" option.
        all_choice = next(super().choices(changelist))
        all_choice['query_parts'] = (
            (k, v)
            for k, v in changelist.get_filters_params().items()
            if k != self.parameter_name
        )
        yield all_choice


class IpFilter(InputFilter):
    parameter_name = 'ip'
    title = 'ip'

    def queryset(self, request, queryset):
        if self.value() is not None:
            path = self.value()

            return queryset.filter(
                ip__icontains=path
            )
