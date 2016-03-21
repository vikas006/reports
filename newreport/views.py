from django.http import HttpResponse
from xhtml2pdf import pisa
import cStringIO as StringIO
from django.template.loader import get_template
from django.template import Context


def html_to_pdf_directly(request):
    template = get_template("home.html")
    context = Context({'pagesize': 'A4', 'data': 'abc'})
    html = template.render(context)
    result = StringIO.StringIO()
    pdf = pisa.pisaDocument(StringIO.StringIO(html), dest=result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    else:
        return HttpResponse('Errors')
