from upload_avatar import get_uploadavatar_context

@login_required
def upload(request):
    return render_to_response(
        'upload.html',
        get_uploadavatar_context(),
        context_instance = RequestContext(request)
    )# Create your views here.
