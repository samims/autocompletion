from itertools import chain

from django.db.models.functions import Length
from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView

# local imports
from .models import Dictionary


class AutoCompleteView(View):
    def get(self, request, *args, **kwargs):
        # checking if ajax request or not
        if request.is_ajax():
            query_string = request.GET.get("word", "")

            results = Dictionary.objects.filter(word__icontains=query_string).distinct()
            exact_match = results.filter(word__iexact=query_string)  # checking if exact match found
            # filtering out startswith query word
            first_ranked_qs = results.filter(word__startswith=query_string).order_by(
                "-frequency", Length("word").asc()
            )
            # excluding startswith values and separating query containing values
            second_ranked_qs = results.exclude(
                id__in=first_ranked_qs.values_list("id", flat=True)
            ).order_by("frequency", Length("word"))[:25]

            if exact_match:
                # removing exact match from unwanted rank
                first_ranked_qs = first_ranked_qs.exclude(id=exact_match.first().id)

            # not using '|' to maintain order though performance is better in '|'
            merged_results = list(
                chain(
                    exact_match.values_list("word", flat=True),
                    first_ranked_qs.values_list().values_list("word", flat=True),
                    second_ranked_qs.values_list("word", flat=True),
                )
            )[:25]
            return JsonResponse({"data": merged_results}, safe=False)
        return JsonResponse({"error": "Bad Request"}, status=400)


class SearchTemplateView(TemplateView):
    template_name = 'suggestion/search.html'


