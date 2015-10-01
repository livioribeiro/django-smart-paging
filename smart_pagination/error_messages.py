from django.core.paginator import Page

MISSING_FIRST_ARG = 'Missing first argument (instance of "{}")'.format(Page.__qualname__)
MISSING_SECOND_ARG = 'Missing second argument (number of links)'

WRONG_FIRST_ARG = 'First parameter must be an instance of "{}"'.format(Page.__qualname__)
WRONG_SECOND_ARG = 'Second parameter must be an instance of "{}"'.format(int.__qualname__)

WRONG_ARGS = '"{{}}" requires an instance of "{}",' \
             ' the number of links to show' \
             ' and, optionally, the "page_kwarg" name'.format(Page.__qualname__)