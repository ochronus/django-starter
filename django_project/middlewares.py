def set_correct_ip_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        if 'HTTP_X_FORWARDED_FOR' in request.META:
            request.META['REMOTE_ADDR'] = request.META['HTTP_X_FORWARDED_FOR'].split(",")[0].strip()

        response = get_response(request)

        return response

    return middleware
