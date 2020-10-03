from django.shortcuts import render


def index(request):
    """
    function based view
    :param request:
    :return: Hello Full Cycle Developer!
    """
    return render(request, 'index.html')
